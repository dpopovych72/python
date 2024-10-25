"""I had in total about of 4-5 attempts making this code already , and couldn't finished any of them because I made them too complicated and got lost.
This time I decided to make this program small and only made what was required .
"""
free_tickets=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Available tickets
bought_tickets =[] # Tickets that a user bought from the list free_tickets

def main():
    print("Don't enter 0 unless you want to quit ")
    how_many=int(input("How much tickets do you want? "))
    # Due to the fact that I have made 1 a starting point instead of zero , it skipped question number 0 completely 
    for i in range(1,how_many+1): # The optimal solution was to add 1 , because I moved starting point one space up 
        print("Those tickets are available :", free_tickets )
        ticket_num = int(input(f"What would be your ticket number {i} ? "))
        if ticket_num in free_tickets : # Checks if the ticket is available 
            # if it was in the free_tickets list , the user could take it and it would move the ticket from free_tickets list to bought_tickets list
            free_tickets.remove(ticket_num) 
            bought_tickets.append(ticket_num)
            print("You bought ticket :",ticket_num)
        elif ticket_num in bought_tickets: # if the ticket is not in the free_tickets list then it is not available for sale 
            while ticket_num in bought_tickets:
                print("This ticket is already taken ")
                ticket_num = int(input(f"Choose another ticket number {i} ? "))
                if ticket_num in free_tickets : # Checks if the ticket is available 
                    free_tickets.remove(ticket_num) 
            bought_tickets.append(ticket_num) # important to put it outside of the while loop , otherwise the program stucks in it
            print("You bought ticket :",ticket_num) # if it is being appended inside the while loop , it is suitable to repeat the while loop
        else :
            print("You wrote invalid ticket")
        if ticket_num == 0:
            print("stopping the program ")
            break # if the user enters 0 at any point , the program will stop 
    print("\nYou bought those tickets : ",bought_tickets)
    print("Goodbye")
        
        
    
main() #Forgot to call the function in a program before and thought that I did it wrong again 