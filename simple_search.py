# List of names
names = ["jake", "zac", "ian", "ron", "sam", "dave"]
# Convert all names to lowercase and store them in a set for fast searching
names_lower = {name.lower() for name in names}
# Keep the program running until the user types 'exit'
while True:
    # Get user input and remove extra spaces
    search = input("Enter name to search (or type 'exit' to quit): ").strip()
    # Exit condition
    if search.lower() == 'exit':
        break  #
    # Case-insensitive search
    if search.lower() in names_lower:
        print(f"{search} found in the list.")
    else:
        print(f"{search} not found in the list.")