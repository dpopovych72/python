"""1) Create a tuple named programming_classes with these classes: 
'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 
'Data Structures in Python', 'Web Design Fundamentals'.
2) Write a program that uses a for loop to print each class in the tuple.
3) Use the len function to print how many classes are in the tuple.
4) Make sure to use a main function for this program.
"""
# define a function main
def main():
    # tuple being created 
    programming_classes = ('Intro to Python','Adevanced Python',
    'Database Essentials','Web Development Basics','Data Structures in Python','Web Design Fundamentals')
# print the message and the length of the tuple "programming_classes"
    print("\nThe tuple has ", len(programming_classes),"classes\n") 

    for i in programming_classes :
        print(i) # Print everything from the tuple "programming_classes"
   
# Function main being called in the program 
main()

