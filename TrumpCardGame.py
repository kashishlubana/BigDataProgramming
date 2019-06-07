import random
import time


class Card:

    def __init__(self, name, height, weight, rank, bicep, chest):
        self.name = name
        self.height = height
        self.weight = weight
        self.rank = rank
        self.bicep = bicep
        self.chest = chest


cards = []
cards.append(Card("John Cena", 1.88, 200, 3, 23, 42))
cards.append(Card("Rock", 1.88, 226, 5, 22, 46))
cards.append(Card("Stone Cold", 1.80, 212, 7, 20, 43))
cards.append(Card("HHH", 1.83, 227, 4, 21, 44))
cards.append(Card("Big Show", 2.48, 500, 9, 26, 51))
cards.append(Card("Kane", 2.40, 380, 11, 24, 46))
cards.append(Card("Undertaker", 2.33, 350, 8, 25, 45))
cards.append(Card("Shawn Michaels", 1.73, 225, 15, 20, 40))
cards.append(Card("Mark Henry", 2.20, 490, 12, 28, 55))
cards.append(Card("The Great Khali", 2.88, 420, 10, 27, 52))
cards.append(Card("Booker T", 1.90, 250, 13, 25, 49))
cards.append(Card("Jeff Hardy", 1.75, 180, 14, 21, 40))
cards.append(Card("Matt Hardy", 1.79, 240, 16, 22, 40))
cards.append(Card("Brock Lesnar", 1.99, 260, 1, 26, 48))
cards.append(Card("Kurt Angle", 1.88, 220, 6, 23, 42))
cards.append(Card("Bautista", 1.97, 250, 3, 27, 49))
random.shuffle(cards)

player1Deck = []
player2Deck = []
outDatedDeck = []

while len(cards) > 0:
    player1Deck.append(cards.pop(0))
    player2Deck.append(cards.pop(0))

player1Score = 0
player2Score = 0
player1Turn = True


allowedResponses = ["a", "b", "c", "d", "e"]
if player1Turn == True:
    while len(player1Deck) > 0 and len(player2Deck) > 0:

        time.sleep(1)

        player1Card = player1Deck.pop(0)
        godSpell = input("Player 1, Do you wish to use God Spell? True/ False")
        if godSpell == False:
            player2Card = player2Deck.pop(0)

            print("Player 1 Card")
            print("Name:", player1Card.name)
            print("a. Height:", player1Card.height)
            print("b. Weight:", player1Card.weight)
            print("c. Rank:", player1Card.rank)
            print("d. Bicep:", player1Card.bicep)
            print("e. Chest:", player1Card.chest)

            time.sleep(1)

            if player1Turn == True:
                answer = input("Which characteristic do you choose? ")
                while allowedResponses.count(answer) == 0:
                    answer = input("Please choose a valid option out of a,b,c,d and e: ")

            print("Player 2 CARD")
            print("Name:", player2Card.name)

            player1Wins = False

            if answer == "a":
                print("Height:", player2Card.height)
                isDraw = (player1Card.height == player2Card.height)
                player1Wins = (player1Card.height > player2Card.height)

            elif answer == "b":
                print("Weight:", player2Card.weight)
                isDraw = (player1Card.weight == player2Card.weight)
                player1Wins = (player1Card.weight > player2Card.weight)

            elif answer == "c":
                print("Rank:", player2Card.rank)
                isDraw = (player1Card.rank == player2Card.rank)
                player1Wins = (player1Card.rank < player2Card.rank)

            elif answer == "d":
                print("Bicep:", player2Card.bicep)
                isDraw = (player1Card.bicep == player2Card.bicep)
                player1Wins = (player1Card.bicep > player2Card.bicep)

            elif answer == "e":
                print("Chest:", player2Card.chest)
                isDraw = (player1Card.chest == player2Card.chest)
                player1Wins = (player1Card.chest > player2Card.chest)

            if player1Wins:
                print("Player 1 wins  the round!")
                outDatedDeck.append(player1Card)
                outDatedDeck.append(player2Card)
                player1Score += 1
                print("Player 1 score is :", player1Score)
                player1Turn = True
                player2Turn = False

            else:
                print("Player 2 wins  the round!")
                outDatedDeck.append(player2Card)
                outDatedDeck.append(player1Card)
                player2Score += 1
                print("Player 2 score is :", player2Score)
                player1Turn = False
                player2Turn = True



        else:
            print("Number of player 2 cards", len(player2Deck))
            cardNumber = input("Choose the card number of your opponent ")
            player2Card = player2Deck.pop(int(cardNumber))

            print("Player 1 Card")
            print("Name:", player1Card.name)
            print("a. Height:", player1Card.height)
            print("b. Weight:", player1Card.weight)
            print("c. Rank:", player1Card.rank)
            print("d. Bicep:", player1Card.bicep)
            print("e. Chest:", player1Card.chest)

            time.sleep(1)

            if player1Turn == True:
                answer = input("Which characteristic do you choose? ")
                while allowedResponses.count(answer) == 0:
                    answer = input("Please choose a valid option out of a,b,c,d and e: ")

            print("Player 2 CARD")
            print("Name:", player2Card.name)

            player1Wins = False

            if answer == "a":
                print("Height:", player2Card.height)
                isDraw = (player1Card.height == player2Card.height)
                player1Wins = (player1Card.height > player2Card.height)

            elif answer == "b":
                print("Weight:", player2Card.weight)
                isDraw = (player1Card.weight == player2Card.weight)
                player1Wins = (player1Card.weight > player2Card.weight)

            elif answer == "c":
                print("Rank:", player2Card.rank)
                isDraw = (player1Card.rank == player2Card.rank)
                player1Wins = (player1Card.rank < player2Card.rank)

            elif answer == "d":
                print("Bicep:", player2Card.bicep)
                isDraw = (player1Card.bicep == player2Card.bicep)
                player1Wins = (player1Card.bicep > player2Card.bicep)

            elif answer == "e":
                print("Chest:", player2Card.chest)
                isDraw = (player1Card.chest == player2Card.chest)
                player1Wins = (player1Card.chest > player2Card.chest)

            if player1Wins:
                print("Player 1 wins  the round!")
                outDatedDeck.append(player1Card)
                outDatedDeck.append(player2Card)
                player1Score += 1
                print("Player 1 score is :", player1Score)
                player1Turn = True
                player2Turn = False

            else:
                print("Player 2 wins  the round!")
                outDatedDeck.append(player2Card)
                outDatedDeck.append(player1Card)
                player2Score += 1
                print("Player 2 score is :", player2Score)
                player1Turn = False
                player2Turn = True
    else:
        player2Turn = True

        allowedResponses = ["a", "b", "c", "d", "e"]

        while len(player1Deck) > 0 and len(player2Deck) > 0:

            time.sleep(1)

            player1Card = player1Deck.pop(0)
            player2Card = player2Deck.pop(0)

            print("Player 2 Card")
            print("Name:", player2Card.name)
            print("a. Height:", player2Card.height)
            print("b. Weight:", player2Card.weight)
            print("c. Rank:", player2Card.rank)
            print("d. Bicep:", player2Card.bicep)
            print("e. Chest:", player2Card.chest)

            time.sleep(1)

            if player2Turn == True:
                answer = input("Player 2, Which characteristic do you choose? ")
                while allowedResponses.count(answer) == 0:
                    answer = input("Please choose a valid option out of a,b,c,d and e: ")

            print("Player 1 CARD")
            print("Name:", player1Card.name)

            player2Wins = False

            if answer == "a":
                print("Height:", player2Card.height)
                isDraw = (player1Card.height == player2Card.height)
                player2Wins = (player2Card.height > player1Card.height)

            elif answer == "b":
                print("Weight:", player2Card.weight)
                isDraw = (player1Card.weight == player2Card.weight)
                player2Wins = (player2Card.weight > player1Card.weight)

            elif answer == "c":
                print("Rank:", player2Card.rank)
                isDraw = (player2Card.rank == player1Card.rank)
                player2Wins = (player2Card.rank < player1Card.rank)

            elif answer == "d":
                print("Bicep:", player2Card.bicep)
                isDraw = (player2Card.bicep == player1Card.bicep)
                player2Wins = (player2Card.bicep > player1Card.bicep)

            elif answer == "e":
                print("Chest:", player2Card.chest)
                isDraw = (player2Card.chest == player1Card.chest)
                player2Wins = (player2Card.chest > player1Card.chest)

            if player2Wins:
                print("Player 2 wins  the round!")
                outDatedDeck.append(player1Card)
                outDatedDeck.append(player2Card)
                player1Turn = False
                player2Turn = True

            else:
                print("Player 1 wins  the round!")
                outDatedDeck.append(player2Card)
                outDatedDeck.append(player1Card)
                player1Turn = True
                player2Turn = False

time.sleep(2)

if player1Score > player2Score:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")