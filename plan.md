### Plan for Improving the `ifcalendar` Library

Here are some opportunities to improve the `ifcalendar` library, with a focus on a test-driven approach and simplicity.

#### 1. Refactor the `IFC` Class

The `IFC` class is a good start, but it can be improved. The properties are currently calling the `get_*` functions directly. This is not ideal because it makes the class harder to test and maintain.

**Plan:**

1.  **Create a `dataclasses` file:** Create a new file `ifcalendar/dataclasses.py` to define a `IFCDate` dataclass. This class will hold the calculated date information (day, week, month, etc.).
2.  **Refactor `IFC` class:** The `IFC` class should be responsible for the calculations, and it should return an `IFCDate` object. The properties on the `IFC` class should be removed.
3.  **Update tests:** The tests will need to be updated to reflect these changes.

#### 2. Improve Test Coverage

The current test suite is a good start, but it can be improved. There are several functions that are not tested, and the existing tests could be more thorough.

**Plan:**

1.  **Add tests for all `get_*` functions:** Add unit tests for `get_week_ct`, `get_day_of_week`, `get_week_day`, and `get_month_name`.
2.  **Add tests for `to_ifc`:** Add unit tests for the `to_ifc` function.
3.  **Add tests for the `IFC` class:** Add unit tests for the `IFC` class itself, to test its initialization and the `__repr__` method.
4.  **Use a test runner:** Configure the project to use a test runner like `pytest`. This will make it easier to run the tests and get coverage reports.

#### 3. Improve Code Quality

The code is generally well-written, but there are a few areas that could be improved.

**Plan:**

1.  **Add docstrings:** Add docstrings to all functions and classes, explaining what they do, their parameters, and what they return.
2.  **Use f-strings:** Use f-strings for string formatting instead of the `format()` method.
3.  **Use a linter:** Configure the project to use a linter like `flake8` or `pylint`. This will help to enforce a consistent code style and catch potential errors.
4.  **Use a code formatter:** Configure the project to use a code formatter like `black`. This will automatically format the code to a consistent style.

#### 4. Add a `Makefile`

A `Makefile` can be used to automate common tasks, such as running tests, linting the code, and building the project.

**Plan:**

1.  **Create a `Makefile`:** Create a `Makefile` with targets for `test`, `lint`, `format`, and `build`.
2.  **Update `README.md`:** Update the `README.md` file to explain how to use the `Makefile`.
