![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# Python Modules

## Q1. What is a module in Python?
**Answer:**  
A module is a file containing Python code (functions, classes, variables) that can be imported and reused.

## Q2. How do you create a module?
**Answer:**  
Save Python code in a `.py` file.  
```python
# mymodule.py
def greet(): print("Hello")
```

## Q3. How do you import a module?
**Answer:**  
Use the `import` statement.  
```python
import mymodule
mymodule.greet()
```

## Q4. What is the difference between `import module` and `from module import`?
**Answer:**  
- `import module`: Requires prefix `module.func()`.  
- `from module import func`: Can call `func()` directly.

## Q5. How do you import all functions from a module?
**Answer:**  
Use `from module import *` (not recommended, can cause conflicts).

## Q6. What is the `as` keyword used for in import?
**Answer:**  
It creates an alias.  
```python
import numpy as np
```

## Q7. What is the difference between module and package?
**Answer:**  
- Module → single `.py` file.  
- Package → collection of modules with `__init__.py`.

## Q8. Where does Python look for modules?
**Answer:**  
- Current directory  
- Built-in standard library  
- Paths listed in `sys.path`

## Q9. How do you reload a module?
**Answer:**  
Use `importlib.reload()`.  
```python
import importlib, mymodule
importlib.reload(mymodule)
```

## Q10. How do you check module location?
**Answer:**  
```python
import math
print(math.__file__)
```

## Q11. What is the difference between built-in and user-defined modules?
**Answer:**  
- Built-in → come with Python (`math`, `os`).  
- User-defined → created by developers.

## Q12. How do you see all functions inside a module?
**Answer:**  
Use `dir(module)`.  
```python
import math
print(dir(math))
```

## Q13. What is the role of `__name__` in a module?
**Answer:**  
`__name__` helps identify if the file is run directly (`__main__`) or imported.

## Q14. How do you create an executable module?
**Answer:**  
Include:  
```python
if __name__ == "__main__":
    main()
```

## Q15. What is the benefit of using modules?
**Answer:**  
- Code reusability  
- Better organization  
- Easier debugging and testing

## Q16. What are some commonly used standard library modules?
**Answer:**  
`os`, `sys`, `math`, `datetime`, `json`, `random`, `collections`

## Q17. How do you check installed modules in Python?
**Answer:**  
Run `pip list` or check with `help("modules")`.

## Q18. What is a namespace in modules?
**Answer:**  
A container where variable and function names are mapped to objects inside a module.

## Q19. Can two modules have the same function name?
**Answer:**  
Yes, but must be called with their module name to avoid conflict.

## Q20. How do you share code across multiple projects using modules?
**Answer:**  
By creating reusable module files, packages, or publishing them as installable libraries (`pip` packages).

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
