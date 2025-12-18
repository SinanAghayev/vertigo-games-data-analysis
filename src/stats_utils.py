from scipy.optimize import curve_fit
import numpy as np


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
