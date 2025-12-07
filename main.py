import random
import poker
import itertools
import time

def all_check():
    deck = poker.deck_new()

    start = time.time()
    for comb in itertools.combinations(deck, 7):
        board = []
        for card in comb:
            board.append(card)
    
        hand = poker.judge(board)
    end = time.time()
    process_time = start - end
    print(process_time)

def win_rate_check():
    deck = poker.deck_new()

    hole_cards_1 = []
    card_1, deck = poker.select(deck, "cA")
    card_2, deck = poker.select(deck, "dA")
    hole_cards_1.append(card_1)
    hole_cards_1.append(card_2)

    hole_cards_2 = []
    card_3, deck = poker.select(deck, "h2")
    card_4, deck = poker.select(deck, "s3")
    hole_cards_2.append(card_3)
    hole_cards_2.append(card_4)

    dealer_board = []
    """    
    card_5, deck = poker.select(deck, "hA")
    card_6, deck = poker.select(deck, "sA")
    card_7, deck = poker.select(deck, "sK")
    dealer_board.append(card_5)
    dealer_board.append(card_6)
    dealer_board.append(card_7)
    """

    start = time.time()

    hand_1_win_count = 0
    hand_2_win_count = 0
    count = 0
    for comb in itertools.combinations(deck, 5 - len(dealer_board)):
        board = dealer_board.copy()
        for card in comb:
            board.append(card)
    
        seven_cards_1 = hole_cards_1 + board
        hand_1 = poker.judge(seven_cards_1)
    
        seven_cards_2 = hole_cards_2 + board
        hand_2 = poker.judge(seven_cards_2)
    
        if hand_1 < hand_2:
            hand_1_win_count += 1
        elif hand_2 < hand_1:
            hand_2_win_count += 1
        count += 1
    
    hole_cards_1_text = poker.cards_to_text(hole_cards_1, " ")
    hole_cards_2_text = poker.cards_to_text(hole_cards_2, " ")
    print(hole_cards_1_text + ":", round(100 * (hand_1_win_count / count)), "%")
    print(hole_cards_2_text + ":", round(100 * (hand_2_win_count / count)), "%")

    end = time.time()
    process_time = end - start
    print(process_time)

def random_check():
    for i in range(100):
        deck = poker.deck_new()
        random.shuffle(deck)
    
        card_1, deck = poker.pick(deck)
        card_2, deck = poker.pick(deck)
        
        hole_cards_1 = []
        hole_cards_1.append(card_1)
        hole_cards_1.append(card_2)
        
        card_3, deck = poker.pick(deck)
        card_4, deck = poker.pick(deck)
        
        hole_cards_2 = []
        hole_cards_2.append(card_3)
        hole_cards_2.append(card_4)
    
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
        elif hand_1 > hand_2:
            print("enemy win")
        elif hand_1 < hand_2:
            print("you win")
        print("")

win_rate_check()
#all_check()
