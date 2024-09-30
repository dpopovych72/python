def magic_py():
    # Functions are like magic 
    # Call them and something happens 
    print("It's Magic !!!")

# magic_py()

def months(years):
# calculate how many months old are you 
    months = 12 * years 
    print(f"You are {months}months old .")


years = int(input("How old are you ?"))
months(years)