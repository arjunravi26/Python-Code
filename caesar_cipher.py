import string
import caesar_cipher_art
print(caesar_cipher_art.logo)
alphabet = [i for i in string.ascii_lowercase]
text = ""
shift = 0
direction = ""


def get_inputs():
    global text, shift, direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ['encode', 'decode']:
        direction = input(
            "Invalid input!. Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("That's not a valid number. Please try again.")


restart = True
get_inputs()


def ceasar(plain_text, shift_amount, direction='encode'):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction == 'encode':
            position = (position + shift_amount) % len(alphabet)
        else:
            position = (position - shift_amount) % len(alphabet)

        cipher_text += alphabet[position]
    return cipher_text


while True:
    ceasar_text = ceasar(text, shift, direction)
    print(f"Your {direction} text is {ceasar_text}")
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    while restart not in ['yes', 'no']:
        direction = input(
            "Invalid input!. ype 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        print("Goodbye")
        break
    else:
        get_inputs()
