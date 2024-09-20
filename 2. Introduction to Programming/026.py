def gen_pig_latin(word):
    for vowel in "aeiou":
        return word + "way" if word[0] == vowel else ""
    return word[1:] + word[0] + "ay"

print("Pig Latin Generator")
while True:
    user_input = input("Enter your word to convert to Pig Latin!\nWord: ")
    
    print(gen_pig_latin(user_input.lower()))