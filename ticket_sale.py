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
        take_it = input(f"Do you want to take it ? yes/no ")
        if take_it in ["yes","y"] :
            print(f"You took seat : {buy_seat}")
            free_seats.remove(buy_seat)
            print(f"Free seats left : ", free_seats)
        if take_it in["no","n"] :
            plan_to_pick = input("Do you plan to pick any seat ? (yes/no)" )
            while plan_to_pick in ["yes","y"]:
                pick_another_seat = int(input("Pick another seat"))
                print("You picked seat:" , pick_another_seat)
                want_another_seat = input("Do you want to pick another seat ?(yes/no)" )
            else :
                print("You are free to leave " )
    else :
        print("Seat is not available ")


main()
