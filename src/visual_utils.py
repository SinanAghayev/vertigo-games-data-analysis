import numpy as np
import matplotlib.pyplot as plt
from .stats_utils import retention_formula


def show_retention_curve(
    original_days: list[int],
    original_retentions: list[float],
    parameters: tuple[float, float],
    start_day: int = 1,
    end_day: int = 15,
):
    """Plots given retentions and fitted curve and shows them

    Args:
        original_days (list[int]): Days for which retentions are known
        original_retentions (list[float]): Retentions for the corresponding days
        parameters (tuple[float, float]):
            Fitted parameters of model (a, b)
            R(d) = a * exp(-b * (d - 1))
        start_day (int, optional): Day the plotting of curve starts. Defaults to 1.
        end_day (int, optional): Day the plotting of curve ends. Defaults to 15.

    Raises:
        ValueError: If days and retentions have different lengths

    """
    if len(original_days) != len(original_retentions):
        raise ValueError("Days and retentions must have the same length!")

    days_to_show = np.array([i for i in range(start_day, end_day + 1)])

    a, b = parameters
    fitted_retentions = [retention_formula(day, a, b) for day in days_to_show]

    # Plot original data
    plt.plot(original_days, original_retentions, "o", color="red", label="Known Data")
    # Plot fitted curve
    plt.plot(days_to_show, fitted_retentions, color="blue", label="Fitted curve")

    plt.xlabel("Days")
    plt.ylabel("Retention")
    plt.title("Exponential Retention Model")
    plt.legend()
    plt.show()


def plot_data_bar(x_values: list[any], y_values: list[any], x_rotation=0):
    """Plots a bar chart with given x and y values

    Args:
        x_values (list): x-axis values
        y_values (list): y-axis values
        x_rotation (int, optional): Rotation for x values, mainly for dates. Defaults to 0.
    """
    plt.figure(figsize=(8, 6))

    plt.bar(
        x_values,
        y_values,
    )

    plt.xticks(rotation=x_rotation)
    plt.tight_layout()
    plt.legend()
    plt.show()


def plot_data_line(x_values, y_values, x_rotation=0):
    """Plots a line chart with given x and y values

    Args:
        x_values (list): x-axis values
        y_values (list): y-axis values
        x_rotation (int, optional): Rotation for x values, mainly for dates. Defaults to 0.
    """
    plt.figure(figsize=(8, 6))

    plt.plot(
        x_values,
        y_values,
    )

    plt.xticks(rotation=x_rotation)
    plt.tight_layout()
    plt.legend()
    plt.show()
