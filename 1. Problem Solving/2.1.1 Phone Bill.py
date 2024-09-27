MONTHLY_BILL = 23 # define standard monthly bill
EXTRA_MIN_FEE = 0.02 # define the fee for extra minutes

total_charge = MONTHLY_BILL # set total charge to the monthly bill

minutes_used = int(input("How many minutes have you this month?\nMinutes: ")) # ask for the user's total minutes

if minutes_used > 600: # check if minutes used is over 600
    extra_minutes = minutes_used - 600 # calculate the extra minutes
    extra_cost = extra_minutes * EXTRA_MIN_FEE # calculate the fee for those minutes
    total_charge += extra_cost # add extra minutes fee to total cost

print(f"Your bill for this month comes to: £{total_charge}") # output the total cost