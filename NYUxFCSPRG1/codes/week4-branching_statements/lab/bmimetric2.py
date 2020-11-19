# ask for input from the user
# weight_input = float(input("Please  enter weight in kilograms: "))
# height_input = float(input("Please  enter height in meters: "))
weight_input = float(input())
height_input = float(input())


# calculate bmi
bmi = float("{:.2f}".format(weight_input / height_input ** 2))

# determine weight category
category = None
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

# render result output
print("BMI is: {}, Status is {}".format(bmi, category))
