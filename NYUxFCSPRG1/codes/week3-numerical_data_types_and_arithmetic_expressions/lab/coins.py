# ask for input from user
print("Please enter the amount of money to convert:")
dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

# calculate total
total = dollars * 100 + cents

# define list used to iterate coins
# zero index => name of the coin
# first index => value of the coin
# second index => the amount of coins
coins = [
    ["quarters", 25, 0],
    ["dimes", 10, 0],
    ["nickels", 5, 0],
    ["pennies", 1, 0]
]

# define pointer used to mark which coin will be used, started with 0 (the biggest value)
index = 0
# use a while-loop to iterate until total has been exhausted
while total > 0:
    if total - coins[index][1] >= 0:
        total -= coins[index][1]
        coins[index][2] += 1
    else:
        index += 1

# render output statement
print("The coins are {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies".format(
    quarters = coins[0][2],
    dimes = coins[1][2],
    nickels = coins[2][2],
    pennies = coins[3][2]
))
