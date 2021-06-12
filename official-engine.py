import pygame
import time

class Window:
    def __init__(self, width, height, name):
        self.sizeWin = width, height
        self.name = name
        self.nameWindow()

    def get_sizeWin(self):
        return self.sizeWin

    def nameWindow(self):
        pygame.display.set_caption(self.name)

class Square:
    def __init__(self, win, x, y, col):
        self.win = win
        self.x = x  # x, y współrzędne generowania kwadratu
        self.y = y
        self.color = col

    def draw(self, x, y, size):
        pygame.draw.rect(self.win, self.color, pygame.Rect(x, y, 50, 50))

class Board(Square):
    def __init__(self, win, a, b, i_size, j_size):  # x,y = start_a, start_b
        self.win = win
        self.i_size, self.j_size = i_size, j_size

        # INDEKS GRACZA
        self.a, self.b = a, b

        self.sizeSq = 50
        self.margin = 6
        self.sm = self.sizeSq + self.margin

        #colors
        self.boardColor = (22,55,1)
        self.playerColor=(210,148,41)
        self.metaColor=(17,11,7)
        self.p_curedColor=(204,190,180)
        self.obsColor=(197,168,143)

        self.board = []
        self.nextMove = ""
        self.moveNum = 0
        self.list_obstacle=[
                        [0, 3],
                        [1, 0],
                        [2, 0],
                        [2, 5],
                        [3, 2],
                        [4, 2],
                        [5, 4],
                        [6, 0],
                        ]
        
        self.player_coordinates= [[self.a],[self.b]]
        self.meta_coordinates = [6,1]
        self.player_on_meta = False
        self.finished_board = False

        for i in range(self.i_size):
            p = []
            for j in range(self.j_size):
                obj = Square(self.win, i, j, self.boardColor)
                p.append(obj)
            self.board.append(p)

    def get_sizeSq(self):
        return self.sizeSq

    def get_margin(self):
        return self.margin

    def get_sm(self):
        return self.sm

    def player(self): #tutaj dzieje się cała mechanika
        key = pygame.key.get_pressed()
        self.board[self.a][self.b].color = self.boardColor
        self.board[self.meta_coordinates[0]][self.meta_coordinates[-1]].color = self.metaColor

        for p in range(len(self.list_obstacle)):
            self.block_x=self.list_obstacle[p][0]
            self.block_y=self.list_obstacle[p][-1]
            self.board[self.block_x][self.block_y].color = self.obsColor

        if key[pygame.K_RIGHT] and self.a < self.i_size - 1 and self.nextMove != "V" and [self.a+1,self.b] not in self.list_obstacle:
            self.a += 1
            self.nextMove = "V"
            self.moveNum += 1
        if key[pygame.K_LEFT] and self.a > 0 and self.nextMove != "V" and [self.a-1,self.b] not in self.list_obstacle:
            self.a -= 1
            self.nextMove = "V"
            self.moveNum += 1
        if key[pygame.K_DOWN] and self.b < self.j_size - 1 and self.nextMove != "H" and [self.a, self.b+1] not in self.list_obstacle:
            self.b += 1
            self.nextMove = "H"
            self.moveNum += 1
        if key[pygame.K_UP] and self.b > 0 and self.nextMove != "H" and [self.a,self.b-1] not in self.list_obstacle:
            self.b -= 1
            self.nextMove = "H"
            self.moveNum += 1

        self.player_coordinates = [self.a,self.b]
        self.board[self.a][self.b].color = self.playerColor

        self.player_coordinates = [self.a,self.b]
        if self.player_coordinates == self.meta_coordinates:
            self.player_on_meta = True

    def get_player_on_meta(self):
        return self.player_on_meta

    def end_player(self):
        self.board[self.a][self.b].color = self.p_curedColor #gracz meta
        self.finished_board = True

    def get_finished_board(self):
        return self.finished_board


def main():
    pygame.init()
    window = Window(1200, 960, "Plansza")
    window = pygame.display.set_mode(window.get_sizeWin())

    show_mode=1

    start_a = 0
    start_b = 5

    # rozmiar planszy
    x_size = 7
    y_size = 6

    board = Board(window, start_a, start_b, x_size, y_size)
    start = time.time()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if show_mode<=500:
            window.fill(100,100,100) #instrukcja

        else:
            winow.fill(0,0,0) #board background

            for i in range(x_size):
                for j in range(y_size):
                    board.board[i][j].draw(
                        (board.get_sm()) * i + board.get_margin()+ 610,
                        (board.get_sm()) * j + board.get_margin()+ 150,
                        board.get_sizeSq()
                        )

            board.player()
            if board.get_player_on_meta()==True:
                board.end_player()
                end = time.time()
                game_time = end-start

                if board.get_finished_board() == True:
                    winow.fill(250,250,250) #finish statistic background


        show_mode+=1
        print(show_mode)
        pygame.display.flip()

main()
