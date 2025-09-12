![Python Tinitiate Image](../python_tinitiate.png)

# Python Interview QnA
&copy; TINITIATE.COM

##### [Back To Contents](./README.md)

# OOP vs Functional Programming

## Q1. What is the difference between OOP and Functional Programming?
**Answer:**  
- **OOP** organizes code into objects (data + behavior).  
- **Functional** organizes code into pure functions, avoiding shared state and side effects.

## Q2. What is the main principle of OOP?
**Answer:**  
Encapsulation, inheritance, and polymorphism—objects model real-world entities.

## Q3. What is the main principle of Functional Programming (FP)?
**Answer:**  
Immutability, pure functions, and declarative style.

## Q4. Can Python support both OOP and FP?
**Answer:**  
Yes, Python is multi-paradigm and supports both approaches.

## Q5. Give an example of functional style code.
**Answer:**  
```python
nums = [1,2,3,4]
squares = list(map(lambda x: x*x, nums))
```

## Q6. Give an example of OOP style code.
**Answer:**  
```python
class Square:
    def __init__(self, n): self.n = n
    def calc(self): return self.n*self.n
print(Square(4).calc())
```

## Q7. What are pros of OOP?
**Answer:**  
- Encapsulation  
- Reusability  
- Easier modeling of real-world problems  
- Extensibility

## Q8. What are cons of OOP?
**Answer:**  
- Can lead to large, complex hierarchies  
- Requires more boilerplate  
- Slower for small operations

## Q9. What are pros of FP?
**Answer:**  
- Easier debugging due to pure functions  
- Parallelization is easier (no shared state)  
- Concise code

## Q10. What are cons of FP?
**Answer:**  
- Steeper learning curve  
- May be less intuitive for stateful problems  
- Can be inefficient for certain operations

## Q11. What is immutability in FP?
**Answer:**  
Data cannot be changed after creation, ensuring predictable results.

## Q12. What is a pure function?
**Answer:**  
A function that always gives the same output for the same input and has no side effects.  
```python
def add(a,b): return a+b
```

## Q13. What is side effect in programming?
**Answer:**  
Any modification outside the function’s scope (e.g., updating global variable, writing to file).

## Q14. How does OOP handle state vs FP?
**Answer:**  
- OOP → stores state inside objects.  
- FP → avoids state, prefers immutable data and stateless functions.

## Q15. How do you combine OOP and FP in Python?
**Answer:**  
By writing classes with methods, and using functional tools like `map`, `filter`, `reduce`.

## Q16. What Python modules support functional programming?
**Answer:**  
`functools`, `itertools`, `operator`.

## Q17. What is first-class function in FP?
**Answer:**  
Functions can be stored in variables, passed as arguments, and returned.

## Q18. What is higher-order function?
**Answer:**  
A function that takes another function as an argument or returns one.

## Q19. Which paradigm is better for mathematical computations?
**Answer:**  
Functional programming is often better due to immutability and pure functions.

## Q20. Which paradigm is better for real-world modeling like games or applications?
**Answer:**  
Object-Oriented Programming, because it models entities with state and behavior.

##### [Back To Contents](./README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
