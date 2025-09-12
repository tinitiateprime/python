![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Custom Module Folder

## Q1. What is a custom module folder in Python?
**Answer:**  
A directory containing multiple Python modules, usually structured as a package with an `__init__.py` file.

## Q2. Why use a custom module folder?
**Answer:**  
To organize related modules together, improve reusability, and maintain cleaner project structure.

## Q3. How do you create a custom module folder?
**Answer:**  
- Create a folder  
- Add module `.py` files  
- Include an `__init__.py` file

## Q4. What is the role of `__init__.py`?
**Answer:**  
Marks the folder as a package and controls what is exported when imported.

## Q5. How do you import a module from a custom folder?
**Answer:**  
```python
from mypackage import mymodule
```

## Q6. How do you import specific functions from a custom module?
**Answer:**  
```python
from mypackage.mymodule import greet
greet()
```

## Q7. How do you control exports using `__all__`?
**Answer:**  
Define a list of allowed imports in `__init__.py`.  
```python
__all__ = ["mymodule"]
```

## Q8. Can a custom module folder contain sub-packages?
**Answer:**  
Yes, subfolders with their own `__init__.py` act as sub-packages.

## Q9. What is the difference between `import package.module` and `from package import module`?
**Answer:**  
- `import package.module`: Must use full path to call functions.  
- `from package import module`: Can call directly.

## Q10. How do you execute a package as a script?
**Answer:**  
Use the `-m` flag.  
```bash
python -m mypackage.mymodule
```

## Q11. What is a namespace package?
**Answer:**  
A package without `__init__.py`, introduced in Python 3.3+, allowing splitting across directories.

## Q12. How do you access a module from a specific path?
**Answer:**  
Modify `sys.path` or use `importlib`.  
```python
import sys
sys.path.append("/path/to/mypackage")
import mymodule
```

## Q13. How do you make a module executable?
**Answer:**  
Add `if __name__ == "__main__":` in the module file.

## Q14. What is the benefit of grouping related modules?
**Answer:**  
- Better organization  
- Easier maintainability  
- Avoids naming conflicts

## Q15. Can a package be imported without `__init__.py`?
**Answer:**  
Yes, in Python 3.3+, but older versions require it.

## Q16. How do you distribute a custom module folder?
**Answer:**  
Package it with `setup.py` or `pyproject.toml` and distribute via `pip`.

## Q17. How do you alias a module from a custom folder?
**Answer:**  
```python
import mypackage.mymodule as mm
mm.greet()
```

## Q18. How do you test modules inside a package?
**Answer:**  
Use relative imports (`from . import module`) or run with `pytest`.

## Q19. How do you make package-level initialization code run?
**Answer:**  
Put the code inside `__init__.py`.

## Q20. What is the best practice for structuring custom module folders?
**Answer:**  
- Include `__init__.py`  
- Use clear names  
- Group logically related modules  
- Provide docstrings and comments

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
