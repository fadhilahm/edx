user_input = int(input("Please enter an integer value: "))

verdict = "even" if user_input % 2 == 0 else "odd"

print("{} is {}".format(user_input, verdict))