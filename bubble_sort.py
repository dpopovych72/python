"""Your program should prompt the user to enter five names.
    Use a loop to accept each name and append it to a list.
    Implement the Bubble Sort algorithm to sort the list of names in ascending order.
    Print the sorted list.
    After sorting, use a Python list method to reverse the order of the list.
    Print the final reversed list to the console.
"""



def main():
    names = [] # Stores names
    swapped = True

    for i in range(5):# User will be asked to add name 5 times
        new_name = input("Please write a name ")
        names.append(new_name)

    print(names) # not sorted 

    while swapped : # while swapped is True set it to False , otherwise the program will ignore the for loop
        swapped= False
        for i in range (len(names)-1):
            if names[i]>names[i+1]:
                names[i],names[i+1] = names[i+1],names[i]
                swapped = True # set it back to True everytime the for loop runs , otherwise the for loop works only once
        

    print(names) # sorted
    names.reverse()# the program does not see the list if I reverse it inside of the print function
    print(names) # reversed

main()

