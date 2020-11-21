def main():
    # ask for user input
    user_input = float(input("Please enter a temperature in Fahrenheit:\n"))
    tempc = conv_fc(user_input)
    print("{} Fahrenheit is {} Celsius".format(user_input, tempc))

def conv_fc(tempf):
    return "{:.3f}".format((tempf - 32) * 5 / 9)


main()