import random

# Define the card values
card_choice = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
card_names = list(card_choice.keys())

while True:
    random_playerCards = random.choices(card_names, k=2)
    random_dealerCards = random.choices(card_names, k=2)


    playerCards = random_playerCards
    dealerCards = random_dealerCards

    playerBusted = False
    dealerBusted = False

    playerValue = 0
    dealerValue = 0

    for cards in random_playerCards:
        if cards == "Ace": 
            playerValue += 11
        else:
            playerValue += card_choice[cards]
    if playerValue > 21 and "Ace" in playerCards:
        playerValue -= 10

    for cards in random_dealerCards:
        if cards == "Ace": 
            dealerValue += 11
        else:
            dealerValue += card_choice[cards]
    if dealerValue > 21 and "Ace" in dealerCards:
        dealerValue -= 10

    print("Player cards: ", playerCards, "You have: ", playerValue)
    print("Dealer cards: ", dealerCards, "Dealer has: ", dealerValue)
    print("-------------------------------")
        
    playerChoice = input("You can hit or stand: ").lower() 

    if playerChoice == "hit":
        hitCard = random.choice(list(card_choice))
        cardValue = card_choice[hitCard]
        if hitCard == "Ace":
            playerValue += 11
        else:
            playerValue += card_choice[hitCard]

        if playerValue > 21 and "Ace" in playerCards:
            playerValue -= 10

        print("You drew: ", hitCard, "You now have: ", playerValue)

    elif playerChoice == "stand":
        print("You stand. You still have: ", playerValue)

    if dealerValue < 14:
        dealerHitCard = random.choice(list(card_choice))
        dealerCardValue = card_choice[dealerHitCard]
        if dealerHitCard == "Ace":
            dealerValue += 11
        else:
            dealerValue += card_choice[dealerHitCard]

        if dealerValue > 21 and "Ace" in dealerCards:
            dealerValue -= 10

        dealerValue += dealerCardValue
        print("Dealer drew: ", dealerHitCard, "You now have: ", dealerValue)
    else:
        print("Dealer stands. He still has: ", dealerValue)

    print("-------------------------------")

    if playerValue > 21:
        playerBusted = True
        print("YOU BUSTED!")
    if dealerValue > 21:
        dealerBusted = True
        print("DEALER BUSTED!")

    if playerValue > dealerValue and not playerBusted and not dealerBusted:
        print("YOU WINNN!!")
    elif playerValue == dealerValue and not playerBusted and not dealerBusted:
        print("Its a tie!")
    else:
        print("YOU LOSEEE!!")

    print("-------------------------------")

