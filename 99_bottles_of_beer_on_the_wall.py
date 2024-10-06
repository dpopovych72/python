"""
## 3 bottles of beer on the wall
3 bottles of beer
Take one down, pass it around
2 bottles of beer on the wall!

2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottle of beer on the wall!

1 bottle of beer on the wall
1 bottle of beer
take it down, pass it around
No bottles of beer on the wall!

"""

bottles = 99

# Initially there are 99 bottles , the program will write the song until all of the bottles will be taken down
# which means , the song will be written 99 times 
# But due to the fact that the program has that "if " statement in it , the 99th time the song will be a bit different 
# if the "if" statement is written outside of a while loop , the "if" statement will be ignored 
while bottles > 0 :
    print(bottles," bottles of beer on the wall")
    print(bottles," bottles of beer")
    print("Take one down , pass it around")
    bottles -= 1 
    print(bottles," bottles of beer on the wall!")
    print("\n")
    if bottles == 1 :
        print(bottles," bottle of beer on the wall")
        print(bottles," bottle of beer")
        print("take it down , pass it around")
        bottles -= 1
        print("No bottles of beer on the wall !")
        