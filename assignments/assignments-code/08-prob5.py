cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
deck = [] + cards
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]

import random

hand = random.choices(cards, k=2) # pick two cards randomly
#hand = ['10 of Hearts', 'Ace of Clubs']
#hand = ['7 of Hearts', 'Ace of Clubs']
#hand = ['Ace of Clubs', 'Ace of Spades', 'Ace of Hearts']

for c in hand:
    deck.remove(c) # remove the chosen cards from the deck

def calculate_worth(hand):
    # default ace to equal 11
    # if the total score is greater than 21, however, ace should be 1
    worth = 0
    aces = 0
    for c in hand:
        if "Ace" in c:
            value = 1 # default ace value to 1 for now
            aces += 1
        else:
            value = values[cards.index(c)]
        worth += value # add values
    return worth, (worth + aces * 11)


while True:
    worth = calculate_worth(hand)
    if (worth[1] == worth[0]) or (worth[1] > 21):
        worth_string = str(worth[0])
    else:
        worth_string = str(worth[0]) + " or " + str(worth[1])
    print("Player hand:", hand, "is worth", worth_string)

    # win options
    if (worth[0] == 21) or (worth[1] == 21):
        print("You got Blackjack! You win!")
        break
    if worth[0] > 21:
        print("Bust!")
        print("Computer wins!")
        break

    play = input("(h)it or (s)tand? ")
    if play == "h":
        draw = random.choice(deck)
        print("You drew", draw)
        deck.remove(draw)
        hand.append(draw)
    if play == "s":
        comp_hand = random.choices(deck, k=2)
        for c in comp_hand:
            deck.remove(c)
        while True:
            comp_worth = calculate_worth(comp_hand)
            if (comp_worth[1] == comp_worth[0]) or (comp_worth[1] > 21):
                comp_worth_string = str(comp_worth[0])
            else:
                comp_worth_string = str(comp_worth[0]) + " or " + str(comp_worth[1])
            print("Computer hand:", comp_hand, "is worth", comp_worth_string)

            # win options
            if comp_worth[0] > 21:
                print("Bust!")
                print("Player wins!")
                break
            elif (comp_worth[0] == 21) or (comp_worth[1] == 21):
                print("Computer got 21! Blackjack!")
                print("Computer wins!")
                break
            elif comp_worth[0] > worth[0]:
                print("Computer wins!")
                break
            else:
                comp_draw = random.choice(deck)
                comp_hand.append(comp_draw)
                deck.remove(comp_draw)
                print("Computer drew", comp_draw)
        break
    
            
