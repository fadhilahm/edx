print("Enter grades in separate lines.\nTo end input type 'done':")

user_input, sum, count = None, 0, 0

while True:
    user_input = input()
    if user_input != "done":
        sum += int(user_input)
        count += 1
    else:
        break

avg = sum / count
print("The class average is {:.2f}".format(avg))
