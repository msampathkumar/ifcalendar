# Plan for Improving the `ifcalendar` Library

To scale this project, make it impactful, and improve it, we need to address core functionality, performance, integration with data science tools, and developer experience. Here is a prioritized plan for ongoing improvement.

**This plan should be reviewed and updated every week.**

## 1. Core Functionality & Missing Features

Currently, `ifcalendar` is primarily a one-way converter (from `datetime` to `IFCDate`). To make it truly useful, it needs a full suite of date operations.

*   **Reverse Conversion:** Implement `to_datetime(ifc_date)` to convert an IFC date back to a standard Gregorian `datetime` object.
*   **Date Arithmetic:** Implement `__add__` and `__sub__` for `IFCDate` to allow adding/subtracting days, weeks, and months (e.g., `date + timedelta(days=5)`).
*   **Comparisons:** Implement rich comparison methods (`__eq__`, `__lt__`, `__gt__`, etc.) so `IFCDate` objects can be sorted and compared.
*   **String Formatting:** Implement a `strftime`-like method for custom formatting of IFC dates (e.g., `date.strftime("%Y-%m-%d")`).
*   **Timezone Support:** Ensure that conversions handle timezones correctly or explicitly document that it is timezone-naive.

## 2. Scaling & Impactful Integrations (Data Science Focus)

The primary use case outlined in the `INTRO.md` is statistical analysis. To make a real impact, `ifcalendar` must integrate seamlessly with the Python data science ecosystem.

*   **Pandas/NumPy Support:** This is the most critical feature for scaling.
    *   Create a custom Pandas Extension Array/Dtype for `IFCDate`.
    *   Provide vectorized conversion functions for Pandas DataFrames/Series (e.g., `df['date_col'].ifc.to_ifc()`).
    *   *Why?* Calculating dates row-by-row in Python is too slow for large datasets. Vectorization via NumPy is required for performance.
*   **Matplotlib / Seaborn Integration:**
    *   Create custom Matplotlib locators and formatters so that plots can natively display 13 equal-length months on the X-axis without distortion.
    *   Provide examples in the documentation showing how to plot time-series data using IFC dates.

## 3. Architecture & Code Quality Improvements

The existing codebase is simple but needs modernizing to be robust and maintainable.

*   **Refactor `IFC` Class to Dataclasses:**
    *   Separate the calculation logic from the data storage.
    *   Create a `dataclass` (e.g., `IFCDate`) to represent the date.
    *   This will make the objects lighter, immutable, and easier to test.
*   **Migrate Testing Framework:**
    *   The project currently uses `nose`, which is unmaintained and deprecated.
    *   Migrate all tests to `pytest`.
    *   Add parameterized tests to thoroughly check edge cases (leap years, year days, month boundaries).
*   **Type Hinting:**
    *   Add Python type hints (`typing`) to all functions and methods. This improves developer experience, allows static analysis (e.g., `mypy`), and serves as documentation.
*   **Linting & Formatting:**
    *   Integrate `black` (for formatting), `isort` (for imports), and `flake8` or `ruff` (for linting) into the `Makefile` and CI pipeline.

## 4. Developer Experience & Ecosystem

To grow the user base, the library must be easy to discover, learn, and use.

*   **CLI Tool:** Create a simple command-line interface (e.g., `ifcalendar today` or `ifcalendar convert 2024-05-10`) so users can play with it without writing Python code.
*   **Documentation:**
    *   Set up Sphinx or MkDocs to generate API documentation.
    *   Include a "Quickstart" guide and a "Data Science Tutorial" (Jupyter Notebook format) demonstrating the advantages over the Gregorian calendar.
*   **Continuous Integration (CI):**
    *   Set up GitHub Actions to automatically run tests, linting, and build steps on every pull request and push to main.

## Weekly Review Checklist

*   [ ] Review user issues and PRs on GitHub.
*   [ ] Prioritize one feature from the "Data Science Integrations" block.
*   [ ] Ensure test coverage remains high (>95%).
*   [ ] Update this `plan.md` with new findings and shifting priorities.
