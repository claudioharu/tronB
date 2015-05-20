#!/usr/bin/python

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron

import random
from example_grid import *
from minimaxLib import *
from math import sqrt

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

def new_flood_fill(board, startpos, obst):
	expand = [startpos]
	done = []
	while len(expand) is not 0:
		pos = expand.pop()
		done.append(pos)
		for dir in tron.DIRECTIONS:
			dest = board.rel(dir, pos)
			if board.passable(dest) and dest != obst and dest not in done and dest not in expand:
				expand.append(dest)

	return sorted(done)


def Obstacles(board):
	obs = []
	for x in range(0, board.width):
		for y in range (0, board.height):
			point = x, y
			if not board.passable(point):
				if board.me() != point and board.them() != point:
					obs.append([x, y])
	return obs

def wallBot(board):
	# wall bot
		ORDER = list(tron.DIRECTIONS)
		random.shuffle(ORDER)
		decision = board.moves()[0]
		for dir in ORDER:

			# where we will end up if we move this way
			dest = board.rel(dir)

			# destination is passable?
			if not board.passable(dest):
				continue

			# positions adjacent to the destination
			adj = board.adjacent(dest)

			# if any wall adjacent to the destination
			if any(board[pos] == tron.WALL for pos in adj):
				decision = dir
				break

		return decision

def which_move(board):

	graph, nodes = make_graph({"width": board.width, "height": board.height, "obstacle": Obstacles(board)})
	# print graph
	paths = None
	paths = AStarGrid(graph)
	start, end = nodes[board.me()[0]][board.me()[1]], nodes[board.them()[0]][board.them()[1]]
	path = paths.search(start, end)
	# print path

	if path is None:
		#return wallBot(board)
		tempo.inicializa()
		lixo, r = minimax(board, board.me(), board.them(), 0)
		return r
	else:
		# print "Path found:", path
		value = path[1].x, path[1].y
		path.pop(0)

		if abs(board.me()[0] - board.them()[0]) + abs(board.me()[1] - board.them()[1]) > 4:
		
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
		else:
			tempo.inicializa()
			lixo,r = minimax(board, board.me(), board.them(), 0)
			return r




for board in tron.Board.generate():
    tron.move(which_move(board))
