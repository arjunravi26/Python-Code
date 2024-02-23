from replit import clear

# Define the logo as a multi-line string
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

# Initialize variables to keep track of the highest bid
max_value = None
max_amount = 0

# Initialize a dictionary to store all the bids
bidder_collection = {}

# Start a loop that continues until there are no more bidders
while True:
    name = input("What is your name? \n")
    amount = int(input('What`s you bid? \n'))
    bidder_collection[name] = amount
    repeat = input("Are there any other bidders. Type 'yes' or 'no' ").lower()
    clear()

    # If there are more bidders, clear the console and start the next iteration
    if repeat == 'no':
        break

# Iterate over each bid in the bidder_collection dictionary
for key in bidder_collection:

    # If the current bid is higher than the highest bid so far
    if bidder_collection[key] > max_amount:

        # Update max_amount to the current bid and max_value to the current bidder
        max_amount = bidder_collection[key]
        max_value = key

print(f"{max_value} got bidder at {bidder_collection[max_value]} Rs")
