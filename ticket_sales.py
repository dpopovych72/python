available_seats = ["1","2","3","4","5"]
print(available_seats)
sold_seat = []

buy_seat = str(input("Please enter a seat that you would like to take\n"))

if buy_seat in available_seats :
    available_seats.remove(buy_seat)
    sold_seat.append(buy_seat)
    print(buy_seat)
    print(available_seats)
    print(sold_seat)
#while buy_seat != "done" :
   # for item in available_seats:
        # print(item)

#for i in available_seats :
 #   available_seats.remove(i)
  #  sold_seat.append(i)
   # print("You took seat ",[buy_seat])
    #print(available_seats)
    #print(sold_seat)