#!/usr/bin/python

# Copyright (C) 2010 Michael Spang. You may redistribute this file
# under the terms of the FreeBSD license.

"""Template for your tron bot"""

import tron

import random
stack = []


MAX = 4
NUM = 3**(MAX+1)
def invalid (board, move, position):
    return not board.passable(board.rel(move, position))

def same_position(board, p1_position, p1_move ,p2_position, p2_move):
    return board.rel(p1_move,p1_position) == board.rel(p2_move,p2_position)

def hasTime(prof):
    return prof<3
    
def simula_move(board, p1_position, p1_move, p2_position, p2_move):
    global stack
    stack.append((p1_position,p2_position))

    board.tornaNaoPassavel(p1_position)
    board.tornaNaoPassavel(p2_position)
    return board, board.rel(p1_move,p1_position),board.rel(p2_move,p2_position)

def restaura(board):
    global stack
    pos1, pos2 = 0, 0
    if len(stack) > 0:
        (pos1,pos2) = stack.pop()
    board.tornaPassavel(pos1)
    board.tornaPassavel(pos2)
    return board, pos1, pos2

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
	for move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
		if invalid(board, move, my_position): continue
		score_enemy = 0
		for other_move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
			if invalid(board, other_move, e_position):
				score_enemy+=1
				continue
			if same_position(board, my_position, move, e_position, other_move): continue
			if hasTime(profundidade):
				board, my_position, e_position = simula_move(board, my_position, move, e_position, other_move)
				score, lixo = minimax(board, my_position, e_position, profundidade+1)
			else: score = estima(board, my_position, e_position)
			board, my_position, e_position = restaura(board)
			score_enemy+=score
		if score_enemy > score_max:
			score_max = score_enemy
			move_max = move
	return score_max/4, move_max

def which_move(board):

    return minimax(board, board.me(), board.them(), 0)


# you do not need to modify this part
for board in tron.Board.generate():
    tron.move(which_move(board))
