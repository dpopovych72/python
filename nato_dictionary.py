"""
    Your mission is to create a Python program that uses a dictionary 
    to translate letters into the NATO Phonetic Alphabet.
    This program will ask users for a word and then spell it out using the NATO codes.
"""

def main():
    nato_dictionary = {
                    "A":"Alpha",
                    "B":"Bravo",
                    "C":"Charlie",
                    "D":"Delta",
                    "E":"Echo",
                    "F":"Foxtrot",
                    "G":"Golf",
                    "H":"Hotel",
                    "I":"India",
                    "J":"Juliette",
                    "K":"Killo",
                    "L":"Lima",
                    "M":"Mike",
                    "N":"November",
                    "O":"Oscar",
                    "P":"Papa",
                    "Q":"Quebec",
                    "R":"Romeo",
                    "S":"Sierra",
                    "T":"Tango",
                    "U":"Uniform",
                    "V":"Victor",
                    "W":"Whiskey",
                    "X":"X-Ray",
                    "Y":"Yankee",
                    "Z":"Zulu"
                    }
                    
    word = input("Please enter a word : ")
    word = word.upper()
    
    # print(word)
    print(f"NATO phonetic term of {word} is : ")
    for i in word : # itterates through every letter in input word 
    # Checks if any of the letter is seen as key in nato_dictionary
        if i in nato_dictionary: 
            print(nato_dictionary[i])# prints it's value
            
main()

