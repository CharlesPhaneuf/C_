import random

# Define the card values
card_choice = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": (1, 11)}

card_names = list(card_choice.keys())


random_cards = random.choices(card_names, k=2)

sum_of_values = 0
for card in random_cards:
    if card == "Ace":
        sum_of_values += 11  
    else:
        sum_of_values += card_choice[card]
        
print("Sum of Values:", sum_of_values)
