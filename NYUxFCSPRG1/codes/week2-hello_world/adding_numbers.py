print("Please enter two numbers in two separate lines:")
arr, total = [], 0
for _ in range(2):
    temp = input()
    arr.append(temp)
    total += int(temp)
print("{} + {} = {}".format(arr[0], arr[1], total))