
# ask for input from the user
# weight_pounds = float(input("Please  enter weight  in  pounds: "))
# height_inches = float(input("Please  enter height  in  inches: "))

weight_pounds = float(input())
height_inches = float(input())

# convert to metric values
weight_metric = 0.453592 * weight_pounds
height_metric = 0.0254 * height_inches

# calculate bmi
bmi = "{:.10f}".format(weight_metric / height_metric ** 2)

# render output
print("BMI is: {}".format(bmi))
