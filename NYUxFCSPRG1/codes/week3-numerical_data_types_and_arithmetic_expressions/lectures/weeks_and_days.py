print("Please enter the number of days you traveled: ")
days = int(input())
weeks_only = days // 7
days_only = days % 7
print("{} days are {} weeks and {} days".format(days, weeks_only, days_only))