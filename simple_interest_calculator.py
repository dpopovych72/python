"""Objective: Write a Python function named calculate_interest
 that computes and returns the simple interest based on given parameters.
"""

# Simple Interest = (Principal Amount × Rate of Interest × Time) / 100
def calculate_interest(principal , rate , time):
    simple_interest = (principal*rate*time)/100
    return simple_interest

# Ask user for numbers 
principal_ammount= float(input("Write a principal ammount ($): "))
rate_of_interest = float(input("Write an interest rate (%) : "))
time_ammount = int(input("Write time (years) : "))

# Use the provided values for parameters , and call the function 
result = (calculate_interest(principal_ammount,rate_of_interest,time_ammount))
print(f"The simple interest for a principal ammount of ${principal_ammount:0.02f}\n \
at a rate of interest {rate_of_interest:0.02f}% \
over a period of {time_ammount} years is $",result)
