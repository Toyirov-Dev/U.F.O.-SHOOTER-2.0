import pygame
from pygame.locals import *
import random
import math
from pygame import mixer
from ursina import *

# initialize pygame!
pygame.init()

# creating the screen!
screen = pygame.display.set_mode((800,600)) # set_mode((800,600),  FULLSCREEN|SCALED) << it's fullscreen 

# Game title and icon!
pygame.display.set_caption("U.F.O. SHOOTER") # title

icon = pygame.image.load('Assets/icon.png') 
pygame.display.set_icon(icon) # icon

# Background music:
backmus = mixer.music.load('Assets/Backmus.wav')
mixer.music.play(-1)

# player 
playerImg = pygame.image.load('Assets/rocket.png')
playerX = 370
playerY = 520
playerX_change = 0



# Enemy 
EnemyImg = pygame.image.load('Assets/enemies/enemy1.png')
EnemyX = random.randint(0, 735)
EnemyY = random.randint(5, 53)
EnemyX_change = 0.2
EnemyY_change = 40


# Bullet 
BulletImg = pygame.image.load('Assets/bullet2.png')
BulletX = 0
BulletY = 520
BulletX_change = 0
BulletY_change = 2
Bullet_state = "ready"

# score:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
TextX = 10
TextY = 10

# Game over text:
over_font = pygame.font.Font('freesansbold.ttf', 100)


def Game_over():
	Over_text = font.render("GAME OVER!", True, (255, 0, 0))
	screen.blit(Over_text, (300, 300))


def Show_score(x,y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 0))
	screen.blit(score, (x, y))

def player(x,y):
	screen.blit(playerImg, (x, y))

def Enemy(x,y):
	screen.blit(EnemyImg, (x, y))

def Fire_bullet(x,y):
	global Bullet_state
	Bullet_state = "fire"
	screen.blit(BulletImg, (x + 16, y + 10))

def IsCollision(EnemyY, EnemyX, BulletY, BulletX):
	distanse = math.sqrt((math.pow(EnemyX-BulletX,2)) + (math.pow(EnemyY-BulletY,2)))
	if distanse < 27:
		return True
	else:
		return False


# Game loop!
running = True
while running:

	# screen color!
	screen.fill((0, 0, 0))
	



	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
			running = False
			# Exit! 
		
		# Keys!
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.4

			if event.key == pygame.K_RIGHT:
				playerX_change = 0.4



			if event.key == pygame.K_SPACE:
				if Bullet_state is "ready":
					Bullet_sound = mixer.Sound('Assets/laser.wav')
					Bullet_sound.play()
					# get the current x cordinate of spaceship!  
					BulletX = playerX
					Fire_bullet(BulletX, BulletY)

			if event.key == pygame.K_m:
				pygame.mixer.pause()

			if event.key == pygame.K_n:
				pygame.mixer.unpause()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
				


	# Rocket movement!
	playerX += playerX_change

	# border!
	if playerX <= 0:
		playerX = 0
	elif playerX >= 710: 
		playerX = 710

	# No border:
	"""
	if playerX <= 0:
		playerX = 710
	elif playerX >= 710: 
		playerX = 0
	"""

	# game over:
	if EnemyY > 450:
		EnemyY = 2000
		Game_over()



	# Enemy movement!
	EnemyX += EnemyX_change

	if EnemyX <= 0:
		EnemyX_change = 0.2 
		EnemyY += EnemyY_change
	elif EnemyX >= 690: 
		EnemyX_change = -0.2 
		EnemyY += EnemyY_change

	# Bullet movement!
	if BulletY <= 0:
		BulletY = 430
		Bullet_state = "ready"

	if Bullet_state is "fire":
		Fire_bullet(BulletX, BulletY)
		BulletY -= BulletY_change

	# collision:
	collision = IsCollision(EnemyY, EnemyX, BulletY, BulletX)
	if collision:
		explosion_sound = mixer.Sound('Assets/explosion.wav')
		explosion_sound.play()
		BulletY = 430 
		Bullet_state = "ready"
		score_value += 1

		# random joyda paydo bo'lish:
		EnemyX = random.randint(0, 735)
		EnemyY = random.randint(5, 53)

	if score_value == 10:
		EnemyImg = pygame.image.load('Assets/enemies/enemy2.png')
	if score_value == 20:
		EnemyImg = pygame.image.load('Assets/enemies/enemy3.png')
	if score_value == 30:
		EnemyImg = pygame.image.load('Assets/enemies/enemy4.png')
	if score_value == 40:
		EnemyImg = pygame.image.load('Assets/enemies/enemy5.png')
	if score_value == 50:
		EnemyImg = pygame.image.load('Assets/enemies/enemy6.png')
	if score_value == 60:
		EnemyImg = pygame.image.load('Assets/enemies/enemy7.png')
	if score_value == 70:
		EnemyImg = pygame.image.load('Assets/enemies/enemy8.png')
	if score_value == 80:
		EnemyImg = pygame.image.load('Assets/enemies/enemy9.png')
	if score_value == 90:
		EnemyImg = pygame.image.load('Assets/enemies/enemy10.png')
	if score_value == 100:
		EnemyImg = pygame.image.load('Assets/enemies/enemy11.png')
	if score_value == 110:
		EnemyImg = pygame.image.load('Assets/enemies/enemy12.png')
	if score_value == 120:
		EnemyImg = pygame.image.load('Assets/enemies/enemy13.png')






	player(playerX, playerY)
	Enemy(EnemyX, EnemyY)
	Show_score(TextX, TextY)
	pygame.display.update()
