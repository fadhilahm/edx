n = int(input("Please enter the number of students in the class: "))
print("Please enter the students's grades (in separate lines):")

total = 0
for i in range(n):
    total += int(input(""))
total /= n

print("The class average is {:.2f}".format(total))