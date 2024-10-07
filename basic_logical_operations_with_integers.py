"""In this exercise, you will practice using logical operators 
    (and, or, not) in Python. Your task is to create a program that 
    prompts the user for two integer inputs and then demonstrates the use of these operators.
"""

def main():
    number1 = int(input("Please put in a distinct integer : "))
    number2 = int(input("Please put in another distinct integer : "))
    both_greater_than_0 = False
    both_greater_than_100 = False
    either_even = False
    either_less_than_100 = False
    num1_is_equal_to_num2 = False
    num1_is_zero = False

    if number1>0 and number2>0 :
        both_greater_than_0 = True
        print("Both numbers are greater than 0 :",both_greater_than_0)
    else :
        print("Both numbers are greater than 0 :",both_greater_than_0)
    if number1>100 and number2>100 :
        both_greater_than_100 = True
        print("Both numbers are greater than 100 :",both_greater_than_100)
    else :
        print("Both numbers are greater than 100 :",both_greater_than_100)
    if number1 %2 == 0 or number2 %2 == 0 :
        either_even = True
        print("Either number is even ? ", either_even)
    else :
        print("Either number is even ? ",either_even)
    if number1 < 100 or number2 < 100 :
        either_less_than_100 = True
        print("Either number is less than 100 ? ",either_less_than_100)
    else :
        print("Either number is less than 100 ? ",either_less_than_100)
    if not number1 == number2 :
        print("Number 1 is equal to Number 2 :", num1_is_equal_to_num2)
    else :
        num1_is_equal_to_num2 = True 
        print("Number 1 is equal to Number 2 :", num1_is_equal_to_num2)
    if not number1 == 0 :
        print("Number 1 is equal to 0 : ", num1_is_zero)
    else :
        num_is_zero = True
        print("Number 1 is equal to 0 : ", num1_is_zero)





main()
        



