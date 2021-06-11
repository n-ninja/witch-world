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
    def __init__(self,win,x,y,size,col):
        self.win = win
        self.x = x
        self.y = y
        self.size=size
        self.color = col

    def draw(self,x,y,size):
        pygame.draw.rect(self.win, self.color, pygame.Rect(x,y,size,size))

class Board(Square):
    def __init__(self,win,x,y,x_size,y_size):
        #Square.__init__(win, x, y, size), czy da się tak zrobić?
        self.win = win
        self.x=x #czy tego nie można dziedziczyć?
        self.y=y
        self.x_size=x_size
        self.y_size = y_size
        self.board=[]
        self.nextMove=""
        for i in range(self.x_size):
            p=[]
            for j in range(self.y_size):
                obj=Square(self.win,i,j,100,(00,100,100))
                p.append(obj)
            self.board.append(p)
        self.board[x][y].color=(0,0,100) #co to za y i x

    def player(self):
        key = pygame.key.get_pressed()
        self.board[self.x][self.y].color=(00,100,100)
        if key[pygame.K_RIGHT] and self.x<self.x_size-1 and self.nextMove!="V":
            self.x+=1
            self.nextMove="V"

        if key[pygame.K_LEFT] and self.x>0 and self.nextMove!="V":
            self.x-=1
            self.nextMove="V"

        if key[pygame.K_UP] and self.y>0 and self.nextMove!="H":
            self.y-=1
            self.nextMove="H"

        if key[pygame.K_DOWN] and self.y<self.y_size-1 and self.nextMove!="H":
            self.y+=1
            self.nextMove="H"
        self.board[self.x][self.y].color=(200,0,100)


def main():
    pygame.init()
    window = Window(1000,1000,"Plansza")
    window = pygame.display.set_mode(window.get_sizeWin())

    #pozycja startowa gracza
    start_x = 0
    start_y = 0

    #rozmiar planszy
    x_size = 7
    y_size = 6

    sizeSq=100
    margin=10
    board_size=sizeSq+margin

    board = Board(window,start_x,start_y,x_size,y_size)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((0,0,0))
        for i in range(x_size):
            for j in range(y_size):
                board.board[i][j].draw((board_size)*i+margin,(board_size)*j+margin,sizeSq) #przerwa musi byc wieksza niz rozmiar kwadratu!!!
        board.player()
        pygame.display.update()

main()
