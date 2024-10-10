from random import randint as rng

dice_1 = rng(1,6) # simulate rollind a D6 dice and store it in a variable
dice_2 = rng(1,6)
dice_3 = rng(1,6)

print(f"The dice landed on: [{dice_1}, {dice_2}, {dice_3}]") # output the dice rolls

if dice_1 == dice_2 == dice_3: # check if all 3 dice roll the same
    total_score = dice_1 + dice_2 + dice_3 # add up all scores
    print(f"All dice rolled the same!\nYour score is: {total_score}") # output total
elif dice_1 == dice_2:
    total_score = dice_1 + dice_2 - dice_3 # add up the 2 same dice rolls and subtract the incorrect one
    print(f"Dice 1 and 2 rolled the same!\nYour score is: {total_score}") # output total
elif dice_1 == dice_3:
    total_score = dice_1 + dice_3 - dice_2
    print(f"Dice 1 and 3 rolled the same!\nYour score is: {total_score}")
elif dice_2 == dice_3:
    total_score = dice_2 + dice_3 - dice_1
    print(f"Dice 2 and 3 rolled the same!\nYour score is: {total_score}")
else:
    print("No dice rolled the same.\nGame over!") # if none are the same, end the game and output