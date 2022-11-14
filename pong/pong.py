import math
import random
import sys
import pygame


class Ball:
    velocity_y = 6
    velocity_x = 6
    # constant velocity of the ball that will be split into x and y components
    velocity = 12
    image = None
    first_hit = False

    def __init__(self, screen_width, screen_height):
        # creates the rectangle representing the ball in the middle of the screen
        self.image = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)

    # function to reset the ball when it goes off screen
    def reset(self, screen_width, screen_height):

        # checks if the ball has gone off the left or right of screen
        if self.image.left <= 0 or self.image.right >= screen_width:
            self.velocity = 12
            # updates the score based on which side of the screen it went off
            if self.image.left <= 0:
                player.score += 1

            else:
                opponent.score += 1

            # plays sound effect
            pygame.mixer.Sound.play(score_sound)
            # sets the position of the ball to the middle of the screen
            self.image.x = screen_width / 2 - 15
            self.image.y = screen_height / 2 - 15
            # sets the velocity of the ball, so it will go in a random direction
            self.velocity_y = random.choice((6, -6))
            self.velocity_x = random.choice((6, -6))
            self.first_hit = False

    # function to handle the movement and collisions of the ball
    def animation(self, screen_height, player1, player2):
        # updates the x and y coords with the velocity of the ball
        self.image.x += self.velocity_x
        self.image.y += self.velocity_y

        # if the ball hits the top or bottom of the screen it will bounce in the opposite direction and play sound
        if self.image.top <= 0 and self.velocity_y < 0:
            pygame.mixer.Sound.play(wall_bounce_sound)
            self.velocity_y *= -1

        if self.image.bottom >= screen_height and self.velocity_y > 0:
            self.velocity_y *= -1
            pygame.mixer.Sound.play(wall_bounce_sound)

        if self.image.colliderect(player1):
            # plays sound on collision
            pygame.mixer.Sound.play(paddle_bounce_sound)
            # increases the speed of the ball after every hit
            self.velocity += 0.5
            # max angle the ball can bounce off the paddle at
            max_angle = 45
            # calculates the difference between the center of ball and center of the paddle
            diff = (player1.centery - self.image.centery)
            # scales the number down so its between -1 and 1
            scaled_diff = diff / 70
            # the angle the ball will bounce at is calculated
            bounce_angle = max_angle * scaled_diff
            # the x and y components of the velocity given the angle are calculated
            self.velocity_x = abs(math.cos(math.radians(bounce_angle)) * self.velocity) * -1
            self.velocity_y = math.sin(math.radians(bounce_angle)) * self.velocity * -1

        if self.image.colliderect(player2):
            pygame.mixer.Sound.play(paddle_bounce_sound)
            self.velocity += 0.5
            max_angle = 45
            diff = (player2.centery - self.image.centery)
            scaled_diff = diff / 70
            bounce_angle = max_angle * scaled_diff
            self.velocity_x = abs(math.cos(math.radians(bounce_angle)) * self.velocity)
            self.velocity_y = math.sin(math.radians(bounce_angle)) * self.velocity * -1


class Player:
    score = 0
    velocity = 0
    image = None

    # creates a rectangle at the given x and y locations upon creating of an object
    def __init__(self, x, y):
        self.image = pygame.Rect(x, y, 20, 140)

    # function that moves the players paddle as long as moving it won't result in it going off-screen
    def manual_move(self, screen_height):
        if (0 < self.image.top or self.velocity > 0) and (self.image.bottom < screen_height or self.velocity < 0):
            self.image.y += self.velocity

    # function that automatically moves a players paddle so that it will follow the y position of the ball
    def auto_move(self, ball_y, ball_velocity_x, screen_height):
        if ball_velocity_x < 0:
            if self.image.y > ball_y and 0 < self.image.y:
                self.image.y -= 12

            if self.image.y < ball_y and self.image.bottom < screen_height:
                self.image.y += 12


# function that prints score
def display_score():
    screen_font = pygame.font.SysFont("impact", 128)
    player_score = screen_font.render(f"{player.score}", True, grey)
    opponent_score = screen_font.render(f"{opponent.score}", True, grey)
    screen.blit(opponent_score, (500, 20))
    screen.blit(player_score, (710, 20))


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# sounds
paddle_bounce_sound = pygame.mixer.Sound("paddle_bounce.mp3")
wall_bounce_sound = pygame.mixer.Sound("wall_bounce.mp3")
score_sound = pygame.mixer.Sound("score.mp3")

# sets the dimensions of the screen and creates the screen
screen_width = 1280
screen_height = 860
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# creates instances of the player and ball class
player = Player(screen_width - 60, screen_height / 2 - 70)
opponent = Player(40, screen_height / 2 - 70)
ball = Ball(screen_width, screen_height)

grey = (200, 200, 200)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checks if the up or down key is being pressed and adjusts the players velocity accordingly
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.velocity += 14

            if event.key == pygame.K_UP:
                player.velocity -= 14

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.velocity -= 14

            if event.key == pygame.K_UP:
                player.velocity += 14

    # moves player and opponent
    player.manual_move(screen_height)
    opponent.auto_move(ball.image.y, ball.velocity_x, screen_height)

    # moves ball
    ball.animation(screen_height, player.image, opponent.image)
    ball.reset(screen_width, screen_height)

    # updates screen
    clock.tick(60)
    screen.fill('black')
    display_score()
    pygame.draw.rect(screen, grey, player.image)
    pygame.draw.rect(screen, grey, opponent.image)
    pygame.draw.ellipse(screen, grey, ball.image)
    pygame.draw.aaline(screen, grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.display.update()
