import random
import sys
import itertools
import time
import poker


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

def range_check(board_text):
    board = poker.text_to_cards(board_text)

    utg_range = poker.utg_range_new()
    count = 0
    sf_count = 0
    fk_count = 0
    fh_count = 0
    fl_count = 0
    st_count = 0
    tk_count = 0
    tp_count = 0
    op_count = 0
    hc_count = 0
    for hole_cards in utg_range:
        if board[0] == hole_cards[0] or board[0] == hole_cards[1] or board[1] == hole_cards[0] or board[1] == hole_cards[1] or board[2] == hole_cards[0] or board[2] == hole_cards[1]:
            continue
        rank = poker.judge_5(board[0], board[1], board[2], hole_cards[0], hole_cards[1])
        if rank < 11:
            sf_count += 1
        elif rank < 167:
            fk_count += 1
        elif rank < 323:
            fh_count += 1
        elif rank < 1600:
            fl_count += 1
        elif rank < 1610:
            st_count += 1
        elif rank < 2468:
            tk_count += 1
        elif rank < 3326:
            tp_count += 1
        elif rank < 6186:
            op_count += 1
        elif rank < 7464:
            hc_count += 1
        count += 1
    print("UTG")
    print("straight flash:", 100*sf_count/count, "%")
    print("4 of a kind:", 100*fk_count/count, "%")
    print("full house:", 100*fh_count/count, "%")
    print("flash:", 100*fl_count/count, "%")
    print("straight:", 100*st_count/count, "%")
    print("3 of a kind:", 100*tk_count/count, "%")
    print("2 pair:", 100*tp_count/count, "%")
    print("1 pair:", 100*op_count/count, "%")
    print("high:", 100*hc_count/count, "%")
    print("")

    btn_range = poker.btn_range_new()
    count = 0
    sf_count = 0
    fk_count = 0
    fh_count = 0
    fl_count = 0
    st_count = 0
    tk_count = 0
    tp_count = 0
    op_count = 0
    hc_count = 0
    for hole_cards in btn_range:
        if board[0] == hole_cards[0] or board[0] == hole_cards[1] or board[1] == hole_cards[0] or board[1] == hole_cards[1] or board[2] == hole_cards[0] or board[2] == hole_cards[1]:
            continue
        rank = poker.judge_5(board[0], board[1], board[2], hole_cards[0], hole_cards[1])
        if rank < 11:
            sf_count += 1
        elif rank < 167:
            fk_count += 1
        elif rank < 323:
            fh_count += 1
        elif rank < 1600:
            fl_count += 1
        elif rank < 1610:
            st_count += 1
        elif rank < 2468:
            tk_count += 1
        elif rank < 3326:
            tp_count += 1
        elif rank < 6186:
            op_count += 1
        elif rank < 7464:
            hc_count += 1
        count += 1
    print("BTN")
    print("straight flash:", 100*sf_count/count, "%")
    print("4 of a kind:", 100*fk_count/count, "%")
    print("full house:", 100*fh_count/count, "%")
    print("flash:", 100*fl_count/count, "%")
    print("straight:", 100*st_count/count, "%")
    print("3 of a kind:", 100*tk_count/count, "%")
    print("2 pair:", 100*tp_count/count, "%")
    print("1 pair:", 100*op_count/count, "%")
    print("high:", 100*hc_count/count, "%")
    print("")

    utg_win_count = 0
    btn_win_count = 0
    vs_count = 0
    for utg_cards in utg_range:
        for btn_cards in btn_range:
            if board[0] == utg_cards[0] or board[0] == utg_cards[1] or \
               board[1] == utg_cards[0] or board[1] == utg_cards[1] or \
               board[2] == utg_cards[0] or board[2] == utg_cards[1] or \
               board[0] == btn_cards[0] or board[0] == btn_cards[1] or \
               board[1] == btn_cards[0] or board[1] == btn_cards[1] or \
               board[2] == btn_cards[0] or board[2] == btn_cards[1] or \
               utg_cards[0] == btn_cards[0] or utg_cards[0] == btn_cards[1] or \
               utg_cards[1] == btn_cards[0] or utg_cards[1] == btn_cards[1]:
                continue
            btn_rank = poker.judge_5(board[0], board[1], board[2], btn_cards[0], btn_cards[1])
            utg_rank = poker.judge_5(board[0], board[1], board[2], utg_cards[0], utg_cards[1])
            if btn_rank < utg_rank:
                btn_win_count += 1
            elif utg_rank < btn_rank:
                utg_win_count += 1
            count += 1
    print("UTG vs BTN")
    print(100*utg_win_count/count, "% vs", 100*btn_win_count/count, "%")
    print("")


#win_rate_check()
#all_check()
range_check(sys.argv[1])
