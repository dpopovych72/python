"""Develop a Python-based Madlib based on a song of your choice.
The program should collect at least 8 different pieces
of information from the user and incorporate them into the song using named arguments.
The goal is to practice using functions, user input, and string manipulation in Python.
"""
def little_star(size,world,narrator,child_1,child_2,star,emotion,friends):

    print(f"[Scene opens with a soft, starry backdrop. The {narrator} stands to the side.]" )
    print(f"\n{narrator}:" )
    print(f"\n{emotion}  Welcome, everyone! \nTonight, we’re going on a magical journey to meet a special {star}!\n Let’s start by singing our favorite song together!" )
    print(f"\n[All characters gather and hold hands.]")
    print("\nAll Together:" )
    print(f"Twinkle, twinkle, {size} {star},\nHow I wonder what you are!\nUp above the {world} so high,\nLike a diamond in the sky." )
    print(f"\n[{child_1} looks up, pretending to see the {star}.]" )
    print(f"\n{child_1}:" )
    print(f"\nWow! Look at that bright {star}! I wonder where it lives!" )
    print(f"\n[{child_2} jumps in {emotion}.]" )
    print(f"\n{child_2}:" )
    print(f"\nLet’s call it down to play with us!" )
    print(f"\n[They both shout together.]" )
    print(f"\n{child_1}&{child_2} :" )
    print("\nStar, come down and play with us!" )
    print(f"\n[{star} enters, twinkling and sparkling.]" )
    print(f"\n{star}:" )
    print(f"\n{emotion}Hello, little {friends}! I heard your song! What do you want to do?" )
    print(f"\n{child_1}:" )
    print(f"\nWe want to dance with you!" )
    print(f"\n{child_2}:" )
    print(f"\nYes! Let’s have a twinkling dance party!" )
    print(f"\n[Music starts playing, and everyone dances around.]\n[After a fun dance break, everyone gathers back in a circle.]" )
    print(f"\n{child_1} :" )
    print(f"\n{star}, how do you shine so bright?" )
    print(f"\n{star} :" )
    print(f"\n{emotion} I twinkle with joy and share light! Whenever you feel happy, just remember to shine bright too!" )
    print(f"\n{child_2} :" )
    print("\nLet’s sing our song one more time!" )
    print("\nAll Together:" ) 
    print(f"Twinkle, twinkle, {size} {star},\nHow I wonder what you are!\nUp above the {world} so high,\nLike a diamond in the sky." )
    print(f"\n[{star} waves goodbye as it twinkles away.]" )
    print(f"\n{star}:" )
    print(f"\nGoodbye, my {friends}! Keep shining bright!" )
    print(f"\n{narrator} :" )
    print(f"\nAnd so, our {friends} learned that just like the {star}, they can shine bright in everything they do. Thank you for joining us on this twinkling adventure!")
    print("\n[All characters wave and smile as the scene ends.]")

# Ask a user to put in the answers , those answers will be used as parameters in the function 
object_size = input("Write a size of an object ")
world_name = input("Write a place " )
narrator_name = input("Who is the Narrator? " )
child_name1 = input("Write a name ")
child_name2 = input("Write another name ")
star_name = input("Write a name of somebody you love ")
feelings = input("How do you feel right now ? ")
organization = input("Write a name of an organization ")

# Make every answer a parameter in the function and call the function in the program
little_star(size=object_size,world=world_name,narrator=narrator_name,child_1=child_name1,child_2=child_name2
,star=star_name,emotion=feelings,friends=organization)










