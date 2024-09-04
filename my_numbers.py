# Working with and formatting numbers 
# Variables 

hamburger = 3.99
cheese_burger = 4.99
soda = 0.99
tax = 0.02

total = (hamburger * 2 ) + cheese_burger + (2*soda)
taxed = total * tax 
grand_total = total + taxed 

print ("Your ordered :\n")
print(f"Two hamburgers at {hamburger} each.")
print(f"One Cheese burger at {cheese_burger} each")
print(f"Two sodas at {soda} each")
print(f"For a total of : ${total:0.02f}")
print(f"Taxxed for : ${taxed:0.02f}")
print(f"Your Grand Total is : ${grand_total:0.02f}")
