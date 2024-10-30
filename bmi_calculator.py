# Me :can a function return a string
"""
ChatGPT :

Yes, a function can definitely return a string in most programming languages.
The syntax may vary depending on the language, but the basic idea is similar. 

For example, in Python:

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

In this example, 
the `greet` function takes a name as an argument
and returns a greeting string. If you have a specific language in mind,
let me know, and I can provide a more tailored example!
"""

# Ask user all of the needed data 
weight = float(input("Please enter your weight (pounds) : "))
height = float(input("Please enter your height (inches) : "))

# Convert into europian measurements 
weight*=0.453592
height*=0.0254

def main(weight_kg, height_cm):
    # define variables that the function will return 
    under_weight = "You are underweight "
    normal_weight = "You are in the normal weight category "
    over_weight =  "You are overweight "
    obese =  "You are obese "
    bmi = weight_kg / height_cm ** 2
    weight_category = ""
    # write if statements for every case scenario 
    # f"{:.4f}" = stands for the ammount of all numbers  in float variable . 
    # f"{:.2f}" = used this , and the function returned me very low numbers (2e+01)
    if bmi<18.5 :
        print(f"Your BMI is : {bmi:.4}")
        weight_category = under_weight
    elif bmi >= 18.5 and bmi <24.9 :
        print(f"Your BMI is : {bmi:.4}")
        weight_category = normal_weight
    elif bmi >= 25 and bmi <29.9:
        print(f"Your BMI is : {bmi:.4}")
        weight_category = over_weight
    elif bmi >= 30 :
        print(f"Your BMI is : {bmi:.4}")
        weight_category = obese
    
    return weight_category
main(weight,height) # Use users' data in place of parameters 
