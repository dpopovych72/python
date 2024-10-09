"""1)Create a List: Start by creating a list named days that includes all seven days of the week.
2)Initialize an Empty List: Create an empty list called steps. This will store the number of steps taken each day.
3)User Input: Using a loop, ask the user to enter the number of steps they took for each day, 
based on your days list. For example, "How many steps did you take on Monday?"
4)Store Steps: Append the user's input (number of steps) to the steps list for each day.
5)Display Daily Steps: Show the user the steps recorded for each day.
6)Total Steps: Calculate and display the total number of steps taken in the week.
7)Average Steps: Create a variable named average to calculate the average steps taken. 
Use the formula: average = round(total / len(steps)). Display the average steps.
"""

def main():
    # Declare all lists and integers 
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    steps = []
    total = 0
    average = 0

    for i in days :
        # Get all of data for steps from the user , convert it to " int " so you could use it as numbers
        steps.append(int(input("How many steps did you do on "+ str(i) + "? ")))
        # When the program stops to ask all of the questions , it will then provide user all of the answers
        if len(steps)==7:  
            for i in range(len(steps)):
                day = days[i]
                step = steps[i]
                total += step
                average = total / len(steps)
                # It will be printed same ammount of times as items in list "steps" 
                print("You did ",step,"steps on ",day) 
                
                
    print("\nTotal steps : ",total)
    print(f"Average steps : {average:0.0f}")

# Call the function "main"
main()
