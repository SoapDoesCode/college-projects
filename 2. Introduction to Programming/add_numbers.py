numbers = input("Please enter the numbers you'd like to add separated by commas e.g., 1, 2, 3\nNumbers: ").removesuffix(" ").removesuffix(",").split(", ")

total = 0

for value in numbers:
    total += float(value)

print(f"The numbers you input add up to: {total}")