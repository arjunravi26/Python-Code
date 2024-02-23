# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
import string
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
print(symbols)

print("Welcome to the PyPassword Generator!")

n_char = int(input("How many letters would you like in your password?\n"))
n_num = int(input(f"How many numbers would you like?\n"))
n_sym = int(input(f"How many symbols would you like?\n"))
pass_list = []
for i in range(1, n_char+1):
    pass_list.append(random.choice(letters))

for i in range(1, n_num+1):
    pass_list.append(random.choice(numbers))

for i in range(1, n_sym+1):
    pass_list.append(random.choice(symbols))

random.shuffle(pass_list)
password = ''.join(pass_list)
print(f"Your password is {password}")
