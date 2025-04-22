# 🧠 Type Annotations in Python 3 — with `mypy` Static Checking


A curated set of Python examples showcasing **type annotations**, **static typing**, and **clean function signatures** using the `typing` module and validated with [`mypy`](https://mypy-lang.org/).

---

## 📌 Table of Contents

- [📚 Overview](#-overview)
- [🧠 Concepts Covered](#-concepts-covered)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🧪 Run Type Checking](#-run-type-checking)
- [📘 Learn More](#-learn-more)
- [👨‍💻 Author](#-author)
- [📜 License](#-license)

---

## 📚 Overview

This project demonstrates how to:

- Use type hints with basic and advanced Python types.
- Structure functions with precise type annotations.
- Validate type safety using `mypy`.
- Apply real use cases with `List`, `Union`, `Optional`, `Callable`, `TypedDict`, and `Protocol`.

---

## 🧠 Concepts Covered

✔️ Function annotations\
✔️ Variable type declarations\
✔️ `Union`, `Optional`, `Callable`, `TypedDict`, `Protocol`\
✔️ Static analysis with `mypy`\
✔️ Reusable patterns for production code

---

## 📁 Project Structure

- `0-add.py` ➜ 🧮 Adds two integers
- `1-concat.py` ➜ 🔤 Concatenates two strings
- `2-floor.py` ➜ 📉 Rounds down a float
- `3-to_str.py` ➜ 🔁 Converts a float to string
- `4-define_variables.py` ➜ 📦 Defines typed variables
- `5-sum_list.py` ➜ ➕ Sums a list of floats
- `6-sum_mixed_list.py` ➜ 🔀 Sums mixed int and float list
- `7-to_kv.py` ➜ 🎁 Returns tuple with string and squared value
- `8-make_multiplier.py` ➜ 🔧 Returns a multiplier function (`Callable`)
- `9-element_length.py` ➜ 📏 Returns element lengths as tuples

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- `mypy` installed

```bash
pip install mypy
```

---

## 🧪 Run Type Checking

Run `mypy` in the root of the project:

```bash
mypy .
```

You can also configure a `mypy.ini` file:

```ini
[mypy]
python_version = 3.8
disallow_untyped_defs = True
warn_return_any = True
ignore_missing_imports = True
```

---

## 📘 Learn More

- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Python ](https://docs.python.org/3/library/typing.html)[`typing`](https://docs.python.org/3/library/typing.html)[ module](https://docs.python.org/3/library/typing.html)

---

## 👨‍💻 Author

**Adolfo Rodriguez**

&#x20;
