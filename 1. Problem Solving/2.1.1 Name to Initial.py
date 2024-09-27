first_name = input("What is your first name?\nFirst name: ")
last_name = input("What is your last name?\nLast name: ")

initial = first_name[0].upper()
formatted_last_name = last_name[0].upper() + last_name[1:].lower()

print(f"{initial}. {formatted_last_name}")


### One line version
# last_name = input("What is your last name?\nLast name: "); print(f"{input("What is your first name?\nFirst name: ")[0].upper()}. {last_name[0].upper()}{last_name[1:].lower()}")