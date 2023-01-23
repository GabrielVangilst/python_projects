import pygame
import sys
import random
import time


pygame.init()


# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS controller
fpsController = pygame.time.Clock()

# Snake's initial position
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

# randomly creates a position for the food
foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

# Snake starts going to the right
direction = 'RIGHT'
changeto = direction

score = 0

# Game over function
def gameOver():
   myFont = pygame.font.SysFont('monaco', 72)
   GOsurf = myFont.render('Game over!', True, red)
   GOrect = GOsurf.get_rect()
   GOrect.midtop = (360, 15)
   playSurface.blit(GOsurf, GOrect)
   showScore(0)
   pygame.display.flip()

   time.sleep(4)
   pygame.quit()  # pygame exit
   sys.exit()  # console exit

# Prints the score
def showScore(choice=1):
  # Sets font and displays score
   sFont = pygame.font.SysFont('monaco', 24)
   Ssurf = sFont.render('Score : {0}'.format(score), True, black)
   Srect = Ssurf.get_rect()
   Srect.midtop = (80, 10)
   playSurface.blit(Ssurf, Srect)

# Main Logic of the game
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
      # Checks if a directional key is pressed. If so it sets the snakes direction to that direction
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT or event.key == ord('d'):
               changeto = 'RIGHT'
           if event.key == pygame.K_LEFT or event.key == ord('a'):
               changeto = 'LEFT'
           if event.key == pygame.K_UP or event.key == ord('w'):
               changeto = 'UP'
           if event.key == pygame.K_DOWN or event.key == ord('s'):
               changeto = 'DOWN'
           if event.key == pygame.K_ESCAPE:
               pygame.event.post(pygame.event.Event(QUIT))


   # Makes it so the snake can not turn in the opposite direction
   if changeto == 'RIGHT' and not direction == 'LEFT':
       direction = 'RIGHT'
   if changeto == 'LEFT' and not direction == 'RIGHT':
       direction = 'LEFT'
   if changeto == 'UP' and not direction == 'DOWN':
       direction = 'UP'
   if changeto == 'DOWN' and not direction == 'UP':
       direction = 'DOWN'

   # Update snake position [x,y] so it moves in the correct direction
   if direction == 'RIGHT':
       snakePos[0] += 10
   if direction == 'LEFT':
       snakePos[0] -= 10
   if direction == 'UP':
       snakePos[1] -= 10
   if direction == 'DOWN':
       snakePos[1] += 10

   # Checks if the snake has collided with the food. If so an addtional square is added to it
   snakeBody.insert(0, list(snakePos))
   if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
       score += 1
       foodSpawn = False
   else:
       snakeBody.pop()
  
   # If the snake has collided with the food, the food spawns in another random location
   if foodSpawn == False:
       foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
   foodSpawn = True

   # Background
   playSurface.fill(white)

   # Draws Snake
   for pos in snakeBody:
       pygame.draw.rect(playSurface, green,
                        pygame.Rect(pos[0], pos[1], 10, 10))
  # Draws food
   pygame.draw.rect(playSurface, brown,
                    pygame.Rect(foodPos[0], foodPos[1], 10, 10))

   # Initiates a game over if the snake collides with boundary
   if snakePos[0] > 710 or snakePos[0] < 0:
       gameOver()
   if snakePos[1] > 450 or snakePos[1] < 0:
       gameOver()

   # Initiates a game over if the snake collides with itself
   for block in snakeBody[1:]:
       if snakePos[0] == block[0] and snakePos[1] == block[1]:
           gameOver()

   showScore()
   pygame.display.flip()
   fpsController.tick(23)