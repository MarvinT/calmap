"""
Tests for calmap.
"""


import numpy as np

np.random.seed(sum(map(ord, "calmap")))
import matplotlib.pyplot as plt
import pandas as pd
import pytest

import calmap


@pytest.fixture
def events():
    """
    We create 500 events as random float values assigned to random days over a
    700-day period.
    """
    all_days = pd.date_range("1/15/2014", periods=700, freq="D")
    days = np.random.choice(all_days, 500)
    return pd.Series(np.random.randn(len(days)), index=days)


def test_yearplot(events):
    """
    By default, `yearplot` plots the first year and sums the values per day.
    """
    ax = calmap.yearplot(events)
    assert len(ax.collections) == 2
    plt.close(ax.figure)


def test_yearplot_year(events):
    """
    We can choose which year is plotted with the `year` keyword argment.
    """
    ax = calmap.yearplot(events, year=2015)
    assert ax.get_xlim()[1] >= 52
    plt.close(ax.figure)


def test_yearplot_cmap_fillcolor_linewidth(events):
    """
    The appearance can be changed by using another colormap. Here we also use
    a darker fill color for days without data and remove the lines.
    """
    ax = calmap.yearplot(events, cmap="YlGn", fillcolor="grey", linewidth=0)
    assert ax.collections[1].get_linewidths()[0] == 0
    plt.close(ax.figure)


def test_yearplot_monthticks_daylabels_dayticks(events):
    """
    We can ask to draw only every nth label, or explicitely supply the label
    indices. The labels themselves can also be customized.
    """
    ax = calmap.yearplot(
        events, monthticks=3, daylabels="MTWTFSS", dayticks=[0, 2, 4, 6]
    )
    assert [label.get_text() for label in ax.get_xticklabels()] == [
        "Feb",
        "May",
        "Aug",
        "Nov",
    ]
    assert [label.get_text() for label in ax.get_yticklabels()] == [
        "M",
        "W",
        "F",
        "S",
    ]
    plt.close(ax.figure)


def test_calendarplot(events):
    """
    With `calendarplot` we can plot several years in one figure.
    """
    fig, axes = calmap.calendarplot(events)
    assert len(axes) == 2
    plt.close(fig)


def test_calendarplot_columns(events):
    """
    We can specify a number of columns.
    """
    fig, axes = calmap.calendarplot(events, ncols=2)
    assert axes.shape == (2,)
    plt.close(fig)


def test_yearplot_aggregates_values_by_calendar_day():
    events = pd.Series(
        [1.0, 2.0],
        index=pd.to_datetime(["2025-01-01 08:00", "2025-01-01 16:00"]),
    )

    ax = calmap.yearplot(events)

    assert 3.0 in ax.collections[1].get_array().compressed()
    plt.close(ax.figure)


def test_yearplot_uses_custom_month_labels(events):
    labels = [f"M{i}" for i in range(1, 13)]

    ax = calmap.yearplot(events, monthlabels=labels, monthticks=[0, 6, 11])

    assert [label.get_text() for label in ax.get_xticklabels()] == [
        "M1",
        "M7",
        "M12",
    ]
    plt.close(ax.figure)


@pytest.mark.parametrize("ncols", [0, -1, 1.5, True])
def test_calendarplot_rejects_invalid_ncols(events, ncols):
    with pytest.raises(ValueError, match="positive integer"):
        calmap.calendarplot(events, ncols=ncols)
