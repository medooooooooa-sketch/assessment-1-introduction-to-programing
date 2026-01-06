# Get user information
full_name = input("enter your name")
city = input("enter your city")
age = input("enter your age")

# Check if age contains only numbers
if age.isdigit():
    age = int(age)  # Convert age to integer
else:
    print("error")  # Invalid age input

