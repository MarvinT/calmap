# Calendar heatmaps from pandas time series data

[![PyPI version](https://img.shields.io/pypi/v/calmap.svg)](https://pypi.org/project/calmap/)
[![Python versions](https://img.shields.io/pypi/pyversions/calmap.svg)](https://pypi.org/project/calmap/)
[![CI](https://github.com/MarvinT/calmap/actions/workflows/ci.yml/badge.svg)](https://github.com/MarvinT/calmap/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/calmap)](https://pepy.tech/project/calmap)

Plot [pandas](https://pandas.pydata.org/) time series data sampled by day in
a heatmap per calendar year, similar to GitHub's contributions plot, using
[matplotlib](https://matplotlib.org/).

## Installation

```console
python -m pip install calmap
```

## Usage

```python
import calmap
import pandas as pd

events = pd.Series(
    [1, 2, 3],
    index=pd.to_datetime(["2025-01-01", "2025-01-02", "2025-02-01"]),
)
calmap.yearplot(events, year=2025)
```

Use `calmap.calendarplot(events)` to draw multiple years. See the
[API documentation](https://github.com/MarvinT/calmap/blob/master/doc/index.rst)
for all options.

The canonical source repository is
[`MarvinT/calmap`](https://github.com/MarvinT/calmap). The original
`martijnvermaat/calmap` repository points here for continued maintenance.
