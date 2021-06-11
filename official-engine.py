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
        pygame.draw.rect(self.win, self.color, pygame.Rect(x, y, 100, 100))


class Board(Square):
    def __init__(self, win, a, b, i_size, j_size):  # x,y = start_a, start_b
        self.win = win

        self.sizeSq = 100
        self.margin = 10
        self.sm = self.sizeSq + self.margin
        self.moveNum = 0
        self.a = a  # INDEKS GRACZA
        self.b = b
        self.i_size = i_size
        self.j_size = j_size
        self.board = []
        self.nextMove = ""
        self.list_obstacle = [
            [0, 3],
            [1, 0],
            [2, 0],
            [2, 5],
            [3, 2],
            [4, 2],
            [5, 4],
            [6, 0],
        ]
        self.player_coordinates = [[self.a], [self.b]]
        self.meta_coordinates = [6, 1]
        self.player_on_meta = False
        self.close_win = False
        self.finished_board = False

        for i in range(self.i_size):
            p = []
            for j in range(self.j_size):
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
        self.board[self.meta_coordinates[0]
                   ][self.meta_coordinates[-1]].color = (250, 250, 250)

        for p in range(len(self.list_obstacle)):

            self.block_x = self.list_obstacle[p][0]
            self.block_y = self.list_obstacle[p][-1]
            self.board[self.block_x][self.block_y].color = (0, 0, 0)
        if key[pygame.K_RIGHT] and self.a < self.i_size - 1 and self.nextMove != "V" and [self.a + 1, self.b] not in self.list_obstacle:
            self.a += 1
            self.nextMove = "V"
            self.moveNum += 1
        if key[pygame.K_LEFT] and self.a > 0 and self.nextMove != "V" and [self.a - 1, self.b] not in self.list_obstacle:
            self.a -= 1
            self.nextMove = "V"
            self.moveNum += 1
        if key[pygame.K_DOWN] and self.b < self.j_size - 1 and self.nextMove != "H" and [self.a, self.b + 1] not in self.list_obstacle:
            self.b += 1
            self.nextMove = "H"
            self.moveNum += 1
        if key[pygame.K_UP] and self.b > 0 and self.nextMove != "H" and [self.a, self.b - 1] not in self.list_obstacle:
            self.b -= 1
            self.nextMove = "H"
            self.moveNum += 1

        self.player_coordinates = [self.a, self.b]
        self.board[self.a][self.b].color = (200, 0, 100)

        self.player_coordinates = [self.a, self.b]
        if self.player_coordinates == self.meta_coordinates:
            self.player_on_meta = True

    def get_player_on_meta(self):
        return self.player_on_meta

    def end_player(self):
        self.board[self.a][self.b].color = (0, 0, 100)  # gracz meta
        self.close_win = True
        self.finished_board = True

    def get_finished_board(self):
        return self.finished_board

    def get_close_win(self):
        return self.close_win

def show_text():
    print("\nZa siedmioma górami, za siedmioma lasami.\nW krainie wypełnionej z baśni postaciami:\nKsiążęta, królewny, smoki i wróżki,\nzłe stwory i wiedźma w ciele staruszki.\n")
    print("Czas płynie przyjemnie w tym miejscu czarownym\ndopóty dopóki zło równa się z dobrym.\nLecz niebo się chmurzy, nadchodzi zagłada.\nWirus nadciąga z obcego nam świata.\n")
    print("Posłuchaj wędrowcze, w potrzebie dopomóż\nŚpiesz się, gdyż wkrótce nie bedzie już komu.\nZ innego wymiaru zaraza doskwiera\nJedyna nadzieja w miksturze Pfizera!\n")
    print("By znaleźć lekarstwo, pokonaj labirynt\nCiemności unikaj, tam mroczne są siły.\nStrzeż się uroku, bo z nikąd ratunku\ngdy pójdziesz dwa razy w tym samym kierunku!\n")
    print("Jeśli jesteś gotów do drogi, naciśnij \"x\", a następnie kliknij w planszę.")



def main():
    show_text()
    ready=input()
    if ready=="x":
        pygame.init()
    window = Window(1000, 1000, "Plansza")
    window = pygame.display.set_mode(window.get_sizeWin())

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
                end = time.time()
                game_time = end - start
                print("Twoja podróż trwała ", round(game_time,2), "sekundy")
                print("Wykonałeś: ", board.moveNum, "siedmiomilowych kroków")
               

        window.fill((0, 0, 0))
        for i in range(x_size):
            for j in range(y_size):
                board.board[i][j].draw(
                    (board.get_sm()) * i + board.get_margin(),
                    (board.get_sm()) * j + board.get_margin(),
                    board.get_sizeSq()
                )

        board.player()
        if board.get_player_on_meta() == True:
            board.end_player()

            if board.get_finished_board() == True:
                window.fill((250, 250, 250))
                font1 = pygame.font.SysFont('Courier-New.ttf', 60)
                text1 = font1.render('The end - zajrzyj do konsoli', True, (0, 0, 0))
                window.blit(text1, (200,400))

        pygame.display.update()

main()
