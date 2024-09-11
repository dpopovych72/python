"""Create a Python application that allows users to input
       their total budget and the amount spent in various categories. 
       The program will then calculate and display what percentage of 
       the total budget each category represents.
"""

housing = int(input("How much money did you spend on housing this month ?"))
utilities = int(input("How much did you spend on your utilities this month ?"))
groceries = int(input("How much did you spend on groceries this month ?"))
transportation = int(input("How much did you spend on transportation this month ?"))
health_care = int(input("How much have you spent on healthcare this month ?"))
personal_care = int(input("How much did you spend on personal care this month ?"))
clothing = int(input("How much did you spend on clothng this month ?"))
debt = int(input("What's your debt ?"))
budget = int(input("What's your budget this month?"))

housing_percentage = housing/budget*100
print(housing_percentage ,"%")
utilities_percentage = utilities/budget*100
print(utilities_percentage , "%")
groceries_percentage = groceries/budget*100
print(groceries_percentage , "%")
transportation_percentage = transportation/budget*100
health_care_percentage = health_care/budget*100
personal_care_percentage = personal_care/budget*100
clothing_percentage = clothing/budget*100
debt_percentage = debt/budget*100
