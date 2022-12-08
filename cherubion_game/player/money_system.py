# Create a variable to keep track of the player's money
player_money = 0

# Function to add money to the player's money
def add_money(amount):
    global player_money
    player_money += amount

# Function to remove money from the player's money
def remove_money(amount):
    global player_money
    player_money -= amount

# Function to check if the player has enough money
def has_money(amount):
    global player_money
    return player_money >= amount

# Add money to the player's money
add_money(100)

# Check if the player has enough money to buy something
if has_money(50):
    # Remove money from the player's money
    remove_money(50)
    print("The player has bought something")
else:
    print("The player does not have enough money")