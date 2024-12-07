"""
This main function receives the character and returns the unicode code point for it ,
which should be the number 
"""

def main():
    user_input = input("Enter a character : ")
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    ascii_value = ord(user_input)   
    # ord() gives the unicode code point of the single character
    # chr() gives character for a unicode code point 
    print(f"The ASCII value of {user_input} is {ascii_value}")
    
    
    
    
main()   
