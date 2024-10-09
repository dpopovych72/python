

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
                print("You did ",step,"steps on ",day)
                
    print("\nTotal steps : ",total)
    print(f"Average steps : {average:0.0f}")

# Call the function "main"
main()
