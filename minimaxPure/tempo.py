import time


pilha = []
quant = 0
fimNivel = 0
fimEste = 0
primeiro = True
cincoSegundos = 4.5
cincoSobreTresSegundos = cincoSegundos/3
tempoDeRetorno = 0.2

def pegaInstante():
	inst = time.time()
	return inst

def inicializa():
	global pilha, quant, fimNivel, fimEste, primeiro, cincoSegundos, cincoSobreTresSegundos
	pilha = []
	quant = 3
	agora = pegaInstante()
	fimNivel = agora + cincoSegundos
	fimEste = agora + cincoSobreTresSegundos
	primeiro = True
	return

def pula():
	global quant, primeiro, fimEste, fimNivel
	if primeiro : primeiro = False
	else:
		quant-=1
		if(quant!=0):
			agora = pegaInstante()
			fimEste = agora + (fimNivel - agora) / quant 
	return

def subiuNivel():
	global pilha, quant, fimNivel, fimEste, primeiro
	pilha.append((quant,fimNivel, fimEste, primeiro))
	fimNivel = fimEste
	quant = 3
	agora = pegaInstante()
	fimEste = agora + (fimNivel - agora) / quant
	primeiro = True
	return

def desceuNivel():
	global pilha, quant, fimEste, fimNivel, primeiro
	(quant, fimEste, fimNivel,primeiro) = pilha.pop()
	quant-=1
	agora=pegaInstante()
	if (quant!=0): fimEste = agora + (fimNivel - agora) / quant
	return

def hasTime(a):
	global fimEste, tempoDeRetorno, fimNivel, quant

	agora = pegaInstante()
	resposta = agora < fimEste - tempoDeRetorno
	if (not resposta):
		quant-=1
		if(quant!=0): fimEste = agora + (fimNivel - agora) / quant 
	return resposta
