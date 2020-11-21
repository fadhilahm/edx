print("Please enter 3 words:")
strings = []
for i in range(3):
    # print("#{}: ".format(i + 1), end="")
    # strings.append(input(""))
    strings.append(input("#{}: ".format(i + 1)))

min = None
for string in strings:
    if min == None or string < min:
        min = string
print(min)