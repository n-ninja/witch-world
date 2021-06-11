import pygame


class Window:
    def __init__(self, width, height, name):
        self.sizeWin = width, height
        self.name = name

        self.nameWindow()

    def get_sizeWin(self):
        return self.sizeWin

    def nameWindow(self):
        pygame.display.set_caption(self.name)


class Board:
    def __init__(self, win, sizeSq, spacesSq):
        self.rows = 6
        self.columns = 7
        self.board_startX, self.board_startY = 10, 10
        self.sizeSq = sizeSq
        self.spacesSq = spacesSq

        self.win = win

        self.square = pygame.Rect(self.board_startX, self.board_startY, self.sizeSq, self.sizeSq)


    def drawBoard(self):
        for i in range(self.rows * self.columns):

            pygame.draw.rect(self.win, (5, 100, 70), self.square)

            self.square.x += (self.square.width + self.spacesSq)
            if self.square.x >= ((self.square.width + self.spacesSq) * self.columns):
                self.square.x = self.board_startX
                self.square.y += (self.square.height + self.spacesSq)

        self.square.y = self.board_startY


class Player:
    def __init__(self, win, board, spawnPoints):
        self.spawnPoints = spawnPoints
        self.pos = self.spawnPoints
        self.size = 15
        self.board = board
        self.win = win

    def drawPlayer(self):
        pygame.draw.circle(self.win, (200, 0, 100), self.pos, self.size)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.board.square.width + self.board.spacesSq  # pos[0] = pos.x
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.board.square.width + self.board.spacesSq
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.board.square.height + self.board.spacesSq  # pos[1] = pos.y
        if keys[pygame.K_UP]:
            self.pos[1] -= self.board.square.height + self.board.spacesSq


def main():

    pygame.init()

    mainWindow = Window(1000,1000, "Plansza")
    mainWindow = pygame.display.set_mode(mainWindow.get_sizeWin())


    board = Board(mainWindow, 100, 10)
    player = Player(mainWindow, board, [35,35])

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mainWindow.fill((0,0,0))
            board.drawBoard()
            player.move()
            player.drawPlayer()

            pygame.display.update()

main()

