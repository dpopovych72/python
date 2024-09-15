"""Create a Python application that allows users to input
       their total budget and the amount spent in various categories. 
       The program will then calculate and display what percentage of 
       the total budget each category represents.
"""
# Ask a user how much money he/she spent on each of the categories 
housing = int(input("How much money did you spend on housing this month ?"))
utilities = int(input("How much did you spend on your utilities this month ?"))
groceries = int(input("How much did you spend on groceries this month ?"))
transportation = int(input("How much did you spend on transportation this month ?"))
health_care = int(input("How much have you spent on healthcare this month ?"))
personal_care = int(input("How much did you spend on personal care this month ?"))
clothing = int(input("How much did you spend on clothng this month ?"))
debt = int(input("What's your debt this month ?"))
budget = int(input("What's your budget this month ?"))

""" Divide all the results each by budget
 and multiply by 100 to get the percentage 
 of budget spent on each of the categories """

housing_percentage = housing/budget*100
print(f"{housing_percentage:0.2f}%" )
utilities_percentage = utilities/budget*100
print(f"{utilities_percentage:0.2f}%" )
groceries_percentage = groceries/budget*100
print(f"{groceries_percentage:0.2f}%" )
transportation_percentage = transportation/budget*100
print(f"{transportation_percentage:0.2f}%" )
health_care_percentage = health_care/budget*100
print(f"{health_care_percentage:0.2f}%" )
personal_care_percentage = personal_care/budget*100
print(f"{personal_care_percentage:0.2f}%" )
clothing_percentage = clothing/budget*100
print(f"{clothing_percentage:0.2f}%" )
debt_percentage = debt/budget*100
print(f"{debt_percentage:0.2f}%" )

budget_spent = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
print(budget_spent)

budget_spent_percentage = housing_percentage + utilities_percentage + groceries_percentage + transportation_percentage + health_care_percentage + personal_care_percentage + clothing_percentage + debt_percentage
print(budget_spent_percentage)
