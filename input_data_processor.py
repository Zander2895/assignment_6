first_name = input("Input your first name: ")
last_name = input("Input your last name: ")

if len(first_name) >= 2:
    print("The first name has been approved")
else:
    print("The first name must be two characters long")

if len(last_name) >= 2:
    print("The last name has been approved")
else:
    print("The last name must be two characters long")
