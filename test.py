import poker

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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
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
    check_cards = poker.text_to_cards(check_text)
    hand = poker.judge(check_cards)
    if (hand & (0xff * hand_offset)) == (hand_op * hand_offset):
        print(check_text, "OK")
    else:
        print(check_text, "NG")

# test straight flash rank
print("test straight flash rank")
lose_win_list = [
    ["sAs2s3s4s5cAdA", "s2s3s4s5s6cAdA"],
    ["s2s3s4s5s6cAdA", "s3s4s5s6s7cAdA"],
    ["s3s4s5s6s7cAdA", "s4s5s6s7s8cAdA"],
    ["s4s5s6s7s8cAdA", "s5s6s7s8s9cAdA"],
    ["s5s6s7s8s9cAdA", "s6s7s8s9sTcAdA"],
    ["s6s7s8s9sTcAdA", "s7s8s9sTsJcAdA"],
    ["s7s8s9sTsJcAdA", "s8s9sTsJsQcAdA"],
    ["s8s9sTsJsQcAdA", "s9sTsJsQsKcAdA"],
    ["s9sTsJsQsKcAdA", "sTsJsQsKsAcAdA"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test four of a kind rank
print("test four of a kind rank")
lose_win_list = [
    ["c2d2h2s2s7s8s9", "c3d3h3s3s7s8s9"],
    ["c3d3h3s3s7s8s9", "c4d4h4s4s7s8s9"],
    ["c4d4h4s4s7s8s9", "c5d5h5s5s7s8s9"],
    ["c5d5h5s5s7s8s9", "c6d6h6s6s7s8s9"],
    ["c6d6h6s6s7s8s9", "c7d7h7s7sQsKsA"],
    ["c7d7h7s7sQsKsA", "c8d8h8s8sQsKsA"],
    ["c8d8h8s8sQsKsA", "c9d9h9s9sQsKsA"],
    ["c9d9h9s9sQsKsA", "cTdThTsTs7s8s9"],
    ["cTdThTsTs7s8s9", "cJdJhJsJs7s8s9"],
    ["cJdJhJsJs7s8s9", "cQdQhQsQs7s8s9"],
    ["cQdQhQsQs7s8s9", "cKdKhKsKs7s8s9"],
    ["cKdKhKsKs7s8s9", "cAdAhAsAs7s8s9"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test full house rank
print("test full house rank")
lose_win_list = [
    ["c2d2h2c3d3cKdA", "c2d2h2c4d4cKdA"],
    ["c2d2h2c3d3c4d4", "c2d2h2c3d3c5d5"],
    ["c2d2h2c3d3cKcA", "c2d2c3d3h3cKcA"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test flash rank
print("test flash rank")
lose_win_list = [
    ["c2c3c4c5c7dKdA", "c2c3c4c5c8dKdA"],
    ["c2c3c4c5c8dKdA", "c2c3c4c5c9dKdA"],
    ["c2c3c4c5c9dKdA", "c2c3c4c5cTdKdA"],
    ["c2c3c4c5cTdKdA", "c2c3c4c5cJdKdA"],
    ["c2c3c4c5cJdKdA", "c2c3c4c5cQdKdA"],
    ["c2c3c4c5cQdKdA", "c2c3c4c5cKdKdA"],
    ["c2c3c4c5cKdKdA", "c2c3c4c5cAdKdA"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test straight rank
print("test straight rank")
lose_win_list = [
    ["hAs2s3s4s5cAdA", "h2s3s4s5s6cAdA"],
    ["h2s3s4s5s6cAdA", "h3s4s5s6s7cAdA"],
    ["h3s4s5s6s7cAdA", "h4s5s6s7s8cAdA"],
    ["h4s5s6s7s8cAdA", "h5s6s7s8s9cAdA"],
    ["h5s6s7s8s9cAdA", "h6s7s8s9sTcAdA"],
    ["h6s7s8s9sTcAdA", "h7s8s9sTsJcAdA"],
    ["h7s8s9sTsJcAdA", "h8s9sTsJsQcAdA"],
    ["h8s9sTsJsQcAdA", "h9sTsJsQsKcAdA"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test three of a kind rank
print("test three of a kind rank")
lose_win_list = [
    ["d2dKs2h2d4h5cQ", "d3dKs3h3d4h5cQ"],
    ["d3dKs3h3d4h5cQ", "dKh4s4c4d5h9d8"],
    ["dKh4s4c4d5h9d8", "d2d5h7d9sJc5s5"],
    ["d2d5h7d9sJc5s5", "d2d6h7d9sJc6s6"],
    ["d2d6h7d9sJc6s6", "d7dKs7h7d4h5cA"],
    ["d7dKs7h7d4h5cA", "d8dKs8h8d4h5cA"],
    ["d8dKs8h8d4h5cA", "d9dKs9h9d4h5cA"],
    ["d9dKs9h9d4h5cA", "dTdKsThTd4h5cA"],
    ["dTdKsThTd4h5cA", "dJdKsJhJd4h5cA"],
    ["dJdKsJhJd4h5cA", "dQdKsQhQd4h5cA"],
    ["dQdKsQhQd4h5cA", "d2dKh7d9sJcKsK"],
    ["d2dKh7d9sJcKsK", "dAdKsAhAd4h5cQ"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test two pair rank
print("test two pair rank")
lose_win_list = [
    ["d7s2c3hTs3d8c2", "d7s4c3hTs3d8c4"],
    ["d7s4c3hTs3d8c4", "c5d5cKc2d2c9dA"],
    ["c5d5cKc2d2c9dA", "d5h6c3s6h9s4d4"],
    ["d5h6c3s6h9s4d4", "d7cJh2s7cQd3c2"],
    ["d7cJh2s7cQd3c2", "s8h5c8d3sJc9s5"],
    ["s8h5c8d3sJc9s5", "s5c6dTc9h7h6d9"],
    ["s5c6dTc9h7h6d9", "s5c6d9cTh7h6dT"],
    ["s5c6d9cTh7h6dT", "s5c6dTcJh7h6dJ"],
    ["s5c6dTcJh7h6dJ", "sQdTcJs8d6hQc6"],
    ["sQdTcJs8d6hQc6", "s8h2dKh5h7hKd2"],
    ["s8h2dKh5h7hKd2", "s8h3dKh5h7hKd3"],
    ["s8h3dKh5h7hKd3", "sJhJhKc2dKc7s8"],
    ["sJhJhKc2dKc7s8", "sQhQhKc2dKc7s8"],
    ["sQhQhKc2dKc7s8", "s8h2dAh5h7hAd2"],
    ["s8h2dAh5h7hAd2", "s8h3dAh5h7hAd3"],
    ["s8h3dAh5h7hAd3", "s5dQhQhThAcAh6"],
    ["s5dQhQhThAcAh6", "d3h2dAd9sAhKsK"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test one pair rank
print("test one pair rank")
lose_win_list = [
    ["c2s7dKc3c9s2d4", "h3s6s9c4cKs5s3"],
    ["h3s6s9c4cKs5s3", "d5d6s4h8hTh3c4"],
    ["d5d6s4h8hTh3c4", "hQd2c4s5sAd5sT"],
    ["hQd2c4s5sAd5sT", "sJh2d6c7h6dAh5"],
    ["sJh2d6c7h6dAh5", "d8d7h7cAhKcTsJ"],
    ["d8d7h7cAhKcTsJ", "c8s8s7cKcTh5c6"],
    ["c8s8s7cKcTh5c6", "s9sKs4d9d3hJdQ"],
    ["s9sKs4d9d3hJdQ", "cAdJcQdTd9sTc5"],
    ["cAdJcQdTd9sTc5", "d3cTcQsJd4dJs9"],
    ["d3cTcQsJd4dJs9", "c2h4cQhQhKd5dT"],
    ["c2h4cQhQhKd5dT", "hKs6dKsQsTd2h7"],
    ["hKs6dKsQsTd2h7", "c8s3hJsKdAcAc5"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

# test high card rank
print("test high card rank")
lose_win_list = [
    ["c7d2c9s5h3c8s4", "c7d2c9s5hTc6s4"],
    ["c7d2c9s5hTc6s4", "c7dJc9s5hTc6s4"],
    ["c7dJc9s5hTc6s4", "h3c4d5h2dQsTs7"],
    ["h3c4d5h2dQsTs7", "sKd8s3dTs6h9h5"],
    ["sKd8s3dTs6h9h5", "hJhAs7s2c5h9c4"],
]
for lose_win in lose_win_list:
    lose_text = lose_win[0]
    win_text = lose_win[1]
    lose_cards = poker.text_to_cards(lose_text)
    win_cards = poker.text_to_cards(win_text)
    lose_hand = poker.judge(lose_cards)
    win_hand = poker.judge(win_cards)
    if lose_hand < win_hand:
        print(lose_text, "<", win_text, "OK")
    else:
        print(lose_text, "<", win_text, "NG", lose_hand, win_hand)

