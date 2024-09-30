"""Create a Python script to track heart rate readings 
       taken at various times throughout the day and 
       calculate the average heart rate.
"""
time_slots = ["Morning" , "Midday", "Afternoon" , "Evening" ]
heart_rate_list = []


for time_of_day in time_slots :
    heart_rate = int(input(f"Please write your heart rate(in BPM) for the {time_of_day}\n" ))
    heart_rate_list.append([time_of_day,heart_rate])
    print(f"You had a heart rate of {heart_rate} BPM for the {time_of_day}\n")

    
print(heart_rate_list)