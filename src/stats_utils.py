from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


def retention_formula(day: int, a: float, b: float) -> float:
    """A general formula to calculate retention

    Args:
        day (int): Day to calculate the retention
        a (float): First parameter
        b (float): Second parameter

    Returns:
        float: Retention for the given day with the parameters
    """
    return a * np.exp(-b * (day - 1))


def fit_retention_curve(
    days: list[int], retentions: list[float]
) -> tuple[float, float]:
    """Fits a curve to given data and returns parameters

    Args:
        days (list[int]): Days for which the retentions are known
        retentions (list[float]): Retentions for the corresponding days

    Raises:
        ValueError: If days and retentions have different lengths

    Returns:
        tuple[float, float]: Returns fitted parameters for the formula
    """
    if len(days) != len(retentions):
        raise ValueError("Days and retentions must have the same length!")

    parameters, _ = curve_fit(retention_formula, days, retentions)
    a, b = parameters
    return a, b


def calculate_daily_active_users(
    day_number: int, installs_per_day: int, parameters: tuple[float, float]
) -> int:
    """
        Calculates daily active users count for given day count, same day install are excluded.

        Uses the formula
            DAU(x) = N * sum(R(i))
        where:
            x is the day_number,
            N is installs_per_day,
            R(i) is retention on day i after install
            i goes from 1 to x.

    Args:
        day_number (int): Day to find the DAU for.
        installs_per_day (int): Assuming install count is the same everyday
        parameters (tuple[float, float]): Parameters for retention formula (a, b)

    Returns:
        int: Total DAU after 'day_number' days
    """
    a, b = parameters
    result = installs_per_day * sum(
        [retention_formula(day, a, b) for day in range(1, day_number + 1)]
    )
    return int(result)


def calculate_total_revenue(
    start_day: int,
    end_day: int,
    dpr: float,
    ecpm: float,
    installs_per_day: int,
    parameters: tuple[float, float],
    AMSPP: float = 1,
) -> float:
    """Calculates total revenue between [start_day, end_day)

    Args:
        start_day (int): Starting day of simulating the calculation.
        end_day (int): Ending day of simulating the calculation. end_day is excluded.
        dpr (float): Daily purchase ratio, purchases / DAU
        ecpm (float): Ad revenue per 1000 impression
        installs_per_day (int): Number of installs per day
        parameters (tuple[float, float]): Parameters for retention formula (a, b)
        AMSPP (float, optional): Average money spent by players each day. Defaults to 1.

    Returns:
        float: Total revenue until 'until_day'
    """
    total_revenue = 0.0
    for day in range(start_day, end_day):
        dau = calculate_daily_active_users(day, installs_per_day, parameters)

        ad_revenue_per_day = dau * ecpm / 1000
        purchase_revenue_per_day = dpr * dau * AMSPP

        total_revenue_per_day = ad_revenue_per_day + purchase_revenue_per_day
        total_revenue += total_revenue_per_day
    return total_revenue


def percentage_difference(a: float, b: float) -> float:
    """Calculate the percentage difference between two numbers"""
    return (b - a) / a * 100


################ Task 2
def calculate_retention(df: pd.DataFrame, day_number: int):
    df["days_after_install"] = (df["event_date"] - df["install_date"]).dt.days

    total_installs = df.groupby("install_date")["user_id"].nunique()
    active_users = (
        df[df["days_after_install"] == day_number]
        .groupby("install_date")["user_id"]
        .nunique()
    )

    retention = (active_users / total_installs) * 100
    retention.dropna()
    return retention
