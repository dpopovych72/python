free_tickets=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Available tickets
bought_tickets =[] # Tickets that a user bought from the list free_tickets

def main():
    how_many=int(input("How much tickets do you want? "))
    # Due to the fact that I have made 1 a starting point instead of zero , it skipped question number 0 completely 
    for i in range(1,how_many+1): # The optimal solution was to add 1 , because I moved starting point one space up 
        ticket_num = int(input(f"What would be your ticket number {i} ? "))
        if ticket_num in free_tickets : # Checks if the ticket is available 
            # if it was in the free_tickets list , the user could take it and it would move the ticket from free_tickets list to bought_tickets list
            free_tickets.remove(ticket_num) 
            bought_tickets.append(ticket_num)
        else: # if the ticket is not in the free_tickets list then it is not available for sale 
            print("This ticket is already taken ")
    print("You bought those tickets : ",bought_tickets)
    
main() #Forgot to call the function in a program before and thought that I did it wrong again 
