package main

import (
	"errors"
	"log/slog"
	"math/rand"
	"os"
	"time"
)

var logger *slog.Logger

func main() {
	logger = slog.New(slog.NewJSONHandler(os.Stdout, nil))

	if len(os.Args) < 2 {
		logger.Error("usage: porkerutils command <options>")
		os.Exit(1)
	}
	command := os.Args[1]

	switch command {
	case "hh":
		if err := hand_vs_hand(os.Args[1:]); err != nil {
			logger.Error(err.Error(), "command", command)
			os.Exit(1)
		}
	case "hr":
		if err := hand_vs_range(os.Args[1:]); err != nil {
			logger.Error(err.Error(), "command", command)
			os.Exit(1)
		}
	case "rr":
		if err := range_vs_range(os.Args[1:]); err != nil {
			logger.Error(err.Error(), "command", command)
			os.Exit(1)
		}
	case "bench":
		if err := all_check(); err != nil {
			logger.Error(err.Error(), "command", command)
			os.Exit(1)
		}
	}
}

func hand_vs_hand(hands []string) error {
	if len(hands) < 3 {
		return errors.New("usage: hh hand1 hand2")
	}
	hand1 := newCards(hands[1])
	target1 := make([]int, 7)
	target1[5] = hand1[0]
	target1[6] = hand1[1]

	board := make([]int, 5)
	win1 := 0
	win2 := 0
	count := 0

	hand2 := newCards(hands[2])
	target2 := make([]int, 7)
	target2[5] = hand2[0]
	target2[6] = hand2[1]

	deck := newDeck(5)
	for _, card := range hand1 {
		deck.remove(card)
	}
	for _, card := range hand2 {
		deck.remove(card)
	}

	for {
		if end := deck.nextBoard(board); end {
			break
		}

		target1[0] = board[0]
		target1[1] = board[1]
		target1[2] = board[2]
		target1[3] = board[3]
		target1[4] = board[4]

		target2[0] = board[0]
		target2[1] = board[1]
		target2[2] = board[2]
		target2[3] = board[3]
		target2[4] = board[4]

		rank1 := evaluate7(target1)
		rank2 := evaluate7(target2)

		if rank1 < rank2 {
			win1++
		} else if rank2 < rank1 {
			win2++
		}
		count++
	}
	println(hands[1], 100*win1/count, "%")
	println(hands[2], 100*win2/count, "%")

	return nil
}

func hand_vs_range(hands []string) error {
	if len(hands) < 3 {
		return errors.New("usage: hh hand range <board>")
	}
	hand1 := newCards(hands[1])
	target1 := make([]int, 7)
	target1[5] = hand1[0]
	target1[6] = hand1[1]

	board := make([]int, 5)
	preBoard := []int{}
	if len(hands) == 4 {
		preBoard = newCards(hands[3])
		for i, v := range preBoard {
			board[len(board)-i-1] = v
		}
	}
	comb := len(board) - len(preBoard)

	r := newRange(hands[2])
	target2 := make([]int, 7)

	win := 0
	count := 0
	for _, hand2 := range r {
		target2[5] = hand2[0]
		target2[6] = hand2[1]

		deck := newDeck(comb)
		for _, card := range hand1 {
			deck.remove(card)
		}
		for _, card := range hand2 {
			deck.remove(card)
		}
		for _, card := range preBoard {
			deck.remove(card)
		}

		for {
			if end := deck.nextBoard(board); end {
				break
			}

			for i, v := range board {
				target1[i] = v
				target2[i] = v
			}

			rank1 := evaluate7(target1)
			rank2 := evaluate7(target2)

			if rank1 < rank2 {
				win++
			}
			count++
		}
	}
	println(hands[2], 100*win/count, "%")

	return nil
}

func range_vs_range(ranges []string) error {
	if len(ranges) < 3 {
		return errors.New("usage: hh range range <board>")
	}
	target1 := make([]int, 7)
	target2 := make([]int, 7)
	board := make([]int, 5)
	preBoard := []int{}
	if len(ranges) == 4 {
		preBoard = newCards(ranges[3])
		for i, v := range preBoard {
			board[len(board)-i-1] = v
		}
	}
	comb := len(board) - len(preBoard)

	r1 := newRange(ranges[1])
	r2 := newRange(ranges[2])
	for _, hand1 := range r1 {
		target1[5] = hand1[0]
		target1[6] = hand1[1]

		win := 0
		count := 0
		for _, hand2 := range r2 {
			target2[5] = hand2[0]
			target2[6] = hand2[1]

			deck := newDeck(comb)
			for _, card := range hand1 {
				deck.remove(card)
			}
			for _, card := range hand2 {
				deck.remove(card)
			}
			for _, card := range preBoard {
				deck.remove(card)
			}

			for {
				if end := deck.nextBoard(board); end {
					break
				}

				for i, v := range board {
					target1[i] = v
					target2[i] = v
				}

				rank1 := evaluate7(target1)
				rank2 := evaluate7(target2)
				if rank1 < rank2 {
					win++
				}
				count++
			}
		}
		println(toText(hand1, " "), 100*win/count, "%")
	}

	return nil
}

func all_check() error {
	hand := make([]int, 7)
	deck := newDeck(7)

	s := time.Now()
	for {
		if end := deck.nextBoard(hand); end {
			break
		}
		evaluate(hand)

	}
	println("all check time:", time.Since(s).Seconds())

	randome_board := make([]int, 100000000*7)
	for i := range 100000000 {
		deck = newDeck(1)
		for j := range 7 {
			randome_board[i*7+j] = deck.cards[rand.Intn(len(deck.cards))]
			deck.remove(randome_board[i*7+j])
		}
	}

	sr := time.Now()
	for i := range 100000000 {
		evaluate(randome_board[i*7 : i*7+7])

	}
	println("all check time:", time.Since(sr).Seconds())

	return nil
}
