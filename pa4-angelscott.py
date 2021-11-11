# Programmers: Angel Scott
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: Yes or No (If user wants another card)
# Program Outputs: User's first two cards, any additional cards upon request, and their total points.
# Program Outputs: Dealer's first two cards, any additional cards, and their total points.
# Program Outputs: Outcome (You win or You Lose or Tie) and both player's hands


import random


# Function to make a general deck of cards and shuffle it. Returns a list of strings representing cards.
def deck_of_cards():
    suits = ["c", "h", "d", "s"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck = []
    for i in range(len(numbers)):
        for j in range(len(suits)):
            card = numbers[i] + " " + suits[j]
            deck.append(card)
    random.shuffle(deck)
    return deck


# Function to convert a list of card strings to a list card names (number and suit). Returns a list of cards.
def card_name(list):
    x = 0
    while x <= 52:
        for i in list:
            card = list.pop(list.index(i))
            card_number, card_suit = card.split(" ")
            card_number = int(card_number)
            if card_suit == "c":
                card_suit = "clubs"
            elif card_suit == "d":
                card_suit = "diamonds"
            elif card_suit == "s":
                card_suit = "spades"
            elif card_suit == "h":
                card_suit = "hearts"
            if card_number == 1:
                the_card = "Ace of " + card_suit
            elif card_number == 11:
                the_card = "Jack of " + card_suit
            elif card_number == 12:
                the_card = "Queen of " + card_suit
            elif card_number == 13:
                the_card = "King of " + card_suit
            else:
                the_card = str(card_number) + " of " + card_suit
            return the_card
        x += 1


# Function to convert cards to points. Returns a list of point values.
def point_conversion(list):
    x = 0
    point_list = []
    while x <= 52:
        for i in range(0, len(list)):
            card = list[i]
            card_number, card_suit = card.split(" of ")
            if card_number.isdigit():
                point = int(card_number)
            elif card_number == "Ace":
                point = 11
            elif card_number == "Jack" or card_number == "Queen" or card_number == "King":
                point = 10
            point_list.append(point)
        return point_list
    x += 1


# Function to calculate sum of points in successive cards. Returns a list of point sums.
def sum_of_points(list):
    sum_list = []
    x = 0
    b = 2
    while x <= 50:
        the_sum = sum(list[:b])
        b += 1
        sum_list.append(the_sum)
        x += 1
    return sum_list


# Function to make a card list for the deck. Returns a list of cards.
def making_the_deck():
    x = 1
    the_deck = []
    while x <= 52:
        card = card_name(deck_of_cards())
        the_deck.append(card)
        x += 1
    return the_deck


# Function to find the first two cards in user's hand:
def user_hand(list):
    cards_in_hand = []
    cards_in_hand.extend([list[0], list[1]])
    return cards_in_hand


# Function to output user's first two cards, and their point total:
def user_first_cards(handlist, sumlist):
    print("Your first card is:", handlist[0])
    print("Your second card is:", handlist[1])
    print("Your total points is:", sumlist[0])
    return sumlist[0]


# Function to add cards to user's hand, and calculate total points until reaching or exceeding 21:
def user_hand_plus(list, sum):
    cards_in_hand = []
    card_count = 2
    request = input("Do you request another card? Yes or No:")
    request = request.strip().lower()
    if request != "yes" and request != "no":
        while request != "no" and request != "yes":
            print("Invalid answer.")
            request = input("Do you request another card? Yes or No:")
            request = request.strip().lower()
    if request == "yes":
        i = 2
        x = 1
        count = len(sum)
        while request == "yes":
            card_count += 1
            print("Your next card is:", list[i])
            if x < count:
                print("Your total point is:", sum[x])
                cards_in_hand.append(list[i])
                if sum[x] != 21:
                    request = input("Do you request another card? Yes or No:")
                    request = request.strip().lower()
                else:
                    print("You have reached 21. You have won!")
                    return "End", list[0:card_count]
            else:
                print("Total has exceeded 21. You have lost.")
                return "End", list[0:card_count]
            i += 1
            x += 1
        if request == "no":
            print("Okay. Dealer will play now.")
            return sum[x-1], list[0:card_count]
    elif request == "no":
        print("Okay. Dealer will play now.")
        return sum[0], list[0:card_count]


# Function to create dealer's hand. Calculates total points until reaching or exceeding 17:
def dealer_hand(dealerhand, dealersum):
    print("Dealer's first card is:", dealerhand[0])
    print("Dealer's second card is:", dealerhand[1])
    print("Dealer's total points is:", dealersum[0])
    card_count = 2
    if dealersum[0] >= 17:
        print("Points will now be compared.")
        return dealersum[0], dealerhand[0:2]
    else:
        i = 2
        x = 1
        count = len(dealersum)
        while x < count:
            print("The dealer's next card is:", dealerhand[i])
            print("The dealer's total points is:", dealersum[x])
            card_count += 1
            if dealersum[x] >= 17 and dealersum[x] <= 21:
                print("The dealer has stopped requesting cards. Points will now be compared.")
                return dealersum[x], dealerhand[0:card_count]
            elif dealersum[x] == 21:
                print("The dealer has reached 21. Sorry. You lost.")
            elif dealersum[x] > 21:
                print("The dealer's next card is:", dealerhand[i])
                print("The dealer's total points have exceeded 21. You win!")
            x += 1
            i += 1
        if x >= count:
            print("The dealer's next card is:", dealerhand[i])
            print("The dealer's total points have exceeded 21. You win!")
            return "End", dealerhand[0: card_count]


# Game play:
def main():
    # Program Purpose
    print("This program will allow you to play a simplified game of Blackjack with an automated dealer.")

    # Creating user's deck of cards, and a list of corresponding points.
    user_deck = making_the_deck()
    user_hand_list = user_hand(user_deck)
    user_points = point_conversion(user_deck)

    # Creating a list of point totals to use as player draws from their deck.
    sum_points_list = sum_of_points(user_points)
    x = 0
    while x <= 51:
        for i in sum_points_list:
            if int(i) > 21:
                sum_points_list.remove(i)
        x += 1

    # Printing user's first cards and their total.
    user_starter_deck = user_first_cards(user_hand_list, sum_points_list)
    if user_starter_deck == 21:
        print("You won!")
        print("Your hand:", user_hand_list[0:2])
    else:
        # Gameplay for user
        user_game, user_final_hand = user_hand_plus(user_deck, sum_points_list)

        # Checking user's status. If they did not reach or exceed 21, dealer will play.
        if user_game == "End":
            print("Game Over.")
            print("Your hand:", user_final_hand)
        elif user_game != "End":
            # Creating dealer's deck of cards, and a list of corresponding points.
            dealer_deck = making_the_deck()
            dealer_points = point_conversion(dealer_deck)

            # Creating a list of totals to use as the dealer draws from their deck.
            dealer_sum_points_list = sum_of_points(dealer_points)
            x = 0
            while x <= 51:
                for i in dealer_sum_points_list:
                    if int(i) > 21:
                        dealer_sum_points_list.remove(i)
                x += 1

            # Printing dealer's hand and total until total reaches or exceeds 17.
            dealer_game, dealer_final_hand = dealer_hand(dealer_deck, dealer_sum_points_list)

            # Checking dealer's status. If they did not reach or exceed 21, points will be compared.
            if dealer_game == "End":
                print("Game Over")
            else:
                # Comparing points. Printing the outcome.
                if user_game > dealer_game:
                    print("Yay! You won!")
                elif user_game == dealer_game:
                    print("It was a tie.")
                elif user_game < dealer_game:
                    print("Sorry. You lost.")

            # Printing the player's hands.
            print("Your hand:", user_final_hand)
            print("The dealer's hand:", dealer_final_hand)


main()
