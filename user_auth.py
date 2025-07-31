username = input("Enter username: ")

password = input("Enter password: ")

lower = upper = digit = special = 0
special_chars = "$#@"

if len(password) < 6 or len(password) > 12:
    print("Password length must be between 6 and 12 characters.")
else:
    for ch in password:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        elif ch.isdigit():
            digit += 1
        elif ch in special_chars:
            special += 1

    if lower == 0:
        print("Password must contain at least one lowercase letter.")
    if upper == 0:
        print("Password must contain at least one uppercase letter.")
    if digit == 0:
        print("Password must contain at least one digit.")
    if special == 0:
        print("Password must contain at least one special character from $, #, @.")

    if lower >= 1 and upper >= 1 and digit >= 1 and special >= 1:
        print("Signup successful!")


