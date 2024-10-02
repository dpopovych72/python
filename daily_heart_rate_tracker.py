"""Create a Python script to track heart rate readings 
       taken at various times throughout the day and 
       calculate the average heart rate.
"""
# All lists and variables are declared 
time_slots = ["Morning" , "Midday", "Afternoon" , "Evening" ]
heart_rate_list = []
total = 0
average = 0

# 1) For each time of day , the user will be asked to provide the heart rate 
# 2) The heart rate value and time of day for which it was asked , will be stored in a heart rate list
# 3) The total will receive all of the data provided by the user 
# 4) Average is being calculated by dividing total by 4 
for time_of_day in time_slots :
    heart_rate = int(input(f"Please write your heart rate(in BPM) for the {time_of_day}\n" ))
    heart_rate_list.append([time_of_day,heart_rate])
    total += int(heart_rate)
    average = total/4

# Display collected data from the user , and show the average heart rate
print("\n")
print(heart_rate_list)
print(f"Your average heart rate is {average} BPM")


       