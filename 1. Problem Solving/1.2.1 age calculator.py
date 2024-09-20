def calculate_age(age_years):
    return age_years * 365 # calculate and return age in days

if __name__ == "__main__":
    print("Calculator for converting years to days!")
    age_years = int(input("How old are you in years?\nAge: "))
    print(f"You are {calculate_age(age_years)} days old")