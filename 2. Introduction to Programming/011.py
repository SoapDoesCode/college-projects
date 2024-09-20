def find_individual(euros: float) -> int:
    # Find how many of eaxch make up the input, and then update the remainder for the next line to use
    num_50s = euros // 50; remainder = euros % 50
    num_20s = remainder // 20; remainder %= 20
    num_10s = remainder // 10; remainder %= 10
    num_5s = remainder // 5; remainder %= 5
    num_2s = remainder // 2; remainder %= 2
    num_1s = remainder // 1; remainder %= 1

    # separating whole numbers and decimals for readability
    num_050s = remainder // 0.50; remainder %= 0.50
    num_020s = remainder // 0.20; remainder %= 0.20
    num_010s = remainder // 0.10; remainder %=  0.10
    num_005s = remainder // 0.05; remainder %=  0.05
    num_002s = remainder // 0.02; remainder %=  0.02
    num_001s = remainder // 0.01

    # return all of the values
    return num_50s, num_20s, num_10s, num_5s, num_2s, num_1s, num_050s, num_020s, num_010s, num_005s, num_002s, num_001s

if __name__ == "__main__":
    print("Type 'quit' to stop the program")
    while True:
        user_num = input("Euros to break down: ") # takes the user input
        if user_num.lower() == "quit":
            exit(0) # stops the code when the user wants
        else:
            try:
                print(find_individual(float(user_num))) # print the output of the function
            except Exception as e: # raise an exception if the input is invalid
                print(f"Exception: {e}")