"""Write a Python program that uses if else statements and:

Ask the user for their age.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount (65).
Print all the results on the screen.
"""
# Declare and Ask all of the required age info
name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
drive_age = int(input("How old do you need to be to drive in your state ? "))
vote_age = 18
alcohol_age = int(input("How old do you need to be to buy alcohol in your state ? "))
senior_discount = 65


print("\n")
if age >= drive_age :
    print("Good news , you are eligible to drive !!!")
else :
    print("Can't drive yet ")
if age >= vote_age :
    print("That is great , you can vote !!!")
else : 
    print("Sorry bud , it seems like you can't vote yet ")
if age >= alcohol_age :
    print("It seems like you can buy alcohol , congrats !!!")
else : 
    print("Your are too young to drink , bring some adult if you are fearless ")
if age >= senior_discount :
    print("You can have a discount on anything you buy from us ")
else : 
    print("Great news , you are still not eligible for senior discount")
    