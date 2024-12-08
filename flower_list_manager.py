"""
Create a Python program to manage a list of flowers.
This includes sorting the list, searching for specific flowers,
and handling exceptions using try and except statements.
"""
# if something goes wrong , the answers for exceptions will be raised 
try :
    def main():
        flower_list = []
        while True :
            flower = input("Write down a flower : ")
            if flower == "done":
                print("You are finished adding flowers :")
                break
            flower_list.append(flower)
            print(flower_list)
            flower_list.sort()
            print(flower_list)
        flower_list.sort()
        num = 0
      # prints the table with all flowers and numbers that stand for their place 
        for flower in flower_list:
            num+=1
            print(flower,num)
        want = input("Do you want to take any flower? y/n : ")
        if want == "y":
            number = int(input("Write a number"))
            print("You picked :",flower_list[number-1])
            flower_list.remove(flower_list[number-1])
        print("Here is what is left in the list of flowers : ",flower_list)
except ValueError :
    print("Be carefull with your values")
except IndexError :
    print("This one might be on me ")
except :
    print("I don't know what's gone wrong , don't ask me")

main()
