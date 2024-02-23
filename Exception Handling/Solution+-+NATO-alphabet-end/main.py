#

import pandas

output_list = None
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
while output_list is None:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only alphabet values  accept")
        word = input("Enter a word: ").upper()

print(output_list)
