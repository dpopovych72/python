"""Context: You are in charge of ticket sales for a special event.
 The venue has 20 seats, each uniquely numbered from 1 to 20.
  Your task is to create a system that tracks and updates the availability of seats as they are sold.
"""

free_seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Those seats are available :" , free_seats )

buy_seat = int(input("Please enter a seat that you would like to take " ))

def main():
    if buy_seat in free_seats :
        print(f"Seat {buy_seat} is available")
        want_to_take = bool(input("Enter 'True' if you want to take it , enter 'False' if not "))
        if want_to_take == True :
            print(f"You took seat : {buy_seat}")
            free_seats.remove(buy_seat)
            print(f"Free seats left : ", free_seats)
        if want_to_take == False :
            pick_another_seat = int(input("Pick another seat"))
            print("You picked seat:" , pick_another_seat)
    else :
        print("Seat is not available ")


main()