"""Objective: Write a Python function named calculate_interest
 that computes and returns the simple interest based on given parameters.
"""

# Simple Interest = (Principal Amount × Rate of Interest × Time) / 100
def calculate_interest(principal , rate , time):
    simple_interest = (principal*rate*time)/100
    print(simple_interest)

# Ask user for numbers 
principal_ammount= float(input("Write a principal ammount"))
rate_of_interest = float(input("Write an interest rate in percents"))
time_ammount = int(input("Write time in years"))

# Use the provided values for parameters , and call the function 
calculate_interest(principal=principal_ammount,rate=rate_of_interest,time=time_ammount)
