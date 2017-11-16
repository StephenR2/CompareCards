# Stephen Randall
# 11/15/17
# Folder: Unit9Project File: compare.py
# This is a card game that compares two players cards who ever has the greatest card wins. Uses two classes card.py and
# deck.py
import card
import deck
new_card = card.Card(1, "Hearts",)
new_deck = deck.Deck()
new_deck.shuffle()
print("======DONE SHUFFLE======")


def comparecards(firstcard, secondcard):
    """
    Compares the two cards it is given. If player one wins returns a value of 1 if player two wins returns a value of 2
    :param firstcard: Gets the first card that it's going to compare to the second card
    :param secondcard: Gets the second card that it's going to compare to the first card.
    :return: Returns either 1 or 2 to tell the playgame function who won and who to give the points to.
    """
    print("================")
    if firstcard.rank > secondcard.rank:
        return 1
    elif secondcard.rank > firstcard.rank:
        return 2
    else:
        if firstcard.suit > secondcard.suit:
            return 1
        elif secondcard.suit > firstcard.suit:
            return 2


def playgame(playeronecards, playertwocards):
    """
    Takes the return of comparecards and gives the points to the winner of the compare. Prints results.
    :param playeronecards: Gets player one's deck of cards.
    :param playertwocards: Gets player two's deck of cards.
    """
    play_question = input("Are you ready to play? (y/n)")
    if play_question == "y":
        playeronescore = 0  # Sets Player one score to zero
        playertwoscore = 0  # Sets Player two score to zero
        for x in range(len(playeronecards)):
            who_won = comparecards(playeronecards[x], playertwocards[x])  # Assigns the return value from function
            # comparecards to a variable "who_won"
            if who_won == 1:
                print("Player One has won!")
                playeronescore = playeronescore + 1   # Adds a point to the player one score if player one wins
            elif who_won == 2:
                print("Player Two has won!")
                playertwoscore = playertwoscore + 1   # Adds a point to the player two score if player two wins
            else:
                print("It was a tie.")
            print(playeronescore, playertwoscore)
            print("Player one card:", playeronecards[x])
            print("Player two card:", playertwocards[x])
        if playeronescore > playertwoscore:
            print("Player one won the game! Player one had:", playeronescore, "points!")
        elif playertwoscore > playeronescore:
            print("Player two won the game! Player two had:", playertwoscore, "points!")
        else:
            print("Player one score:", playeronescore)
            print("Player two score:", playertwoscore)
            print("It was a tie.")
    else:
        print("Bye! Have a nice day.")


def main():
    playeronecards = []
    playertwocards = []
    for x in range(5):
        playeronecards.append(new_deck.dealacard())
        playertwocards.append(new_deck.dealacard())
    playgame(playeronecards, playertwocards)

main()
