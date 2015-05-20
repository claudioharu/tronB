#!/usr/bin/python

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron
import tempo
import random
stack = []


MAX = 2
NUM = 3**(MAX+1)

def invalid (board, move, position):
    return not board.passable(board.rel(move, position))

def same_position(board, p1_position, p1_move ,p2_position, p2_move):
    return board.rel(p1_move,p1_position) == board.rel(p2_move,p2_position)

def hasTime(prof):
   return prof<3
    

def estima(board, my_position, e_position):
    val = estimaRecurse(board, my_position, 0)
    val -= estimaRecurse(board, e_position, 0)
    return val/NUM

def estimaRecurse(board, position, depth):
    acmul = 0
    for pos in board.adjacent(position):
        if board.passable(pos):
            acmul+=1
            if depth != MAX: acmul += estimaRecurse(board, pos, depth+1)
    return acmul           

def minimax(board, my_position, e_position, profundidade):
	score_max = -4
	move_max = tron.NORTH
	tempo.subiuNivel()
	for move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
		if invalid(board, move, my_position):
			tempo.pula()
			continue
		score_enemy = 0
		board.tornaNaoPassavel(my_position)
		tempo.subiuNivel()
		for other_move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
			if invalid(board, other_move, e_position):
				score_enemy+=1
				tempo.pula()
				continue
			if same_position(board, my_position, move, e_position, other_move):
				tempo.pula() 
				continue
			if hasTime(profundidade):
				board.tornaNaoPassavel(e_position)
				myNewPosition,eNewPosition = board.rel(move,my_position),board.rel(other_move,e_position) 
				score, lixo = minimax(board, myNewPosition, eNewPosition, profundidade+1)
    				board.tornaPassavel(e_position) 
			else: score = estima(board, my_position, e_position)

			score_enemy+=score
		tempo.desceuNivel()
		if score_enemy > score_max:
			score_max = score_enemy
			move_max = move
    		board.tornaPassavel(my_position)
	tempo.desceuNivel()

	return score_max/4, move_max

# def which_move(board):
#     tempo.inicializa()

#     lixo,r = minimax(board, board.me(), board.them(), 0)
#     return r


# # you do not need to modify this part
# for board in tron.Board.generate():
#     tron.move(which_move(board))
