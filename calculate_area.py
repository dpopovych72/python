"""This program will calculate an area of a square and a circle 
"""
print("Please povide an answer in centimeters for the following questions\n ")
# This function will calculate an area of a square 
def square(side):
    area = side*side
    print(f"An area of your square is {area:0.03f} cm ")

side = float(input("What is the length of one side of your square in cm ?\n"))
square(side)



# This function will calculate an area of a circle 
def circle(radius):
    area = 3.14*radius*radius
    print(f"An area of your circle is {area:0.03f} cm ")

radius = float(input("What is the radius of your circle in cm ?\n" ))
circle(radius)