table = [[1,2,3],[4,5,6],[7,8,9]]

guess = ""
print(table[1][1])


def board():
    for row in table :
        print(row)

def win():
    word = "x"
    if table[1].count(word.upper()) == 3 :
        print("You win ")

def user_guess():
    for i in range(table.length()):
        guess = int(input("Put a number "))
        if guess in table[1] :
            guess.insert(table[1].index(guess))
            print(table[1])
