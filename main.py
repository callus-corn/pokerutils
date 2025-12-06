import random
import poker

for i in range(100):
    deck = poker.deck_new()
    random.shuffle(deck)

    hole_cards_1 = []
    for i in range(2):
        card, deck = poker.pick(deck)
        hole_cards_1.append(card)

    hole_cards_2 = []
    for i in range(2):
        card, deck = poker.pick(deck)
        hole_cards_2.append(card)

    board = []
    for i in range(5):
        card, deck = poker.pick(deck)
        board.append(card)

    seven_cards_1 = hole_cards_1 + board
    hand_1 = poker.judge(seven_cards_1)

    seven_cards_2 = hole_cards_2 + board
    hand_2 = poker.judge(seven_cards_2)

    print("board", poker.cards_to_text(board, " "))
    print("you", poker.cards_to_text(hole_cards_1, " "), poker.hand_to_text(hand_1))
    print("enemy", poker.cards_to_text(hole_cards_2, " "), poker.hand_to_text(hand_2))
    if hand_1 == hand_2:
        print("chop")
    elif hand_1 < hand_2:
        print("enemy win")
    elif hand_1 > hand_2:
        print("you win")
    print("")
