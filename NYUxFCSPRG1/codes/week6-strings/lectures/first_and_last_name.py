print("Please enter your name.\nSeparate first and last name by a space:")
user_input = input()

space_idx = user_input.find(" ")
first_name = user_input[:space_idx]
last_name = user_input[space_idx + 1:]
initials = "{}{}".format(first_name[0], last_name[0])

print(
"""First Name: {first_name}
Last Name: {last_name}
Initials: {initials}""".format(first_name=first_name, last_name=last_name, initials=initials)
)