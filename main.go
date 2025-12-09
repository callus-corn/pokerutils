package main

import (
	"errors"
	"log/slog"
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
	case "ch":
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
		return errors.New("usage: hh hand range")
	}
	hand1 := newCards(hands[1])
	target1 := make([]int, 7)
	target1[5] = hand1[0]
	target1[6] = hand1[1]

	board := make([]int, 5)

	r := newRange(hands[2])
	target2 := make([]int, 7)

	win := 0
	count := 0
	for _, hand2 := range r {
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
				win++
			}
			count++
		}
	}
	println(hands[1])
	println(hands[2], 100*win/count, "%")

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
		evaluate7(hand)
	}
	println("all check time:", time.Since(s).Seconds())

	return nil
}
