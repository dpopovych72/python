"""   In this assignment, you will write a Python program to identify and print all the numbers divisible by 7
      that fall between 1 and 300. This task will help you practice using loops and conditional statements in Python.
"""
# "break" stops the program when some condition is met 
# "continue" ignores the item that have met the condition , but the program does not stop 
"""for i in range(1,7,3):
    print(i)
"""
divisible_by_7 = [] # This list will store all of the numbers divisible by 7 
count = 0

# This "for" loop will run 299 times 
for i in range(1,300):
    if i % 7 == 0 : # if there is no left overs after the modulo , then the number is divisible by 7
        print(i)
        divisible_by_7.append(i) # if the number is divisible by 7 it will be added to the list 
        count+=1

print("\nAmmount of numbers : "+ str(count)) # Ammount of numbers that are divisible by 7 , from 1 to 300
