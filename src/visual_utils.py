from typing import Callable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .stats_utils import retention_formula


def show_retention_curve(
    original_days: list[int],
    original_retentions: list[float],
    parameters: tuple[float, float],
    start_day: int = 1,
    end_day: int = 15,
    name: str = "",
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
        name (str, optional): Name of the plot. Defaults to "".

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
    plt.title("Exponential Retention Model for " + name)
    plt.legend()
    plt.show()


##### Task 2 #####


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


def plot_data_line(
    x_values: list,
    y_values: list,
    label: str = "",
    x_rotation=0,
    y_scale: str = "linear",
    plot_title: str = "",
):
    """Plots a line chart with given x and y values

    Args:
        x_values (list): x-axis values
        y_values (list): y-axis values
        label (str, optional): Label for the line. Defaults to "".
        x_rotation (float, optional): Rotation for x values, mainly used for dates. Defaults to 0.
        y_scale (str, optional): Scale of the plot. Defaults to "linear".
        plot_title (str, optional): Title of the plot. Defaults to "".
    """
    plt.figure(figsize=(8, 6))
    plt.title(plot_title)

    plt.plot(
        x_values,
        y_values,
        label=label,
    )

    plt.xticks(rotation=x_rotation)
    plt.tight_layout()
    plt.yscale(y_scale)
    plt.legend()
    plt.show()


def plot_data_line_multiple(
    multiple_x_values: list[list],
    multiple_y_values: list[list],
    labels: list[str] = [],
    x_rotation: float = 0,
    y_scale: str = "linear",
    plot_title: str = "",
):
    """
    Plots line graph containing multiple lines with given x and y values

        Example:
            multiple_x_values = [[1, 2], [2, 3], [1, 2, 3, 4, 5]]\n
            multiple_y_values = [[9, 10], [7, 2], [15, 17, 19, 10, 3]]\n
            The function will match the arrays and plot the lines.\n
            Length of lines may differ, but pairwise length of x and y values must be the same.

    Args:
        multiple_x_values (list[list]): list of x-axis values.
        multiple_y_values (list[list]): y-axis values
        labels (list[str], optional): Labels for the lines. Must be given for either all lines or none.
        x_rotation (float, optional): Rotation for x values, mainly used for dates. Defaults to 0.
        y_scale (str, optional): Scale of the plot. Defaults to "linear".
        plot_title (str, optional): Title of the plot. Defaults to "".
    """
    if len(multiple_x_values) != len(multiple_y_values):
        raise ValueError("Count of arrays to plot must be the same!")

    if len(labels) not in [0, len(multiple_x_values)]:
        raise ValueError("Label count must either be 0 or the same as plot count!")
    labels = [i + 1 for i in range(len(multiple_x_values))] if labels == [] else labels

    plt.figure(figsize=(8, 6))
    plt.title(plot_title)

    for x_values, y_values, label in zip(multiple_x_values, multiple_y_values, labels):
        if len(x_values) != len(y_values):
            raise ValueError("Arrays for x and y values to be plotted must match!")
        plt.plot(x_values, y_values, label=label)

    plt.xticks(rotation=x_rotation)
    plt.tight_layout()
    plt.yscale(y_scale)
    plt.legend()
    plt.show()


def plot_by_segment(
    df: pd.DataFrame,
    segments: list[str],
    segment_column: str,
    compute_series: Callable[[pd.DataFrame], pd.Series],
    title: str = "",
    x_rotation: float = 45,
):
    """Plots line graphs by segments for data in dataframe with given function

    Args:
        df (pd.DataFrame): Dataframe that holds the data.
        segments (list[str]): Segments to draw the lines for.
        segment_column (str): Name of the column the segments are kept.
        compute_series (Callable[[pd.DataFrame], pd.Series]):
            Function to use to find processed data.
            The function has to have dataframe as input and return series.
        title (str, optional): Title of the plot. Defaults to "".
        x_rotation (float, optional): Rotation for x values, mainly used for dates. Defaults to 45.
    """
    x_values_list, y_values_list, labels = [], [], []
    for segment in segments:
        segment_df = df[df[segment_column] == segment]

        processed_series = compute_series(segment_df)

        x_values_list.append(processed_series.index)
        y_values_list.append(processed_series.values)
        labels.append(segment)

    plot_data_line_multiple(
        x_values_list, y_values_list, labels, x_rotation, plot_title=title
    )
