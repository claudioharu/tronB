# Agente: MyTronBone
# Integrantes: 
# Claudio Junior 
# Diego Starling Fonseca
# Gabriel Torres Uber Bucek


import tron
import tempo
import random
stack = []


MAX = 4
NUM = 3**(MAX+1)
def invalid (board, move, position):
    return not board.passable(board.rel(move, position))

def same_position(board, p1_position, p1_move ,p2_position, p2_move):
    return board.rel(p1_move,p1_position) == board.rel(p2_move,p2_position)

def hasTime(prof):
    return prof < 2
    

def estima(board, my_position, e_position):
	board.tornaNaoPassavel(e_position)
	val = estimaRecurse(board, my_position, 0)
	board.tornaNaoPassavel(my_position)
	val -= estimaRecurse(board, e_position, 0)
	return val/NUM

def estimaRecurse(board, position, depth):
    acmul = 0
    for pos in board.adjacent(position):
        if board.passable(pos):
            board.tornaNaoPassavel(pos)
            acmul+=1
            if depth != MAX: acmul += estimaRecurse(board, pos, depth+1)
            board.tornaPassavel(pos)
    return acmul           

def minimax(board, my_position, e_position, profundidade):
	score_max = -4
	move_max = tron.NORTH
	
	board.tornaNaoPassavel(e_position)
	board.tornaNaoPassavel(my_position)
	tempo.subiuNivel()
	for move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
		if invalid(board, move, my_position):
			tempo.pula()
			continue
		score_min = 1
		tempo.subiuNivel()
		for other_move in [tron.NORTH, tron.SOUTH, tron.EAST, tron.WEST]:
			if invalid(board, other_move, e_position):
				score=1
				tempo.pula()
				continue
			if same_position(board, my_position, move, e_position, other_move):
				tempo.pula() 
				continue
			if tempo.hasTime(profundidade):
				myNewPosition,eNewPosition = board.rel(move,my_position),board.rel(other_move,e_position) 
				score, lixo = minimax(board, myNewPosition, eNewPosition, profundidade+1)
			else: score = estima(board, my_position, e_position)
			if score_min > score:
				score_min = score
		tempo.desceuNivel()
		if score_min > score_max:
			score_max = score_min
			move_max = move
    	board.tornaPassavel(my_position)
    	board.tornaPassavel(e_position) 
	tempo.desceuNivel()
	return score_max, move_max


