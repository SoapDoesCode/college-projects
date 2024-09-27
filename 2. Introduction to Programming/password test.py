from getpass import getpass # used for hiding password input

password = "password123" # sets the password

correct_guess = False # used so we can stop the loop if the guess is correct

while correct_guess == False: # while 
    user_guess = getpass(prompt="Please input your password\nPassword: ") # prompts the user to guess

    if user_guess == password: # if they guess correctly
        print("You guessed the password successfully!") # yippee
        correct_guess = True # yippee
    else:
        print("Incorrect password attempt, please try again!") # if they guess wrong, tell them as such