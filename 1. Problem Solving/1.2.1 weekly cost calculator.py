import locale

locale.setlocale(locale.LC_ALL, 'en_GB') # setting currency locale

def calculate_weekly_cost(num_days: int, meal_price: float, drink_1_price: float, drink_2_price: float):
    total_meal = meal_price * num_days
    total_drink = num_days * (drink_1_price + drink_2_price)
    total_cost = round(total_meal + total_drink, 2) # calculates the total weekly cost

    cost_str = locale.currency(total_cost) # formats output to UK money format

    return cost_str # return function output

if __name__ == "__main__":
    print("Weekly meal budget calculator") # state program name
    num_days = float(input("How many days are you in college?\nDays: ")) # request how many days in college
    meal_price = float(input("How much do your meals cost?\nCost: ")) # request meal cost
    drink1_price = float(input("How much does your 1st drink cost?\nCost: ")) # request drink 1 cost
    drink2_price = float(input("How much does your 2nd drink cost?\nCost: ")) # request drink 2 cost
    
    print(f"Your total weekly cost is: {calculate_weekly_cost(num_days, meal_price, drink1_price, drink2_price)}")