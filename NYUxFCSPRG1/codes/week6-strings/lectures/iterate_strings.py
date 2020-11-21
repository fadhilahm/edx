print("Please enter a line of text:")
user_input = input()

counter = 1
for char in user_input:
    if char == " ":
        counter += 1

print("You typed {} words".format(counter))