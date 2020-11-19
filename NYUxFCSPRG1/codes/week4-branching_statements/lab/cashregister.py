
# ask for user input
items = []
items.append(float(input("Enter price of the first item: ")))
items.append(float(input("Enter price of the second item: ")))
has_club_card = input("Does customer have a club card? (Y/N): ").lower()
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

# determine which item will be discounted, the item in the zero index will be the one to be discounted
base_price = items[0] + items[1]
if items[0] > items[1]:
    temp = items[1]
    items[1] = items[0]
    items[0] = temp
items[0] /= 2

# calculate price
discounted_price = items[0] + items[1] if has_club_card != "y" else (items[0] + items[1]) * 0.9
total_price = discounted_price * (100 + tax_rate) / 100

# render output
print("Base price = {:.2f}".format(base_price))
print("Price after discounts = {:.2f}".format(discounted_price))
print("Total price = {:.2f}".format(total_price))
