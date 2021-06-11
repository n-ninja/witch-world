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


class Square:
    def __init__(self, win, x, y, col):
        self.win = win
        self.x = x  # x, y współrzędne generowania kwadratu
        self.y = y
        self.color = col

    def draw(self, x, y, size):
        pygame.draw.rect(self.win, self.color, pygame.Rect(x, y, 100, 100))


class Board(Square):
    def __init__(self, win, a, b, i_size, j_size):  # x,y = start_a, start_b
        self.win = win

        self.sizeSq = 100

        self.margin = 10
        self.sm = self.sizeSq + self.margin

        self.a = a  # INDEKS GRACZA
        self.b = b
        self.i_size = i_size
        self.j_size = j_size
        self.board = []
        self.nextMove = ""
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
        # self.block=True

        for i in range(self.i_size):
            p = []
            for j in range(self.j_size):
                # 100 trzeba wywalić jako zmienną
                obj = Square(self.win, i, j, (00, 100, 100))
                p.append(obj)
            self.board.append(p)

    def get_sizeSq(self):
        return self.sizeSq

    def get_margin(self):
        return self.margin

    def get_sm(self):
        return self.sm

    def player(self):
        key = pygame.key.get_pressed()
        self.board[self.a][self.b].color = (00, 100, 100)

        for p in range(len(self.list_obstacle)): #generowanie grafiki przeszkody

            self.block_x=self.list_obstacle[p][0]
            self.block_y=self.list_obstacle[p][-1]

            self.board[self.block_x][self.block_y].color = (0, 0, 0) #self.a i self.b mają być wartościami

            # self.block=(self.a==self.block_x and self.b==self.block_y)
        if key[pygame.K_RIGHT] and self.a < self.i_size - 1 and self.nextMove != "V" and [self.a+1,self.b] not in self.list_obstacle: #self.a+1!=self.block_x:
            self.a += 1
            self.nextMove = "V"

        if key[pygame.K_LEFT] and self.a > 0 and self.nextMove != "V" and [self.a-1,self.b] not in self.list_obstacle: #self.a-1!=self.block_x:
            self.a -= 1
            self.nextMove = "V"

        if key[pygame.K_DOWN] and self.b < self.j_size - 1 and self.nextMove != "H" and [self.a, self.b+1] not in self.list_obstacle: #self.b+1!=self.block_y:
            self.b += 1
            self.nextMove = "H"

        if key[pygame.K_UP] and self.b > 0 and self.nextMove != "H" and [self.a,self.b-1] not in self.list_obstacle: #self.b-1!=self.block_y:
            self.b -= 1
            self.nextMove = "H"

        self.board[self.a][self.b].color = (200, 0, 100)



def main():
    pygame.init()
    window = Window(1000, 1000, "Plansza")
    window = pygame.display.set_mode(window.get_sizeWin())

    # pozycja startowa gracza (TABLICE CZYLI OD 0!)
    # to leci do klasy Board jako x,y, żeby def palyer() działał
    start_a = 0
    start_b = 5

    # rozmiar planszy
    x_size = 7
    y_size = 6

    board = Board(window, start_a, start_b, x_size, y_size)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((0, 0, 0))
        for i in range(x_size):
            for j in range(y_size):
                # przerwa musi byc wieksza niz rozmiar kwadratu!!!
                board.board[i][j].draw(
                    (board.get_sm()) * i + board.get_margin(),
                    (board.get_sm()) * j + board.get_margin(),
                    board.get_sizeSq()
                    )
        board.player()
        pygame.display.update()


main()
