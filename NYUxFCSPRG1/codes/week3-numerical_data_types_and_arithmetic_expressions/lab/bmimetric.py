# ask for input from user
# print("Please  enter weight  in  kilograms: ")
weight = float(input())
# print("Please  enter height  in  meters: ")
height = float(input())

# calculate bmi
bmi = float("{:.10f}".format(weight / height ** 2))

# render result output
print("BMI is: {}".format(bmi))