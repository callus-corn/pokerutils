import random
import poker
import itertools

deck = poker.deck_new()

card_1, deck = poker.select(deck, "cA")
card_2, deck = poker.select(deck, "dA")

hole_cards_1 = []
hole_cards_1.append(card_1)
hole_cards_1.append(card_2)

card_3, deck = poker.select(deck, "hA")
card_4, deck = poker.select(deck, "sA")

hole_cards_2 = []
hole_cards_2.append(card_3)
hole_cards_2.append(card_4)

win_count = 0
lose_count = 0
count = 0
for comb in itertools.combinations(deck, 5):
    board = []
    for card in comb:
        board.append(card)

    seven_cards_1 = hole_cards_1 + board
    hand_1 = poker.judge(seven_cards_1)

    seven_cards_2 = hole_cards_2 + board
    hand_2 = poker.judge(seven_cards_2)

    if hand_1 > hand_2:
        win_count += 1
    else:
        lose_count += 1
    count += 1

print(win_count, lose_count, win_count / count)

for i in range(0):
    deck = poker.deck_new()
    _, deck = poker.select(deck, "cA")
    _, deck = poker.select(deck, "dA")
    _, deck = poker.select(deck, "hA")
    _, deck = poker.select(deck, "sA")
    random.shuffle(deck)

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
