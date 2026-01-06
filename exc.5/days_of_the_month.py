# Dictionary that stores number of days for each month
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Get month number from the user
month = int(input("Enter month number (1-12): "))

# Check the month number and print number of days
if month == 1:
    print("31 Days")
elif month == 2:
    print("28 Days")
elif month == 3:
    print("31 Days")
elif month == 4:
    print("30 Days")
elif month == 5:
    print("31 Days")
elif month == 6:
    print("30 Days")
elif month == 7:
    print("31 Days")
elif month == 8:
    print("31 Days")
elif month == 9:
    print("30 Days")
elif month == 10:
    print("31 Days")
elif month == 11:
    print("30 Days")
elif month == 12:
    print("31 Days")
else:
    print("Incorrect input")
