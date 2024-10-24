free_tickets=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
bought_tickets =[]

def main():
    how_many=int(input("How much tickets do you want? "))
    for i in range(how_many):
        ticket_num = int(input(f"What would be your {i} ticket? "))
        if ticket_num in free_tickets :
            free_tickets.remove(ticket_num)
            bought_tickets.append(ticket_num)
        else:
            print("This ticket is already taken ")
    print("You bought those tickets : ",bought_tickets)
