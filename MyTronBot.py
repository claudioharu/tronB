#!/usr/bin/python

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron

import random
from example_grid import *

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

	return sorted(done)

def Frame():
	mapFrame = []
	# print sorted(mapFrame)
	for i in range (0,15):
		mapFrame.append([0,i])

	for i in range (0, 15):
		mapFrame.append([15-1, i])

	for i in range (1, 15-1):
		mapFrame.append([i,0])

	for i in range (1, 15-1):
		mapFrame.append([i,15-1])

	return mapFrame

def which_move(board, path):
	# check walls
    # value = flood_fill(board,  board.me())
    # print value

	


	# print sorted(mapFrame)

	
	# if path is None:
	#     return random.choice(board.moves())
	# else:
	# print "Path found:", path
	value = path[1].x, path[1].y
	path.pop(0)
	
	if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == 1: 
		return tron.EAST
	if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == -1:
		return tron.WEST
	if (value[0] - board.me()[0]) == 1 and (value[1] - board.me()[1]) == 0:
		return tron.SOUTH
	if (value[0] - board.me()[0]) == -1 and (value[1] - board.me()[1]) == 0:
		return tron.NORTH
	# if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == 0:
	# 	return random.choice(board.moves())


graph, nodes = make_graph({"width": 15, "height": 15, "obstacle": Frame()})
# print graph
paths = None
paths = AStarGrid(graph)
start, end = nodes[1][1], nodes[13][13]
path = paths.search(start, end)
# print path
# you do not need to modify this part

for board in tron.Board.generate():
    tron.move(which_move(board, path))


