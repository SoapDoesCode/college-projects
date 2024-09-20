while True:
    user_input = input("Enter 1, 2 or 3\nYour number: ") # prompts the user to input a number

    if user_input == "1": # checks if it is 1
        print("Thank you")
    elif user_input == "2": # checks if it is 2
        print("Well done")
    elif user_input == "3": # checks if it is 3
        print("Correct")
    else: # handles invalid inputs
        print("ERROR: Your input was not valid, please choose either 1, 2 or 3 next time")