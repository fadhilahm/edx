user_input = int(input("Please enter an integer: "))
abs_value = user_input if user_input >= 0 else - user_input
print("|", user_input, "| = ", abs_value, sep="")