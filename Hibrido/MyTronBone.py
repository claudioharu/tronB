#!/usr/bin/python


# MyTronBone

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron

from aEstrelaConcreto import *
from minimaxLib import *


def obstacles(board):
	obs = []
	for x in range(0, board.width):
		for y in range (0, board.height):
			point = x, y
			if not board.passable(point):
				if board.me() != point and board.them() != point:
					obs.append([x, y])
	return obs


def which_move(board):

	nodo, grafo = boardGraph({ "obstaculos": obstacles(board), "largura": board.width, "altura": board.height})
	# print grafo
	paths = None
	paths = AEstrelaConcreto(grafo)

	start = nodo[board.me()[0]][board.me()[1]]
	goal = nodo[board.them()[0]][board.them()[1]]

	path = paths.caminho(start, goal)

	# Se nenhum caminho foi encontrado com o a-estrela utiliza-se o minimax
	if path is None:
		tempo.inicializa()
		lixo, r = minimax(board, board.me(), board.them(), 0)
		return r
	else:
		# print "Path found:", path
		value = path[1].x, path[1].y
		path.pop(0)

		# Verifica a distancia, se for menor que 4 usa-se o minimax
		if abs(board.me()[0] - board.them()[0]) + abs(board.me()[1] - board.them()[1]) > 4:
		
			if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == 1:
				return tron.EAST

			if (value[0] - board.me()[0]) == 0 and (value[1] - board.me()[1]) == -1:
				return tron.WEST
	
			if (value[0] - board.me()[0]) == 1 and (value[1] - board.me()[1]) == 0:
				return tron.SOUTH
	
			if (value[0] - board.me()[0]) == -1 and (value[1] - board.me()[1]) == 0:
				return tron.NORTH

		else:
			tempo.inicializa()
			lixo,r = minimax(board, board.me(), board.them(), 0)
			return r

for board in tron.Board.generate():
    tron.move(which_move(board))
