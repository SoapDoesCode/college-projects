# takes the user input for how many people they'd like to invite
num_invites = int(input("How many people would you like to invite to the party?\nNumber of people: "))

if num_invites >= 10: # if 10 or more invites, return an error
    print("Too many people")
else: # else continue
    print("Please list the people's names below:") # give context to the user
    for invite in range(num_invites): # loop over each invite
        # request, and output the invited person's name and that they've been invited
        print(f"{input(f"Person {invite+1}'s name: ").capitalize()} has been invited!")