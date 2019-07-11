import pygame
import random

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

#set screen size
size = [400, 400]
pygame.display.set_caption("tic-tac-toe")
screen = pygame.display.set_mode(size)
icron = pygame.image.load('smile.bmp').convert()
pygame.display.set_icon(icron)

def displayboard():
	'''displays the game board'''
	pygame.draw.line(screen, BLACK, (130, 0), (130, 400), 5)
	pygame.draw.line(screen, BLACK, (260, 0), (260, 400), 5)
	pygame.draw.line(screen, BLACK, (0, 130), (400, 130), 5)
	pygame.draw.line(screen, BLACK, (0, 260), (400, 260), 5)

def placeO(posx, posy):
	'''place an O marker'''
	pygame.draw.circle(screen, BLUE, (posx, posy), 50, 5)

def placeX(posx, posy):
	'''place an X marker'''
	pygame.draw.line(screen, RED, (posx, posy), (posx + 100, posy + 100), 5)
	pygame.draw.line(screen, RED, (posx + 100, posy), (posx, posy + 100), 5)

def checkwin(cells):
	'''check for win condition'''
	x = "x"
	o = "o"
	win = "nobody"
	cat = "cat"
	counter = 0
	#row 1
	if (cells[0] + cells[1] + cells[2]) == 3:
		win = x
	elif (cells[0] + cells[1] + cells[2]) == -3:
		win = o
	else:
		pass #no win
	#row 2
	if (cells[3] + cells[4] + cells[5]) == 3:
		win = x
	elif (cells[3] + cells[4] + cells[5]) == -3:
		win = o
	else:
		pass #no win
	#row 3
	if (cells[6] + cells[7] + cells[8]) == 3:
		win = x
	elif (cells[6] + cells[7] + cells[8]) == -3:
		win = o
	else:
		pass #no win
	#col 1
	if (cells[0] + cells[3] + cells[6]) == 3:
		win = x
	elif (cells[0] + cells[3] + cells[6]) == -3:
		win = o
	else:
		pass #no win
	#col 2
	if (cells[1] + cells[4] + cells[7]) == 3:
		win = x
	elif (cells[1] + cells[4] + cells[7]) == -3:
		win = o
	else:
		pass #no win
	#col 3
	if (cells[2] + cells[5] + cells[8]) == 3:
		win = x
	elif (cells[2] + cells[5] + cells[8]) == -3:
		win = o
	else:
		pass #no win
	#diag 1
	if (cells[0] + cells[4] + cells[8]) == 3:
		win = x
	elif (cells[0] + cells[4] + cells[8]) == -3:
		win = o
	else:
		pass #no win
	#diag 2
	if (cells[2] + cells[4] + cells[6]) == 3:
		win = x
	elif (cells[2] + cells[4] + cells[6]) == -3:
		win = o
	else:
		pass #no win
	
	for i in range(0, len(cells)):
		if cells[i] != 0:
			counter += 1
	if counter == 9:
		win = cat
	
	return win

def determineposition(posx, posy):
	'''find which cell the player is placing their mark in'''
	cell = 9
	if posx <= 125 and posy <= 125:
		cell = 0
	elif posx > 130 and posx <= 255 and posy < 127:
		cell = 1
	elif posx >= 263 and posy <= 125:
		cell = 2
	elif posx <= 125 and posy >= 135 and posy <= 255:
		cell = 3
	elif posx >= 132 and posx <= 255 and posy >= 137 and posy <= 255:
		cell = 4
	elif posx >= 264 and posy >= 135 and posy <= 255:
		cell = 5
	elif posx <= 125 and posy >= 265:
		cell = 6
	elif posx >= 134 and posx <= 256 and posy >= 264:
		cell = 7
	elif posx >= 264 and posy >=265:
		cell = 8
	return cell

def updateboard(cells):
	'''update the game board with the new marks'''
	#0
	if cells[0] == 1:
		placeX(10, 10)
	elif cells[0] == -1:
		placeO(60, 60)
	else:
		pass #nothing there
	#1
	if cells[1] == 1:
		placeX(140, 10)
	elif cells[1] == -1:
		placeO(200, 60)
	else:
		pass #nothing there
	#2
	if cells[2] == 1:
		placeX(270, 10)
	elif cells[2] == -1:
		placeO(325, 60)
	else:
		pass #nothing there
	#3
	if cells[3] == 1:
		placeX(10, 140)
	elif cells[3] == -1:
		placeO(60, 190)
	else:
		pass #nothing there
	#4
	if cells[4] == 1:
		placeX(150, 140)
	elif cells[4] == -1:
		placeO(200, 190)
	else:
		pass #nothing there
	#5
	if cells[5] == 1:
		placeX(270, 140)
	elif cells[5] == -1:
		placeO(325, 190)
	else:
		pass #nothing there
	#6
	if cells[6] == 1:
		placeX(10, 270)
	elif cells[6] == -1:
		placeO(60, 330)
	else:
		pass #nothing there
	#7
	if cells[7] == 1:
		placeX(140, 270)
	elif cells[7] == -1:
		placeO(200, 330)
	else:
		pass #nothing there
	#8
	if cells[8] == 1:
		placeX(270, 270)
	elif cells[8] == -1:
		placeO(325, 330)
	else:
		pass #nothing there

def mousefollow(state, mouseposition):
	'''follow the mouse with the current player mark'''
	if state == "xmove":
		placeX(mouseposition[0], mouseposition[1])
	elif state == "omove":
		placeO(mouseposition[0], mouseposition[1])
	else:
		pass #invalid state


#main loop
done = False
clock = pygame.time.Clock()
clicked = 0
state = "Start"
cells = [0, 0, 0, 0, 0, 0, 0, 0, 0]
mauspos = (0, 0)
cell = 9
win = "nobody"
#print("init " + str(cells))#debug

while not done:
	clock.tick(10)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mauspos = pygame.mouse.get_pos()
			clicked = 1
	
	screen.fill(WHITE)
	displayboard()
	updateboard(cells)
	mousefollow(state, pygame.mouse.get_pos())
	if(state == "Start"):
		state = random.randint(1, 2)
		if state == 1:
			state = "xmove"
		else:
			state = "omove"
	elif state == "xmove" or state == "omove":
		if clicked == 1:	
			#if(state == "xmove"):#debug
				#print(state + " : " + str(mauspos))#debug
				#state = "omove"
			#elif(state == "omove"):#debug
				#print(state + " : " + str(mauspos))#debug
				#state = "xmove"
			cell = determineposition(mauspos[0], mauspos[1])	
			#print("cell " + str(cell)) #debug
			if cell < 9:
				if cells[cell] == 0:
					if state == "xmove":
						cells[cell] = 1
						state = "omove"
					elif state == "omove":
						cells[cell] = -1
						state = "xmove"
					else:
						pass #not valid state
				else:
					pass #space is taken
			else:
				pass #invalid cell selected
			#print(cells) #debug
			if checkwin(cells) != "nobody":
				#print(checkwin(cells))
				state = "over"
				#break #debug
		
	
	elif state == "over":
		for i in range(0, len(cells)):
			cells[i] = 0
		#print(cells) #debug
		win = "nobody"
		state = "Start"
		#done = True #debug	
	
	clicked = 0
	#print(state)#debug
	
	#placeO(200, 200)
	#placeX(10, 10)
	
	
	pygame.display.flip()
	
	pygame.time.wait(100)
