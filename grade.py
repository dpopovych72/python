"""## Accept a numeric grade from the user and display a letter grade.
 The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
Check to see if the number given is between 0 and 100.  
"""

grade = int(input("What is your grade ? "))
print("Your grade is " + str(grade) )

# The "if" statement checks if the grade is lower than 60 
# "if" statement showed that grade is bigger then minimum , "elif " statements check how big is it 
# When one of the statements end up true , the program tells user the letter grade 
if grade < 60 :
    print("Your letter grade is F") 
elif grade < 70 :
    print("Your letter grade is D") 
elif grade < 80 :
    print("Your letter grade is C")
elif grade < 90 :
    print("Your letter grade is B")
else :
    print("Your letter grade is A")
    