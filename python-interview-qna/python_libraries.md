![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Libraries

## Q1. What is a library in Python?
**Answer:**  
A library is a collection of modules and packages that provide pre-written functionality for developers.

## Q2. What is the difference between module, package, and library?
**Answer:**  
- **Module** → single `.py` file.  
- **Package** → collection of modules with `__init__.py`.  
- **Library** → collection of related packages and modules (e.g., NumPy, Pandas).

## Q3. What is the Python Standard Library?
**Answer:**  
A collection of modules packaged with Python installation (e.g., `os`, `sys`, `math`, `json`).

## Q4. How do you install third-party libraries?
**Answer:**  
Using `pip`:  
```bash
pip install requests
```

## Q5. How do you check installed libraries?
**Answer:**  
Run `pip list` or `pip freeze`.

## Q6. How do you import a library in Python?
**Answer:**  
```python
import math
print(math.sqrt(16))
```

## Q7. What is the difference between `import` and `from ... import`?
**Answer:**  
- `import math` → access with `math.sqrt()`  
- `from math import sqrt` → use directly `sqrt()`

## Q8. How do you alias a library?
**Answer:**  
Use `as`.  
```python
import numpy as np
```

## Q9. What is the role of `__all__` in a library?
**Answer:**  
It defines the list of symbols exported when `from module import *` is used.

## Q10. What is the difference between standard and third-party libraries?
**Answer:**  
- Standard → included with Python (`datetime`, `os`).  
- Third-party → installed via `pip` (`requests`, `pandas`).

## Q11. What are some widely used Python libraries?
**Answer:**  
- **Data Science** → NumPy, Pandas, Matplotlib  
- **Web** → Flask, Django, FastAPI  
- **ML/AI** → TensorFlow, PyTorch, Scikit-learn  
- **Automation** → Selenium, Requests

## Q12. How do you check the version of a library?
**Answer:**  
```python
import pandas
print(pandas.__version__)
```

## Q13. How do you upgrade a library?
**Answer:**  
```bash
pip install --upgrade pandas
```

## Q14. What is the difference between `requirements.txt` and `pyproject.toml`?
**Answer:**  
- `requirements.txt` → simple list of dependencies.  
- `pyproject.toml` → modern packaging/management standard with build system support.

## Q15. What is `venv` used for with libraries?
**Answer:**  
It creates isolated environments so each project can have its own dependencies.

## Q16. How do you uninstall a library?
**Answer:**  
```bash
pip uninstall requests
```

## Q17. What is the difference between `pip` and `conda`?
**Answer:**  
- `pip` → installs Python packages.  
- `conda` → installs Python + non-Python dependencies (e.g., C libs).

## Q18. How do you check where a library is installed?
**Answer:**  
```python
import requests
print(requests.__file__)
```

## Q19. How do you handle version conflicts in libraries?
**Answer:**  
- Use `pip install package==version`  
- Use virtual environments  
- Consider dependency managers like Poetry or Pipenv.

## Q20. Why are libraries important in Python?
**Answer:**  
They save development time by providing reusable, tested code for common tasks, enabling rapid application development.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
