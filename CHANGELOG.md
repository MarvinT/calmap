# Changelog

## 0.0.12 - 2026-06-15

- Add support for Python 3.10 through 3.14.
- Replace Travis CI and password-based deployment with GitHub Actions and PyPI
  trusted publishing.
- Move package metadata to `pyproject.toml`.
- Fix aggregation of multiple timestamps within the same calendar day.
- Respect custom month labels and month tick selection.
- Add current pandas, matplotlib, package-build, and documentation checks.
