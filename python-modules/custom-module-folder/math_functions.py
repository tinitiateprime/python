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

def main():
    n = float(input("Enter a number: "))
    result = square_root(n)
    print("The square root of", n, "is", result)

if __name__ == "__main__":
    main()
