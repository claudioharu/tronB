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

def Frame(board):
	mapFrame = []
	# print sorted(mapFrame)
	for i in range (0,board.width):
		mapFrame.append([0,i])

	for i in range (0, board.width):
		mapFrame.append([board.height-1, i])

	for i in range (1, board.height-1):
		mapFrame.append([i,0])

	for i in range (1, board.height-1):
		mapFrame.append([i,board.width-1])

	return mapFrame

def Obstacles(board):
	obs = []
	for x in range(0, board.width):
		for y in range (0, board.height):
			point = x, y
			if not board.passable(point):
				if board.me() != point and board.them() != point:
					obs.append([x, y])
	return obs


def which_move(board):
	# check walls
    # value = flood_fill(board,  board.me())
    # print value

	


	# print sorted(mapFrame)


	graph, nodes = make_graph({"width": board.width, "height": board.height, "obstacle": Frame(board)})
	# print graph
	paths = None
	paths = AStarGrid(graph)
	start, end = nodes[board.me()[0]][board.me()[1]], nodes[board.them()[0]][board.them()[1]]
	path = paths.search(start, end)
	# print path
	# you do not need to modify this part

	if path is None:
		return random.choice(board.moves())
	else:
		# print "Path found:", path
		value = path[1].x, path[1].y
		path.pop(0)
		
		if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == 1:
			
			if not board.passable(value):
				return random.choice(board.moves())

			return tron.EAST
		if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == -1:
			if not board.passable(value):
				return random.choice(board.moves())
			return tron.WEST
		if (value[0] - board.me()[0]) == 1 and (value[1] - board.me()[1]) == 0:
			if not board.passable(value):
				return random.choice(board.moves())
			return tron.SOUTH
		if (value[0] - board.me()[0]) == -1 and (value[1] - board.me()[1]) == 0:
			if not board.passable(value):
				return random.choice(board.moves())
			return tron.NORTH
		# if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == 0:
		# 	return random.choice(board.moves())




for board in tron.Board.generate():
    tron.move(which_move(board))
