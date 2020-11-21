
# ask for user input
user_input = input("Enter an odd length string: ")

# determine the middle character using ((n - 1) / 2) as the index, where n is the length of the odd-length string
middle_index = int((len(user_input) - 1) / 2)
first_half = user_input[:middle_index]
second_half = user_input[middle_index + 1:]

# render result
print(
"""Middle character: {middle_character}
First Half: {first_half}
Second half: {second_half}""".format(middle_character=user_input[middle_index], first_half=first_half, second_half=second_half))
