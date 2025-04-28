# 🚀 Python Async Comprehension Project

A curated set of Python examples demonstrating asynchronous programming patterns, including generators, comprehensions, and parallel execution, fully type-annotated and following `pycodestyle` standards.

---

## 📌 Table of Contents

- 📚 Overview
- 🧠 Concepts Covered
- 🛠️ Requirements
- 📁 Project Structure
- 🚀 Getting Started
- 🧪 How to Run
- 📘 Learn More
- 👨‍💻 Author

---

## 📚 Overview

This project showcases:

- How to use asynchronous generators in Python 3.
- How to build asynchronous comprehensions.
- How to execute multiple coroutines in parallel efficiently.
- Full compliance with `pycodestyle` and proper documentation standards.
- Type-annotated functions for static analysis.

All examples are compatible with Python 3.9 and were tested on Ubuntu 20.04 LTS.

---

## 🧠 Concepts Covered

✔️ Asynchronous programming fundamentals\
✔️ Async generators with `yield` and `await`\
✔️ Async comprehensions (collecting async-generated values)\
✔️ Parallel execution with `asyncio.gather`\
✔️ Runtime measurement of asynchronous code\
✔️ Type annotations for all functions and coroutines\
✔️ Proper documentation in modules and functions\
✔️ Compliance with `pycodestyle` and static code validation

---

## 🛠️ Requirements

- Python 3.9+
- `pycodestyle` (version 2.5.x)
- Ubuntu 20.04 LTS
- Editors: `vi`, `vim`, or `emacs`

**Mandatory Standards:**

- Every file must start with: `#!/usr/bin/env python3`
- Every file must end with a newline.
- Documentation for all modules and functions.
- Type annotations required.
- Length checkable with `wc`.

Install `pycodestyle`:

```bash
pip install pycodestyle==2.5.0
```

---

## 📁 Project Structure

```bash
holbertonschool-web_back_end/
└── python_async_comprehension/
    ├── 0-async_generator.py ➔ 🔄 Async generator yielding random floats
    ├── 1-async_comprehension.py ➔ 📅 Async comprehension collecting values
    ├── 2-measure_runtime.py ➔ ⏱️ Runtime measurement with parallel tasks
    ├── 0-main.py ➔ 🔹 Tester for 0-async_generator
    ├── 1-main.py ➔ 🔹 Tester for 1-async_comprehension
    ├── 2-main.py ➔ 🔹 Tester for 2-measure_runtime
    └── README.md ➔ 📘 Project documentation
```

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end/python_async_comprehension
```

2. Ensure Python 3.9+ is installed.

3. Run `pycodestyle` to check for style compliance:

```bash
pycodestyle .
```

4. Execute the test files:

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
```

---

## 🧪 How to Run

- **Test Async Generator:**
  ```bash
  python3 0-main.py
  ```
- **Test Async Comprehension:**
  ```bash
  python3 1-main.py
  ```
- **Measure Runtime with Parallel Execution:**
  ```bash
  python3 2-main.py
  ```

---

## 📘 Learn More

- [PEP 492 – Coroutines with async and await syntax](https://peps.python.org/pep-0492/)
- [asyncio — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)

---

## 👨‍💻 Author

**Adolfo Rodriguez**\
💼 [LinkedIn](https://www.linkedin.com/in/adolfo-rodriguez-22b178330/) | 💻 [GitHub](https://github.com/Adolfo2231)
