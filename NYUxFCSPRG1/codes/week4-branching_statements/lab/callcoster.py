
# ask for input from user
day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))

# control flow based on day of the week
if day == "Sat" or day == "Sun":
    price_per_minute = 0.15
else:
    # calculate the time when the call started
    if 800 <= time <= 1800:
        price_per_minute = 0.4
    else:
        price_per_minute = 0.25

# calculate price and render output
price_total = price_per_minute * duration
print("This call will cost ${:.2f}".format(price_total))
