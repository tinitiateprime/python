# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using `if __name__ == "__main__"` statement
#  Author       : Team Tinitiate
# ==============================================================================



import math

def square_root(n):
    return math.sqrt(n)

def power(x, n):
    return x ** n

def main():
    n = float(input("Enter a number: "))
    x = float(input("Enter a power: "))
    result1 = square_root(n)
    result2 = power(x, n)
    print("The square root of", n, "is", result1)
    print(x, "raised to the power of", n, "is", result2)

if __name__ == "__main__":
    main()
