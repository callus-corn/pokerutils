import random
import itertools


hand_sf = 8
hand_fk = 7
hand_fh = 6
hand_fl = 5
hand_st = 4
hand_tk = 3
hand_tp = 2
hand_op = 1
hand_hc = 0

hand_offset = 0x100

suit_c = 0x1000
suit_d = 0x0100
suit_h = 0x0010
suit_s = 0x0001

suit_offset = 0x100
prime = [0,0,2,3,5,7,11,13,17,19,23,29,31,37,41]

c2 = suit_c * suit_offset + prime[2]
d2 = suit_d * suit_offset + prime[2]
h2 = suit_h * suit_offset + prime[2]
s2 = suit_s * suit_offset + prime[2]
c3 = suit_c * suit_offset + prime[3]
d3 = suit_d * suit_offset + prime[3]
h3 = suit_h * suit_offset + prime[3]
s3 = suit_s * suit_offset + prime[3]
c4 = suit_c * suit_offset + prime[4]
d4 = suit_d * suit_offset + prime[4]
h4 = suit_h * suit_offset + prime[4]
s4 = suit_s * suit_offset + prime[4]
c5 = suit_c * suit_offset + prime[5]
d5 = suit_d * suit_offset + prime[5]
h5 = suit_h * suit_offset + prime[5]
s5 = suit_s * suit_offset + prime[5]
c6 = suit_c * suit_offset + prime[6]
d6 = suit_d * suit_offset + prime[6]
h6 = suit_h * suit_offset + prime[6]
s6 = suit_s * suit_offset + prime[6]
c7 = suit_c * suit_offset + prime[7]
d7 = suit_d * suit_offset + prime[7]
h7 = suit_h * suit_offset + prime[7]
s7 = suit_s * suit_offset + prime[7]
c8 = suit_c * suit_offset + prime[8]
d8 = suit_d * suit_offset + prime[8]
h8 = suit_h * suit_offset + prime[8]
s8 = suit_s * suit_offset + prime[8]
c9 = suit_c * suit_offset + prime[9]
d9 = suit_d * suit_offset + prime[9]
h9 = suit_h * suit_offset + prime[9]
s9 = suit_s * suit_offset + prime[9]
ct = suit_c * suit_offset + prime[10]
dt = suit_d * suit_offset + prime[10]
ht = suit_h * suit_offset + prime[10]
st = suit_s * suit_offset + prime[10]
cj = suit_c * suit_offset + prime[11]
dj = suit_d * suit_offset + prime[11]
hj = suit_h * suit_offset + prime[11]
sj = suit_s * suit_offset + prime[11]
cq = suit_c * suit_offset + prime[12]
dq = suit_d * suit_offset + prime[12]
hq = suit_h * suit_offset + prime[12]
sq = suit_s * suit_offset + prime[12]
ck = suit_c * suit_offset + prime[13]
dk = suit_d * suit_offset + prime[13]
hk = suit_h * suit_offset + prime[13]
sk = suit_s * suit_offset + prime[13]
ca = suit_c * suit_offset + prime[14]
da = suit_d * suit_offset + prime[14]
ha = suit_h * suit_offset + prime[14]
sa = suit_s * suit_offset + prime[14]

master_deck = [
    c2, d2, h2, s2,
    c3, d3, h3, s3,
    c4, d4, h4, s4,
    c5, d5, h5, s5,
    c6, d6, h6, s6,
    c7, d7, h7, s7,
    c8, d8, h8, s8,
    c9, d9, h9, s9,
    ct, dt, ht, st,
    cj, dj, hj, sj,
    cq, dq, hq, sq,
    ck, dk, hk, sk,
    ca, da, ha, sa,
]

straight_list = []
straight_list.append(prime[14]*prime[2]*prime[3]*prime[4]*prime[5])
straight_list.append(prime[2]*prime[3]*prime[4]*prime[5]*prime[6])
straight_list.append(prime[3]*prime[4]*prime[5]*prime[6]*prime[7])
straight_list.append(prime[4]*prime[5]*prime[6]*prime[7]*prime[8])
straight_list.append(prime[5]*prime[6]*prime[7]*prime[8]*prime[9])
straight_list.append(prime[6]*prime[7]*prime[8]*prime[9]*prime[10])
straight_list.append(prime[7]*prime[8]*prime[9]*prime[10]*prime[11])
straight_list.append(prime[8]*prime[9]*prime[10]*prime[11]*prime[12])
straight_list.append(prime[9]*prime[10]*prime[11]*prime[12]*prime[13])
straight_list.append(prime[10]*prime[11]*prime[12]*prime[13]*prime[14])

def deck_new():
    return master_deck

def judge(cards):
    pair_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in cards:
        pair_cards[prime.index(card & 0xff)] += 1
    i = 0
    for num in pair_cards:
        # four of a kind
        if num == 4:
            return hand_fk * hand_offset + i
        # full house
        if num == 3:
            j = i+1
            for sub_num in pair_cards[j:]:
                if sub_num == 3:
                    return hand_fh * hand_offset + i + j
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            return hand_fh * hand_offset + i + k
                        k += 1
                    return hand_fh * hand_offset + i + j
                j += 1
        if num == 2:
            j = i+1
            for sub_num in pair_cards[j:]:
                if sub_num == 3:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            return hand_fh * hand_offset + j + k
                        k += 1
                    return hand_fh * hand_offset + i + j
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 3:
                            return hand_fh * hand_offset + j + k
                        k += 1
                j += 1
        i += 1

    # flash
    suit_count = 0x3333 * suit_offset
    for card in cards:
        suit_count += (card & (0xffff * suit_offset))
    # club
    if suit_count & (8 * suit_c * suit_offset) != 0:
        c_cards = []
        p = 1
        for card in cards:
            if (card & (suit_c * suit_offset)) != 0:
                c_cards.append(card)
                p *= card & 0xff
        # straight flash
        for straight_number in straight_list:
            if p == straight_number:
                return hand_sf * hand_offset + straight_list.index(straight_number)
        rank = 0
        for card in c_cards:
            if (rank < (card & 0xff)):
                rank = card & 0xff
        return hand_fl * hand_offset + rank
    # diamonds
    elif suit_count & (8 * suit_d * suit_offset) != 0:
        d_cards = []
        p = 1
        for card in cards:
            if (card & (suit_d * suit_offset)) != 0:
                d_cards.append(card)
                p *= card & 0xff
        # straight flash
        for straight_number in straight_list:
            if p == straight_number:
                return hand_sf * hand_offset + straight_list.index(straight_number)
        rank = 0
        for card in d_cards:
            if (rank < (card & 0xff)):
                rank = card & 0xff
        return hand_fl * hand_offset + rank
    # heart
    elif suit_count & (8 * suit_h * suit_offset) != 0:
        h_cards = []
        p = 1
        for card in cards:
            if (card & (suit_h * suit_offset)) != 0:
                h_cards.append(card)
                p *= card & 0xff
        # straight flash
        for straight_number in straight_list:
            if p == straight_number:
                return hand_sf * hand_offset + straight_list.index(straight_number)
        rank = 0
        for card in h_cards:
            if (rank < (card & 0xff)):
                rank = card & 0xff
        return hand_fl * hand_offset + rank
    # spade
    elif suit_count & (8 * suit_s * suit_offset) != 0:
        s_cards = []
        p = 1
        for card in cards:
            if (card & (suit_s * suit_offset)) != 0:
                s_cards.append(card)
                p *= card & 0xff
        # straight flash
        for straight_number in straight_list:
            if p == straight_number:
                return hand_sf * hand_offset + straight_list.index(straight_number)
        rank = 0
        for card in s_cards:
            if (rank < (card & 0xff)):
                rank = card & 0xff
        return hand_fl * hand_offset + rank

    # straight
    p = 1
    for card in cards:
        p = p * (card & 0xff)
    for straight_number in straight_list:
        if p % straight_number == 0:
            return hand_st * hand_offset + straight_list.index(straight_number)

    i = 0
    for num in pair_cards:
        # three of a kind
        if num == 3:
            return hand_tk * hand_offset + i
        # one pair
        if num == 2:
            j = i + 1
            for sub_num in pair_cards[j:]:
                # two pair
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            return hand_tp * hand_offset + j + k
                        k += 1
                    return hand_tp * hand_offset + i + j
                j += 1
            return hand_op * hand_offset + i
        i += 1

    # high card
    rank = 0
    for card in cards:
            if (rank < (card & 0xff)):
                rank = card & 0xff

    return rank

def pick(deck):
    return deck[0], deck[1:]

def text_to_card(text):
    card = 0
    suit = text[0]
    p = text[1]

    if suit == "c":
        card += suit_c * suit_offset
    elif suit == "d":
        card += suit_d * suit_offset
    elif suit == "h":
        card += suit_h * suit_offset
    elif suit == "s":
        card += suit_s * suit_offset

    if p == "2":
        card += prime[2]
    elif p == "3":
        card += prime[3]
    elif p == "4":
        card += prime[4]
    elif p == "5":
        card += prime[5]
    elif p == "6":
        card += prime[6]
    elif p == "7":
        card += prime[7]
    elif p == "8":
        card += prime[8]
    elif p == "9":
        card += prime[9]
    elif p == "T":
        card += prime[10]
    elif p == "J":
        card += prime[11]
    elif p == "Q":
        card += prime[12]
    elif p == "K":
        card += prime[13]
    elif p == "A":
        card += prime[14]

    return card

def text_to_cards(text):
    cards = []
    for i in range(7):
        cards.append(text_to_card(text[i*2:i*2+2]))
    return cards

def cards_to_text(cards):
    text = ""
    for card in cards:
        suit = (card & 0xffff00) >> 8
        p = card & 0xff
        if suit == suit_c:
            text += "c"
        elif suit == suit_d:
            text += "d"
        elif suit == suit_h:
            text += "h"
        elif suit == suit_s:
            text += "s"

        if p == prime[2]:
            text += "2"
        elif p == prime[3]:
            text += "3"
        elif p == prime[4]:
            text += "4"
        elif p == prime[5]:
            text += "5"
        elif p == prime[6]:
            text += "6"
        elif p == prime[7]:
            text += "7"
        elif p == prime[8]:
            text += "8"
        elif p == prime[9]:
            text += "9"
        elif p == prime[10]:
            text += "T"
        elif p == prime[11]:
            text += "J"
        elif p == prime[12]:
            text += "Q"
        elif p == prime[13]:
            text += "K"
        elif p == prime[14]:
            text += "A"

    return text

def hand_to_text(hand):
    hand = (hand & (0xff * hand_offset)) / hand_offset

    text = "unknown"
    if hand == hand_sf:
        text = "stragiht flash"
    elif hand == hand_fk:
        text = "four of a kind"
    elif hand == hand_fh:
        text = "full house"
    elif hand == hand_fl:
        text = "flash"
    elif hand == hand_st:
        text = "stragiht"
    elif hand == hand_tk:
        text = "three of a kind"
    elif hand == hand_tp:
        text = "two pair"
    elif hand == hand_op:
        text = "one pair"
    elif hand == hand_hc:
        text = "hight card"
    
    return text

# straight flash
print("test straight flash")
check_texts = [
    "cAc2c3c4c5dQdK",
    "dAd2d3d4d5hQhK",
    "hAh2h3h4h5sQsK",
    "sAs2s3s4s5cQcK",
    "c2c3c4c5c6dQdK",
    "d2d3d4d5d6hQhK",
    "h2h3h4h5h6sQsK",
    "s2s3s4s5s6cQcK",
    "c9cTcJcQcKd3d4",
    "d9dTdJdQdKh3h4",
    "h9hThJhQhKs3s4",
    "s9sTsJsQsKc3c4",
    "cTcJcQcKcAd3d4",
    "dTdJdQdKdAh3h4",
    "hThJhQhKhAs3s4",
    "sTsJsQsKsAc3c4",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_sf * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# four of a kind
print("test four of a kind")
check_texts = [
    "c2d2h2s2s7s8s9",
    "c3d3h3s3s7s8s9",
    "c4d4h4s4s7s8s9",
    "c5d5h5s5s7s8s9",
    "c6d6h6s6s7s8s9",
    "c7d7h7s7sQsKsA",
    "c8d8h8s8sQsKsA",
    "c9d9h9s9sQsKsA",
    "cTdThTsTs7s8s9",
    "cJdJhJsJs7s8s9",
    "cQdQhQsQs7s8s9",
    "cKdKhKsKs7s8s9",
    "cAdAhAsAs7s8s9",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_fk * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# full house
print("test full house")
check_texts = [
    "c2d2h2c3d3h3cA",
    "c2d2h2c3d3cKcA",
    "c2d2h2c3d3c4d4",
    "c2d2c3d3h3c4d4",
    "c2d2c3d3h3cKcA",
    "c2d2c3d3c4d4h4",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_fh * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# flash
print("test flash")
check_texts = [
    "c2c3c4c5cJdQdK",
    "d2d3d4d5dJhQhK",
    "h2h3h4h5hJsQsK",
    "s2s3s4s5sJcQcK",
    "c3c4c5c6cJdQdK",
    "d3d4d5d6dJhQhK",
    "h3h4h5h6hJsQsK",
    "s3s4s5s6sJcQcK",
    "d3d4c5cTcJcQcK",
    "h3h4d5dTdJdQdK",
    "s3s4h5hThJhQhK",
    "c3c4s5sTsJsQsK",
    "d3d4c5cJcQcKcA",
    "h3h4d5dJdQdKdA",
    "s3s4h5hJhQhKhA",
    "c3c4s5sJsQsKsA",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_fl * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# straight
print("test straight")
check_texts = [
    "sAc2c3c4c5dQdK",
    "s2c3c4c5c6dQdK",
    "s3c4c5c6c7dQdK",
    "s4c5c6c7c8dQdK",
    "s5c6c7c8c9dQdK",
    "s6c7c8c9cTdQdK",
    "s7c8c9cTcJd2d3",
    "s8c9cTcJcQd2d3",
    "sTcJcQcKcAd2d3",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_st * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# three of a kind
print("test three of a kind")
check_texts = [
    "c2d2h2s6s7s8s9",
    "c3d3h3s6s7s8s9",
    "c4d4h4s6s7s8s9",
    "c5d5h5sJsQsKsA",
    "c6d6h6sJsQsKsA",
    "c7d7h7sJsQsKsA",
    "c8d8h8sJsQsKsA",
    "c9d9h9sJsQsKsA",
    "cTdThTs3s4s5s6",
    "cJdJhJs3s4s5s6",
    "cQdQhQs3s4s5s6",
    "cKdKhKs3s4s5s6",
    "cAdAhAs3s4s5s6",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_tk * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# two pair
print("test two pair")
check_texts = [
    "c2d2h5s5s7s8s9",
    "c3d3h5s5s7s8s9",
    "c4d4h5s5s7s8s9",
    "c5d5h2s2sQsKsA",
    "c6d6h2s2sQsKsA",
    "c7d7h2s2sQsKsA",
    "c8d8h2s2sQsKsA",
    "c9d9h2s2sQsKsA",
    "cTdTh9s9s4s5s6",
    "cJdJh9s9s4s5s6",
    "cQdQh9s9s4s5s6",
    "cKdKh9s9s4s5s6",
    "cAdAh9s9s4s5s6",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_tp * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# one pair
print("test one pair")
check_texts = [
    "c2d2hAs6s7s8s9",
    "c3d3hAs6s7s8s9",
    "c4d4hAs6s7s8s9",
    "c5d5h2sJsQsKsA",
    "c6d6h2sJsQsKsA",
    "c7d7h2sJsQsKsA",
    "c8d8h2sJsQsKsA",
    "c9d9h2sJsQsKsA",
    "cTdTh9s3s4s5s6",
    "cJdJh9s3s4s5s6",
    "cQdQh9s3s4s5s6",
    "cKdKh9s3s4s5s6",
    "cAdAh9s3s4s5s6",
]
for check_text in check_texts:
    check_cards = text_to_cards(check_text)
    hand = judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_op * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

"""
for i in range(1000):
    deck = deck_new()
    random.shuffle(deck)

    hole_cards = []
    for i in range(2):
        card, deck = pick(deck)
        hole_cards.append(card)

    board = []
    for i in range(5):
        card, deck = pick(deck)
        hole_cards.append(card)

    seven_cards = hole_cards + board
    hand = judge(seven_cards)

    seven_cards_text = cards_to_text(seven_cards)
    print(cards_to_text(seven_cards), hand_to_text(hand))
"""
