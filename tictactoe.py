import pygame
pygame.init()
screen_width = 590
screen_height = 590
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

exit_game = False
image_x=pygame.image.load("x.png")
image_y=pygame.image.load("o.PNG")
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
ch=0
ch_1=0

grid = [
    ['2','3','4'],
    ['5','6','7'],
    ['8','9','10']
]


font = pygame.font.SysFont(None, 45)

def text_screen(text, color):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [225,280])

def display(x,y,ch):

    if ch%2!=0:
        if (20<x<190 and 20<y<190):
            gamewindow.blit(image_x, [40, 40])
            grid[0][0] = 0

        if (210<x<380 and 20<y<190):
            gamewindow.blit(image_x, [230, 40])
            grid[0][1] = 0

        if (400<x<570 and 20<y<190):
            gamewindow.blit(image_x, [420, 40])
            grid[0][2] = 0

        if (20<x<190 and 210<y<380):
            gamewindow.blit(image_x, [40, 230])
            grid[1][0] = 0

        if (210<x<380 and 210<y<380):
            gamewindow.blit(image_x, [230, 230])
            grid[1][1] = 0

        if (400<x<570 and 210<y<380):
            gamewindow.blit(image_x, [420, 230])
            grid[1][2] = 0

        if (20<x<190 and 400<y<570):
            gamewindow.blit(image_x, [40, 420])
            grid[2][0] = 0

        if (210<x<380 and 400<y<570):
            gamewindow.blit(image_x, [230, 420])
            grid[2][1] = 0

        if (400<x<570 and 400<y<570):
            gamewindow.blit(image_x, [420, 420])
            grid[2][2] = 0
        ch_1=1
        winner(ch_1)
        draw(ch, exit_game)


    else:
        if (20 < x < 190 and 20 < y < 190):
            gamewindow.blit(image_y, [40, 40])
            grid[0][0] = 1

        if (210 < x < 380 and 20 < y < 190):
            gamewindow.blit(image_y, [230, 40])
            grid[0][1] = 1

        if (400 < x < 570 and 20 < y < 190):
            gamewindow.blit(image_y, [420, 40])
            grid[0][2] = 1

        if (20 < x < 190 and 210 < y < 380):
            gamewindow.blit(image_y, [40, 230])
            grid[1][0] = 1

        if (210 < x < 380 and 210 < y < 380):
            gamewindow.blit(image_y, [230, 230])
            grid[1][1] = 1

        if (400 < x < 570 and 210 < y < 380):
            gamewindow.blit(image_y, [420, 230])
            grid[1][2] = 1

        if (20 < x < 190 and 400 < y < 570):
            gamewindow.blit(image_y, [40, 420])
            grid[2][0] = 1

        if (210 < x < 380 and 400 < y < 570):
            gamewindow.blit(image_y, [230, 420])
            grid[2][1] = 1

        if (400 < x < 570 and 400 < y < 570):
            gamewindow.blit(image_y, [420, 420])
            grid[2][2] = 1

        ch_1=2
        winner(ch_1)
        draw(ch, exit_game)

def draw(ch, exit_game):
    if ch==9:
        while exit_game != True:
            pygame.draw.rect(gamewindow, white, [0, 260, 590, 70])
            text_screen("!!DRAW!!", green)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
            pygame.display.update()

def winner(ch_1):
    if grid[0][0] == grid[0][1] == grid[0][2] or grid[1][0] == grid[1][1] == grid[1][2] or grid[2][0] == grid[2][1] \
            == grid[2][2] or grid[0][0] == grid[1][0] == grid[2][0] or grid[0][1] == grid[1][1] == grid[2][1] or \
            grid[0][2] == grid[1][2] == grid[2][2] or grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == \
            grid[1][1] == grid[2][0]:
        if ch_1==1:
            win(exit_game, ch_1)

        if ch_1==2:
            win(exit_game, ch_1)

def win(exit_game, ch_1):
    while exit_game!=True:
        pygame.draw.rect(gamewindow, white, [0, 260, 590, 70])
        if ch_1==1:
            text_screen("!!X wins!!", red)

        if ch_1==2:
            text_screen("!!O wins!!", blue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        pygame.display.update()

while exit_game!=True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            ch=ch+1
            (x,y)=pygame.mouse.get_pos()
            display(x,y,ch)

    pygame.draw.rect(gamewindow, green, [0, 0, 20, 590]) #left
    pygame.draw.rect(gamewindow, green, [570, 0, 20, 590]) #right
    pygame.draw.rect(gamewindow, green, [0, 0, 590, 20]) #top
    pygame.draw.rect(gamewindow, green, [0, 570, 590, 20]) #bottom
    pygame.draw.rect(gamewindow, green, [190, 0, 20, 590])
    pygame.draw.rect(gamewindow, green, [380, 0, 20, 590])
    pygame.draw.rect(gamewindow, green, [0, 190, 590, 20])
    pygame.draw.rect(gamewindow, green, [0, 380, 590, 20])

    pygame.display.update()