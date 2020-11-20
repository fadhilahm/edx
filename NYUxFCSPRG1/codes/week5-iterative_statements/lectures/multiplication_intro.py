input_int = int(input("Please enter a positive integer:"))

# line = ""
# for i in range(1, input_int + 1):
#     line += "{}".format((3 * i)) + " "
# print(line)

for i in range(1, input_int + 1):
    print(i * 3, end=" ")
print()