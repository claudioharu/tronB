#!/usr/bin/python

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron

import random

def flood_fill(board, startpos):
	expand = [startpos]
	done = []
	while len(expand) is not 0:
		pos = expand.pop()
		done.append(pos)
		for dir in tron.DIRECTIONS:
			dest = board.rel(dir, pos)
			if board.passable(dest) and dest not in done and dest not in expand:
				expand.append(dest)
	# print sorted(done)
	# return len(done)
	return sorted(done)

def which_move(board):

    # fill in your code here. it must return one of the following directions:
    #   tron.NORTH, tron.EAST, tron.SOUTH, tron.WEST

    # For now, choose a legal move randomly.
    # Note that board.moves will produce [NORTH] if there are no
    # legal moves available.
    x = 7
    y = 1
    value = flood_fill(board,  (x,y))
    print value

# you do not need to modify this part
for board in tron.Board.generate():
    tron.move(which_move(board))
