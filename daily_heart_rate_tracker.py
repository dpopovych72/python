"""Create a Python script to track heart rate readings 
       taken at various times throughout the day and 
       calculate the average heart rate.
"""

time_slots = ["Morning" , "Midday", "Afternoon" , "Evening" ]
heart_rate_list = []
total = 0
average = 0


for time_of_day in time_slots :
    heart_rate = int(input(f"Please write your heart rate(in BPM) for the {time_of_day}\n" ))
    heart_rate_list.append([time_of_day,heart_rate])
    total += int(heart_rate)
    average = total/4

# Display collected data from the user , and show the average heart rate
print("\n")
print(heart_rate_list)
print(f"Your average heart rate is {average} BPM")


       