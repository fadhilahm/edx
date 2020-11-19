print("Please enter a time in a 24-hour format: ")
hours24 = int(input("Hour: "))
minutes24 = int(input("Minute: "))

minutes12 = minutes24

hours12 = None
period = None

# if hours24 == 0:
#     period = "AM"
#     hours12 = 12
# elif hours24 == 12:
#     period = "PM"
#     hours12 = hours24
# elif 0 < hours24 < 12:
#     period = "AM"
#     hours12 = hours24
# elif 12 < hours24 < 24:
#     period = "PM"
#     hours12 = hours24 % 12

if hours24 // 12 == 0:
    period = "AM"
    if hours24 == 0:
        hours12 = 12
    else:
        hours12 = hours24
else:
    period = "PM"
    if hours24 == 12:
        hours12 = hours24
    else:
        hours12 = hours24 % 12

print("{hours24}:{minutes24} is {hours12}:{minutes12} {period}".format(
    hours24 = hours24,
    minutes24 = minutes24,
    hours12 = hours12,
    minutes12 = minutes12,
    period = period
    ))