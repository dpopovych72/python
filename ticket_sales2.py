available_seats = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in available_seats :
    print(i)

select_seat = input("Pick a seat")

if select_seat in available_seats :
    available_seats.remove(select_seat)
    print(available_seats)
