"""
This is a string practice 
"""

def main():
    # Example string
    example_string = "Hello, Python programmers!"
    # TODO: Iterate through the string and print each character
    
    print("Iterating through the string:")
    print()
    for char in example_string:
        print(char)
    # TODO: Find and print the character with the minimum ASCII value in the string
        
    print("\nCharacter with the minimum ASCII value:")
    if ord(min(example_string))== 32 :
        print("'Space'")
    else :
        print(f"'{min(example_string)}'")
    # TODO: Find and print the character with the maximum ASCII value in the string
    
    print("\nCharacter with the maximum ASCII value:")
    if ord(max(example_string))== 32 :
        print("'Space'")
    else :
        print(f"'{max(example_string)}'")
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    
    print("\nIndex of 'o':")
    print(f"'{example_string.index("o")}'")
    # TODO: Convert the string into a list of characters and print the list
    
    print("\nConverting string to a list of characters:")
    print(f"{list(example_string)}")
    # TODO: Count and print the number of occurrences of 'o' in the string
    
    print("\nCount of 'o' in the string:")
    print(f"'{example_string.count("o")}'")
  
main()
