"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def factorial(n):
    if n==0:
        print("the factorial is:" )
        return 1
    else:    
        return n * factorial(n-1)
n = int(input("enter the number:"))
result=factorial(n)
print(result)















