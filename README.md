# Beginner Python Course

This workspace contains a complete beginner-focused Python course delivered as Jupyter notebooks.

## Course Structure

- `00_Syllabus.ipynb` — course overview and roadmap
- `01_Introduction_Getting_Started.ipynb` — setup, fundamentals, and initial exercises
- `02_Python_Basics.ipynb` — expressions, strings, formatting, and type conversion
- `03_Control_Flow.ipynb` — branching, loops, and comprehensions
- `04_Data_Structures.ipynb` — lists, tuples, sets, dictionaries
- `05_Functions_Modules.ipynb` — functions, arguments, and modules
- `06_File_IO_Errors.ipynb` — file reading/writing and error handling
- `07_Object_Oriented_Programming.ipynb` — classes, methods, inheritance
- `08_Virtual_Environments_and_Packaging.ipynb` — venv, pip, packaging basics
- `09_Testing_and_Debugging.ipynb` — pytest/unittest, assertions, logging
- `10_Working_with_Data.ipynb` — CSV, JSON, pandas
- `11_Web_and_APIs.ipynb` — requests, APIs, basic HTML parsing
- `12_Final_Projects_and_Next_Steps.ipynb` — capstones, review, roadmap

## Setup

Use the included virtual environment or create a new one:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Running Tests

Use the helper script to run tests from the course root:

Windows:
```powershell
.\run_tests.bat
```

macOS / Linux:
```bash
./run_tests.sh
```

Run one module's tests by passing the module test file:

Windows:
```powershell
.\run_tests.bat tests/test_module1.py
.\run_tests.bat tests/test_module2.py
```

macOS / Linux:
```bash
./run_tests.sh tests/test_module1.py
./run_tests.sh tests/test_module2.py
```

You can also use plain `pytest`:

```bash
pytest -q
pytest -q tests/test_module1.py
pytest -q tests/test_module2.py
```

## Notes

This course is designed for self-paced learners and includes examples, exercises, and mini-projects in each module. Use the notebooks interactively and modify code to explore further.
