import pygame
import sys


class Game:
    pass


class Board:
    pass


class Player:
    pass


# window
sizeWin = widthWin, heightWin = 500, 500
win = pygame.display.set_mode(sizeWin)

# board
rows = 6
columns = 7

board_startX = 10
board_startY = 10
sizeSq = 50
square = pygame.Rect(board_startX, board_startY, sizeSq, sizeSq)

spacesSq = 10

# player
spawnPoints = [35, 35]
pos = spawnPoints


def drawBoard():  # klasa
    for i in range(rows * columns):
        pygame.draw.rect(win, (5, 100, 70), square)
        square.x += (square.width + spacesSq)
        if square.x >= ((square.width + spacesSq) * columns):
            square.x = board_startX
            square.y += (square.height + spacesSq)
    square.y = board_startY


def main():
    pygame.init()
    pygame.display.set_caption('Plansza')

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                pos[0] += square.width + spacesSq  # pos[0] = pos.x
            if keys[pygame.K_LEFT]:
                pos[0] -= square.width + spacesSq
            if keys[pygame.K_DOWN]:
                pos[1] += square.height + spacesSq  # pos[1] = pos.y
            if keys[pygame.K_UP]:
                pos[1] -= square.height + spacesSq

            win.fill((0,0,0))
            drawBoard()
            player = pygame.draw.circle(win, (200, 0, 100), pos, 15)

            pygame.display.update()


main()
