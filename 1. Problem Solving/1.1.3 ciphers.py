import string

def atbash_cipher(text):
    alphabet = string.ascii_letters
    reverse_alphabet = alphabet[::-1]

    atbash_dict = dict(zip(alphabet, reverse_alphabet))
    result = ''.join(atbash_dict.get(char, char) for char in text.upper())
    return result

def caesar_cipher(text, shift):
    alphabet = string.ascii_letters
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    print(shifted_alphabet)
    caesar_dict = dict(zip(alphabet, shifted_alphabet))
    result = ''.join(caesar_dict.get(char, char) for char in text.upper())
    return result

while True:
    text = input("Text to encode/decode: ")
    print(f"Atbash: {atbash_cipher(text)}")

    print(f"Caesar: {caesar_cipher(text, 13)}")