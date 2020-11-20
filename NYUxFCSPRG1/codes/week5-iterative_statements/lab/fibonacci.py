
# ask for user input
user_input = int(input("Please enter a positive integer greater than 1: "))

# initialize value used for fibonacci
prev_value1 = 0
prev_value2 = 1
curr_value = None

# it will always print out the first number
print(1)

# initialize current value
for _ in range(user_input - 1):
    curr_value = prev_value1 + prev_value2
    prev_value1 = prev_value2
    prev_value2 = curr_value
    print(curr_value)