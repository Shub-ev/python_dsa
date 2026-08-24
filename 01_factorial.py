# Find Factorial
# 
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# In the case of finding the factorial of a number, recursion can be used to break down the problem into smaller subproblems.
# The factorial of a number n (denoted as n!) is the product of all positive integers from 1 to n.
# The base case for the recursion is when n is 0 or 1, in which case the factorial is 1.
# For any other positive integer n, the factorial can be calculated as n multiplied by the factorial of (n-1).

num = int(input("Enter number (num >= 0): "))

def facto(num: int) -> int:
    if(num == 0 or num == 1):
        return 1
    return num * facto(num - 1)

print(facto(num))


## Using lambda expression
facto_lambda = lambda n: 1 if n <= 1 else n * facto_lambda(n - 1)
print(facto_lambda(num))