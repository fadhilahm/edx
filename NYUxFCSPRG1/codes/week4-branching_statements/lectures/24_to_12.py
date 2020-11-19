print("Please enter a time in a 24-hour format:")
hours24 = int(input("Hour: "))
minutes24 = int(input("Minute: "))

condition1 = hours24 // 12 == 0
condition2 = hours24 == 0 or hours24 == 12
time_cycle = "AM" if condition1 else "PM"
hours12 = 12 if condition2 else (hours24 if condition1 else hours24 % 12)

print("{hours24}:{minutes24} is {hours12}:{minutes24} {time_cycle}".format(
    hours24 = hours24,
    minutes24 = minutes24,
    hours12 = hours12,
    time_cycle = time_cycle
    ))