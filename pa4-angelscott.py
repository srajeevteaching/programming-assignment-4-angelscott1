# Programmers: Angel Scott
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: Yes or No (If user wants another card)
# Program Outputs: User's first two cards, any additional cards upon request, and their total points.
# Program Outputs: Dealer's first two cards, any additional cards, and their total points.
# Program Outputs: Outcome (You win or You Lose or Tie) and both player's hands


import random


# Function to make a general deck of cards and shuffle it. Returns a list of strings representing cards.
def deckofcards():
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
def cardname(list):
    x = 0
    while x <= 52:
        for i in list:
            card = list.pop(list.index(i))
            cardnumber, cardsuit = card.split(" ")
            cardnumber = int(cardnumber)
            if cardsuit == "c":
                cardsuit = "clubs"
            elif cardsuit == "d":
                cardsuit = "diamonds"
            elif cardsuit == "s":
                cardsuit = "spades"
            elif cardsuit == "h":
                cardsuit = "hearts"
            if cardnumber == 1:
                thecard = "Ace of " + cardsuit
            elif cardnumber == 11:
                thecard = "Jack of " + cardsuit
            elif cardnumber == 12:
                thecard = "Queen of " + cardsuit
            elif cardnumber == 13:
                thecard = "King of " + cardsuit
            else:
                thecard = str(cardnumber) + " of " + cardsuit
            return thecard
        x += 1


# Function to convert cards to points. Returns a list of point values.
def pointconversion(list):
    x = 0
    pointlist = []
    while x <= 52:
        for i in range(0, len(list)):
            card = list[i]
            cardnumber, cardsuit = card.split(" of ")
            if cardnumber.isdigit():
                point = int(cardnumber)
            elif cardnumber == "Ace":
                point = 11
            elif cardnumber == "Jack" or cardnumber == "Queen" or cardnumber == "King":
                point = 10
            pointlist.append(point)
        return pointlist
    x += 1


# Function to calculate sum of points in successive cards. Returns a list of point sums.
def sumofpoints(list):
    sumlist = []
    x = 0
    b = 2
    while x <= 50:
        thesum = sum(list[:b])
        b += 1
        sumlist.append(thesum)
        x += 1
    return sumlist


# Function to make a card list for the user's deck. Returns a list of cards.
def makingthedeck():
    x = 1
    thedeck = []
    while x <= 52:
        card = cardname(deckofcards())
        thedeck.append(card)
        x += 1
    return thedeck


# Function to find the first two cards in user's hand:
def userhand(decklist):
    cardsinhand = []
    cardsinhand.extend([decklist[0], decklist[1]])
    return cardsinhand


# Function to output user's first two cards, and their point total:
def userfirstcards(userhandlist, sumpointslist):
    print("Your first card is:", userhandlist[0])
    print("Your second card is:", userhandlist[1])
    print("Your total points is:", sumpointslist[0])
    return sumpointslist[0]


# Function to add cards to user's hand, and calculate total points until reaching or exceeding 21:
def userhandplus(list, sum):
    cardsinhand = []
    cardcount = 2
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
            cardcount += 1
            print("Your next card is:", list[i])
            if x < count:
                print("Your total point is:", sum[x])
                cardsinhand.append(list[i])
                if sum[x] != 21:
                    request = input("Do you request another card? Yes or No:")
                    request = request.strip().lower()
                else:
                    print("You have reached 21. You have won!")
                    return "End", list[0:cardcount]
            else:
                print("Total has exceeded 21. You have lost.")
                return "End", list[0:cardcount]
            i += 1
            x += 1
        if request == "no":
            print("Okay. Dealer will play now.")
            return sum[x-1], list[0:cardcount]
    elif request == "no":
        print("Okay. Dealer will play now.")
        return sum[0], list[0:cardcount]


# Function to create dealer's hand. Calculates total points until reaching or exceeding 17:
def dealerhand(dealerhand, dealersum):
    print("Dealer's first card is:", dealerhand[0])
    print("Dealer's second card is:", dealerhand[1])
    print("Dealer's total points is:", dealersum[0])
    cardcount = 2
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
            cardcount += 1
            if dealersum[x] >= 17 and dealersum[x] <= 21:
                print("The dealer has stopped requesting cards. Points will now be compared.")
                return dealersum[x], dealerhand[0:cardcount]
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
            return "End", dealerhand[0: cardcount]


# Game play:
def main():
    # Creating user's deck of cards, and a list of corresponding points.
    userdeck = makingthedeck()
    userhandlist = userhand(userdeck)
    userpoints = pointconversion(userdeck)

    # Creating a list of point totals to use as player draws from their deck.
    sumpointslist = sumofpoints(userpoints)
    x = 0
    while x <= 51:
        for i in sumpointslist:
            if int(i) > 21:
                sumpointslist.remove(i)
        x += 1

    # Printing user's first cards and their total.
    userstarterdeck = userfirstcards(userhandlist, sumpointslist)
    if userstarterdeck == 21:
        print("You won!")
        print("Your hand:", userhandlist[0:2])
    else:
        # Gameplay for user
        usergame, userfinalhand = userhandplus(userdeck, sumpointslist)

        # Checking user's status. If they did not reach or exceed 21, dealer will play.
        if usergame == "End":
            print("Game Over.")
            print("The user's hand:", userfinalhand)
        elif usergame != "End":
            # Creating dealer's deck of cards, and a list of corresponding points.
            dealerdeck = makingthedeck()
            dealerpoints = pointconversion(dealerdeck)

            # Creating a list of totals to use as the dealer draws from their deck.
            dealersumpointslist = sumofpoints(dealerpoints)
            x = 0
            while x <= 51:
                for i in dealersumpointslist:
                    if int(i) > 21:
                        dealersumpointslist.remove(i)
                x += 1

            # Printing dealer's hand and total until total reaches or exceeds 17.
            dealergame, dealerfinalhand = dealerhand(dealerdeck, dealersumpointslist)

            # Checking dealer's status. If they did not reach or exceed 21, points will be compared.
            if dealergame == "End":
                print("Game Over")
            else:
                # Comparing points. Printing the outcome.
                if usergame > dealergame:
                    print("Yay! You won!")
                elif usergame == dealergame:
                    print("It was a tie.")
                elif usergame < dealergame:
                    print("Sorry. You lost.")

            # Printing the player's hands.
            print("The user's hand:", userfinalhand)
            print("The dealer's hand:", dealerfinalhand)


main()
