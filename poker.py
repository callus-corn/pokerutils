# hand: xyyyy
# x: kind of hand
# y: rank of hand
hand_sf = 8
hand_fk = 7
hand_fh = 6
hand_fl = 5
hand_st = 4
hand_tk = 3
hand_tp = 2
hand_op = 1
hand_hc = 0
hand_offset = 0x10000
hand_offset_shift = 16

# card: rsp
# r: rank of card
# s: suit of card
# p: prime of card
suit_c = 0x1000
suit_d = 0x0100
suit_h = 0x0010
suit_s = 0x0001
suit_offset = 0x100
suit_offset_shift = 8

rank_offset = 0x1000000
rank_offset_shift = 24

prime = [0,0,2,3,5,7,11,13,17,19,23,29,31,37,41]

c2 =  2 * rank_offset + suit_c * suit_offset + prime[ 2]
d2 =  2 * rank_offset + suit_d * suit_offset + prime[ 2]
h2 =  2 * rank_offset + suit_h * suit_offset + prime[ 2]
s2 =  2 * rank_offset + suit_s * suit_offset + prime[ 2]
c3 =  3 * rank_offset + suit_c * suit_offset + prime[ 3]
d3 =  3 * rank_offset + suit_d * suit_offset + prime[ 3]
h3 =  3 * rank_offset + suit_h * suit_offset + prime[ 3]
s3 =  3 * rank_offset + suit_s * suit_offset + prime[ 3]
c4 =  4 * rank_offset + suit_c * suit_offset + prime[ 4]
d4 =  4 * rank_offset + suit_d * suit_offset + prime[ 4]
h4 =  4 * rank_offset + suit_h * suit_offset + prime[ 4]
s4 =  4 * rank_offset + suit_s * suit_offset + prime[ 4]
c5 =  5 * rank_offset + suit_c * suit_offset + prime[ 5]
d5 =  5 * rank_offset + suit_d * suit_offset + prime[ 5]
h5 =  5 * rank_offset + suit_h * suit_offset + prime[ 5]
s5 =  5 * rank_offset + suit_s * suit_offset + prime[ 5]
c6 =  6 * rank_offset + suit_c * suit_offset + prime[ 6]
d6 =  6 * rank_offset + suit_d * suit_offset + prime[ 6]
h6 =  6 * rank_offset + suit_h * suit_offset + prime[ 6]
s6 =  6 * rank_offset + suit_s * suit_offset + prime[ 6]
c7 =  7 * rank_offset + suit_c * suit_offset + prime[ 7]
d7 =  7 * rank_offset + suit_d * suit_offset + prime[ 7]
h7 =  7 * rank_offset + suit_h * suit_offset + prime[ 7]
s7 =  7 * rank_offset + suit_s * suit_offset + prime[ 7]
c8 =  8 * rank_offset + suit_c * suit_offset + prime[ 8]
d8 =  8 * rank_offset + suit_d * suit_offset + prime[ 8]
h8 =  8 * rank_offset + suit_h * suit_offset + prime[ 8]
s8 =  8 * rank_offset + suit_s * suit_offset + prime[ 8]
c9 =  9 * rank_offset + suit_c * suit_offset + prime[ 9]
d9 =  9 * rank_offset + suit_d * suit_offset + prime[ 9]
h9 =  9 * rank_offset + suit_h * suit_offset + prime[ 9]
s9 =  9 * rank_offset + suit_s * suit_offset + prime[ 9]
ct = 10 * rank_offset + suit_c * suit_offset + prime[10]
dt = 10 * rank_offset + suit_d * suit_offset + prime[10]
ht = 10 * rank_offset + suit_h * suit_offset + prime[10]
st = 10 * rank_offset + suit_s * suit_offset + prime[10]
cj = 11 * rank_offset + suit_c * suit_offset + prime[11]
dj = 11 * rank_offset + suit_d * suit_offset + prime[11]
hj = 11 * rank_offset + suit_h * suit_offset + prime[11]
sj = 11 * rank_offset + suit_s * suit_offset + prime[11]
cq = 12 * rank_offset + suit_c * suit_offset + prime[12]
dq = 12 * rank_offset + suit_d * suit_offset + prime[12]
hq = 12 * rank_offset + suit_h * suit_offset + prime[12]
sq = 12 * rank_offset + suit_s * suit_offset + prime[12]
ck = 13 * rank_offset + suit_c * suit_offset + prime[13]
dk = 13 * rank_offset + suit_d * suit_offset + prime[13]
hk = 13 * rank_offset + suit_h * suit_offset + prime[13]
sk = 13 * rank_offset + suit_s * suit_offset + prime[13]
ca = 14 * rank_offset + suit_c * suit_offset + prime[14]
da = 14 * rank_offset + suit_d * suit_offset + prime[14]
ha = 14 * rank_offset + suit_h * suit_offset + prime[14]
sa = 14 * rank_offset + suit_s * suit_offset + prime[14]

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
straight_list.append(prime[14]*prime[ 2]*prime[ 3]*prime[ 4]*prime[ 5])
straight_list.append(prime[ 2]*prime[ 3]*prime[ 4]*prime[ 5]*prime[ 6])
straight_list.append(prime[ 3]*prime[ 4]*prime[ 5]*prime[ 6]*prime[ 7])
straight_list.append(prime[ 4]*prime[ 5]*prime[ 6]*prime[ 7]*prime[ 8])
straight_list.append(prime[ 5]*prime[ 6]*prime[ 7]*prime[ 8]*prime[ 9])
straight_list.append(prime[ 6]*prime[ 7]*prime[ 8]*prime[ 9]*prime[10])
straight_list.append(prime[ 7]*prime[ 8]*prime[ 9]*prime[10]*prime[11])
straight_list.append(prime[ 8]*prime[ 9]*prime[10]*prime[11]*prime[12])
straight_list.append(prime[ 9]*prime[10]*prime[11]*prime[12]*prime[13])
straight_list.append(prime[10]*prime[11]*prime[12]*prime[13]*prime[14])

def deck_new():
    return master_deck.copy()

def judge(cards):
    pair_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in cards:
        pair_cards[(card & (0xff * rank_offset)) >> rank_offset_shift] += 1
    i = 0
    for num in pair_cards:
        # four of a kind
        if num == 4:
            rank = 0
            for card in cards:
                rank += (card & 0xff)
            return hand_fk * hand_offset + i * 100 + rank
        # full house
        if num == 3:
            j = i + 1
            for sub_num in pair_cards[j:]:
                if sub_num == 3:
                    return hand_fh * hand_offset + i + j * 15
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            return hand_fh * hand_offset + i * 15 + k
                        k += 1
                    return hand_fh * hand_offset + i * 15 + j
                j += 1
        if num == 2:
            j = i + 1
            for sub_num in pair_cards[j:]:
                if sub_num == 3:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            return hand_fh * hand_offset + j * 15 + k
                        k += 1
                    return hand_fh * hand_offset + i + j * 15
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 3:
                            return hand_fh * hand_offset + j + k * 15
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
        for straight_number in reversed(straight_list):
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
        for straight_number in reversed(straight_list):
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
        for straight_number in reversed(straight_list):
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
        for straight_number in reversed(straight_list):
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
    for straight_number in reversed(straight_list):
        if p % straight_number == 0:
            return hand_st * hand_offset + straight_list.index(straight_number)

    i = 0
    for num in pair_cards:
        # three of a kind
        if num == 3:
            rank = 0
            for card in cards:
                rank += (card & 0xff)
            return hand_tk * hand_offset + i * 100 + rank
        # one pair
        if num == 2:
            j = i + 1
            for sub_num in pair_cards[j:]:
                # two pair
                if sub_num == 2:
                    k = j + 1
                    for sub_sub_num in pair_cards[k:]:
                        if sub_sub_num == 2:
                            rank = 0
                            for card in cards:
                                rank += (card & 0xff)
                            return hand_tp * hand_offset + (j + k * 15) * 100 + rank
                        k += 1
                    rank = 0
                    for card in cards:
                        rank += (card & 0xff)
                    return hand_tp * hand_offset + (i + j * 15) * 100 + rank
                j += 1
            rank = 0
            for card in cards:
                rank += (card & 0xff)
            return hand_op * hand_offset + i * 100 + rank
        i += 1

    # high card
    rank = 0
    max_rank = 0
    for card in cards:
        rank += (card & 0xff)
        if (max_rank < (card & 0xff)):
            max_rank = card & 0xff
    rank += max_rank * 100

    return rank

def pick(deck):
    return deck[0], deck[1:]

def select(deck, card_text):
    card = text_to_card(card_text)
    deck.remove(card)
    return card, deck

def text_to_card(text):
    suit = text[0]
    n = text[1]
    card = -1

    if suit == "c":
        if n == "2":
            card = c2
        elif n == "3":
            card = c3
        elif n == "4":
            card = c4
        elif n == "5":
            card = c5
        elif n == "6":
            card = c6
        elif n == "7":
            card = c7
        elif n == "8":
            card = c8
        elif n == "9":
            card = c9
        elif n == "T":
            card = ct
        elif n == "J":
            card = cj
        elif n == "Q":
            card = cq
        elif n == "K":
            card = ck
        elif n == "A":
            card = ca
    elif suit == "d":
        if n == "2":
            card = d2
        elif n == "3":
            card = d3
        elif n == "4":
            card = d4
        elif n == "5":
            card = d5
        elif n == "6":
            card = d6
        elif n == "7":
            card = d7
        elif n == "8":
            card = d8
        elif n == "9":
            card = d9
        elif n == "T":
            card = dt
        elif n == "J":
            card = dj
        elif n == "Q":
            card = dq
        elif n == "K":
            card = dk
        elif n == "A":
            card = da
    elif suit == "h":
        if n == "2":
            card = h2
        elif n == "3":
            card = h3
        elif n == "4":
            card = h4
        elif n == "5":
            card = h5
        elif n == "6":
            card = h6
        elif n == "7":
            card = h7
        elif n == "8":
            card = h8
        elif n == "9":
            card = h9
        elif n == "T":
            card = ht
        elif n == "J":
            card = hj
        elif n == "Q":
            card = hq
        elif n == "K":
            card = hk
        elif n == "A":
            card = ha
    elif suit == "s":
        if n == "2":
            card = s2
        elif n == "3":
            card = s3
        elif n == "4":
            card = s4
        elif n == "5":
            card = s5
        elif n == "6":
            card = s6
        elif n == "7":
            card = s7
        elif n == "8":
            card = s8
        elif n == "9":
            card = s9
        elif n == "T":
            card = st
        elif n == "J":
            card = sj
        elif n == "Q":
            card = sq
        elif n == "K":
            card = sk
        elif n == "A":
            card = sa
    
    return card

def text_to_cards(text):
    cards = []
    for i in range(7):
        cards.append(text_to_card(text[i*2:i*2+2]))
    return cards

def cards_to_text(cards, delimiter=None):
    text = ""
    for card in cards:
        suit = (card & 0xffff00) >> suit_offset_shift
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

        if not delimiter is None:
            text += delimiter

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
