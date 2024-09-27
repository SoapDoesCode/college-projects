bottle_count = 10 # sets initial number of green bottles

while bottle_count > 0: # loops for as long as we have bottles remaining
    user_guess = int(input(f"""There are {bottle_count} green bottles hanging on the wall, {bottle_count} green bottles on the wall, and if 1 green bottle should accidentally fall
How many green bottles will be hanging on the wall?
Number of bottles: """)) # writes the poem to terminal and prompts the user for the number of remaining bottles
    
    if user_guess == bottle_count-1: # if the user guess is correct
        bottle_count -= 1 # update bottle count
        if bottle_count > 1: # checks if we have more than 1 bottle for grammar
            print(f"There will be {bottle_count} green bottles hanging on the wall") # outputs bottle count
        else: # if we have 1 bottle, once again for grammar
            print(f"There will be {bottle_count} green bottle hanging on the wall") # outputs bottle count
    else: # if the user guess is incorrect
        print("No, try again") # output their mistake

print("There are no more green bottles hanging on the wall") # end the rhyme