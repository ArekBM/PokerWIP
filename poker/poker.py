import random
import os


face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}
card_suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

card_values = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card:
    def __init__(self, suit, value):
        self.suit = suit

        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for v in card_values:
            for s in card_suits:
                if v in face_cards:
                    self.cards.append(Card(s, face_cards[v]))
                else:
                    self.cards.append(Card(s, v))



    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def final_hand(self):
        final_hand = []
        final_hand = eric.hand + table.table
        # for cards in final_hand:
        #     cards.show()
        return final_hand




class Table:
    def __init__(self):
        self.table = []

    def flop(self):
        print("\n")
        print("Flop")
        print("-------------------")
        self.table.append(deck.drawCard())
        self.table.append(deck.drawCard())
        self.table.append(deck.drawCard())
        for card in self.table:
            card.show()


    def turn(self):
        print("Turn")
        print("-------------------")
        self.table.append(deck.drawCard())
        for card in self.table:
            card.show()

    def river(self):
        print("River")
        print("-------------------")
        self.table.append(deck.drawCard())
        for card in self.table:
            card.show()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')





table = Table()
deck = Deck()

deck.shuffle()


eric = Player("Eric")
clear()

#Deal
eric.draw(deck)
eric.draw(deck)


print("Your hand")
print()
eric.showHand()

#Flop
table.flop()
input("Bet: ")
print()
clear()

#Turn
print("Your hand")
print()
eric.showHand()
print()
table.turn()
input("Bet: ")
clear()

#River
print("Your hand")
print()
eric.showHand()
print()
table.river()
input("Bet: ")
clear()
final_hand = eric.final_hand()




def evaluate(final_hand):
    suits = {}
    counts = {}
    vals = set()
    for card in final_hand:
        if card.suit in suits:
            suits[card.suit] += 1
        else:
            suits[card.suit] = 1
        if card.value in face_cards:
            card.value = face_cards[card.value]
        if card.value in counts:
            counts[card.value] += 1
        else:
            counts[card.value] = 1

        vals.add(card.value)

    sorted_suits = sorted(suits.items(), key=lambda item:(item[1], item[0]), reverse=True)
    sorted_counts = sorted(counts.items(), key=lambda item:(item[1], item[0]), reverse=True)
    # print(sorted_counts)
    # print(sorted_suits)
    run = [sorted(list(vals))[0]]
    lastval = sorted(list(vals))[0]
    is_straight = False
    for val in sorted(list(vals)):
        if val - lastval == 1:
            run.append(val)
        else:
            run = [val]
        lastval = val
        if len(run) == 5:
            is_straight = True
            break
        # print(f"last val: {lastval}")
        # print(f"run: {run}")

    # check if sorted_suits contains a flush
    is_flush = False
    if sorted_suits[0][1] == 5:
        is_flush = True
    # check for straight flush
    if is_straight:
        if is_flush:
            return "Straight Flush!"
    if sorted_counts[0][1] == 4:
        return f"Quad {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"
    if sorted_counts[0][1] == 3:
        if sorted_counts[1][1] == 2:
            return f"Full house {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s over {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}s!"
    if is_flush:
        return f"Flush in {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    if is_straight:
        return f"Straight! {run}"
    # check for groups
    # print(sorted_counts)

    if sorted_counts[0][1] == 3:
        return f"Triple {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}s!"
    if sorted_counts[0][1] == 2:
        if sorted_counts[1][1] == 2:
            return f"Two pair {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]} and {face_cards.get(sorted_counts[1][0]) if sorted_counts[1][0] in face_cards else sorted_counts[1][0]}!"
        else:
            return f"Pair of {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"
    if sorted_counts[0][1] == 1:
        return f"High Card {face_cards.get(sorted_counts[0][0]) if sorted_counts[0][0] in face_cards else sorted_counts[0][0]}!"


def determine():
    print(f"Your highest poker hand: {evaluate(final_hand)}")


determine()


#TODO Betting
#TODO Other Player
#TODO Determine best hand