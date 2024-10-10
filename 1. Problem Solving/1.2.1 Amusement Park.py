rides = {
    "ferris wheel": 2,
    "carousel": 3,
    "roller coaster": 5,
    "pirate ship": 2
}

print("You are at the park entrance, please pick a ride then insert your card to pay the fee for the ride")
print("Available rides:")
ride_num = 1
for ride in rides:
    print(f"{ride_num}. {ride}: £{rides[ride]}")
    ride_num += 1

card_balance = 0

while True:
    print(f"Current balance: £{card_balance}")
    card_balance += float(input("How much do you want to put on your card?\nAmount to add: £")) # asks the user for their balance
    print(f"Your new balance: £{card_balance}")
    ride_choice = input("Please choose a ride\nRide name: ").lower()
    
    try:
        # compares the card balance to the ride fee
        if card_balance >= rides[ride_choice]: # if they have enough:
            card_balance -= rides[ride_choice] # subtract ride fee from card
            print(f"Your new balance: £{card_balance}\nOpening barrier to {ride_choice}...") # output their new balance and open barrier
        else:
            # if they do not have enough, ask them to top up and then their balance will be output at the loop start
            print("You do not have high enough balance on your card, please add more")
    except:
        print(f"Invalid ride choice: {ride_choice}")