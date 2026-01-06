
# Set the correct password
password = '12345'

# Number of allowed attempts
opportunities = 5

# Loop runs while attempts are available
while opportunities > 0:
    user_input = input("Enter your password: ")

    # Check if password is correct
    if user_input == password:
        print("Access granted.")
        break  # Stop loop on success
    else:
        opportunities -= 1  # Decrease attempts
        print(f"Incorrect password. You have {opportunities} opportunities")

# If all attempts are used
if opportunities == 0:
    print("Authorities have been notified.")
