import pygame
from brick_map import *
import brick

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Our First Game")
clock = pygame.time.Clock()

pad_img = pygame.image.load("res/pad.png")
ball_img = pygame.image.load("res/ball.png")
brick_img = pygame.image.load("res/brick.png")
pad_sound = pygame.mixer.Sound("res/TableHit.wav")
brick_sound = pygame.mixer.Sound("res/OpponentHit.wav")

bricks_list = []
game_level = 1
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
bright_green = (100, 255, 100)
red = (255,0,0)
bright_red = (255, 100, 100)

def generate_map(level, brick_width, brick_height):
    map = get_map(level)

    for i in range(len(map[0])):
        for j in range(len(map)):
            if map[j][i] == 1:
                brick_object = brick.brick()
                brick_object._init_(i * brick_width, j * brick_height, brick_img)
                bricks_list.append(brick_object)
                print("Object added at", i, j)

def draw_map():
    for object in bricks_list:
        object.draw_brick(gameDisplay)

def game_won(game_level):
    if len(bricks_list) == 0 :
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text("!!You Won", smallText)
        textRect.center = ((100 + (100 / 2)), (100 + (100 / 2)))
        gameDisplay.blit(textSurf, textRect)
        game_level += 1
        generate_map(game_level, brick_width, brick_height)
        return True


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def pad(x, y):
    if x < 0:
        x = 0
    if x > display_width - pad_img.get_size()[0]:
        x = display_width - pad_img.get_size()[0]
    gameDisplay.blit(pad_img, (x, y))

def ball(ball_x, ball_y):
    gameDisplay.blit(ball_img, (ball_x, ball_y))

def collision_check(pad_x, pad_y, pad_width, pad_height, ball_x, ball_y, ball_width, ball_height):
    inversion_x = False
    inversion_y = False
    pad_horizontal_start = pad_x
    pad_horizontal_end = pad_x + pad_width
    pad_vertical_start = pad_y
    pad_vertical_end = pad_y + pad_height
    ball_horizontal_start = ball_x
    ball_horizontal_centre = ball_x + ball_width/2
    ball_horizontal_end = ball_x + ball_width
    ball_vertical_start = ball_y
    ball_vertical_end = ball_y + ball_height
    ball_vertical_centre = ball_y + ball_height/2

    if (ball_horizontal_centre > pad_horizontal_start and ball_horizontal_centre < pad_horizontal_end) and (ball_vertical_end > pad_vertical_start and ball_vertical_start < pad_vertical_end):
        pad_sound.play()
        inversion_y = True
    if (ball_vertical_centre > pad_vertical_start and ball_vertical_centre < pad_vertical_end) and (ball_horizontal_end > pad_horizontal_start and ball_horizontal_start <= pad_horizontal_end):
        pad_sound.play()
        inversion_x = True
    return (inversion_x, inversion_y)


def text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

brick_width = brick_img.get_size()[0]
brick_height = brick_img.get_size()[1]

generate_map(game_level, brick_width, brick_height)

def game_loop():

    pad_x = display_width * 0.45
    pad_y = display_height * 0.9
    pad_width = pad_img.get_size()[0]
    pad_height = pad_img.get_size()[1]
    ball_width = ball_img.get_size()[0]
    ball_height = ball_img.get_size()[1]

    ball_x = 300
    ball_y = 400
    ball_x_speed = 4
    ball_y_speed = 4
    pad_x_change = 0
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pad_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    pad_x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pad_x_change = 0
                elif event.key == pygame.K_RIGHT:
                    pad_x_change = 0

        pad_x += pad_x_change
        gameDisplay.fill(white)
        collision = collision_check(pad_x, pad_y, pad_width, pad_height, ball_x, ball_y, ball_width, ball_height)

        pad(pad_x, pad_y)
        if ball_x < 0 or ball_x > display_width - ball_width or collision[0]:
            ball_x_speed *= -1
        if ball_y < 0 or collision[1]:
            ball_y_speed *= -1
        if  ball_y > display_height - ball_height:
            game_over = True
        ball_x += ball_x_speed
        ball_y += ball_y_speed
        ball(ball_x, ball_y)
        draw_map()
        for brick_object in bricks_list:

            if brick_object.brick_collision(ball_x, ball_y, ball_width, ball_height)[1]:
                brick_sound.play()
                brick_object.increment_collision_count()
                ball_y_speed *= -1
            elif brick_object.brick_collision(ball_x, ball_y, ball_width, ball_height)[0]:
                brick_sound.play()
                brick_object.increment_collision_count()
                ball_x_speed *= -1

            if brick_object.collision_count > 0:
                bricks_list.remove(brick_object)


        if game_won(game_level):
            ball_x = 300
            ball_y = 400
            pad_x = display_width * 0.45

        #print(event)
        pygame.display.update()
        clock.tick(60)

def start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text("DX Ball", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

start()
