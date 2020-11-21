
# ask for user input
user_input = input("Enter a character: ")

# validate the char type of the input
verdict = None
if user_input.islower():
    verdict = "a lower case letter"
elif user_input.isupper():
    verdict = "an upper case letter"
elif user_input.isdigit():
    verdict = "a digit"
elif not user_input.isalnum():
    verdict = "a non-alphanumeric character"

# render result
if verdict:
    print("{} is {}.".format(user_input, verdict))
