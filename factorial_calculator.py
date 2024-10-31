"""A factorial is a mathematical operation applied to a non-negative integer n,
denoted by n!,
that results in the product of all positive integers less than or equal to n. 
For example, the factorial of 5 (5!) is calculated as 5 x 4 x 3 x 2 x 1,
which equals 120.
"""

def factorial(n):
    if n == 1|0 : # The base case (floor)
        return n
    elif n>1 : # repeats until reaches the base case 
        return n * factorial(n-1)
        
def main():
    # collect the data from the user 
    number = int(input("Please enter a non negative integer : "))
    result = factorial(number)
    
    print(f"The factorial of {number} is {result}")
        
        
main()
