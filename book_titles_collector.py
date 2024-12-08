"""
In this assignment,
you will create a Python program that collects book titles from a user.
Your program should use a while loop 
to prompt the user to enter a total of 10 book titles.
"""



def main():
    book_list = []
    count=0
    # runs until all 10 books are written
    while count != 10 :
        book = input("Please enter a book name : ")
        book_list.append(book)
        print(book_list)
        count+=1
    # creates a new list entirely sorted in alphabetical order 
    new_list = sorted(book_list)
    print("This is your list in alphabetical order : ",new_list)
    print("Those are all of the books in your list writen as titles : ")
    # all books in a sorted list written one by one 
    for book in new_list:
        print(book.title())
        
        
main()
