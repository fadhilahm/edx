print("Please enter the number of coins:")
quarters = int(input("# of quarters: ")) # 25 cents
dimes = int(input("# of dimes: ")) # 10 cents
nickels = int(input("# of nickels: ")) # 5 cents
pennies = int(input("# of pennies: ")) # 1 cent

# calculate the total amount
total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
dollars = total // 100
cents = total % 100

# render output
print("The total is {} dollars and {} cents".format(dollars, cents))
