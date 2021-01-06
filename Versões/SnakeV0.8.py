## Imports ##
import random
import pygame
from pygame import *
from tkinter import *

## Spawn aleatório da Apple ##
def on_grid_random():
    x = (random.randint(0,570))
    y = (random.randint(60,570))
    return (x//10 * 10, y//10 * 10)

## Colisão ##
def collision(cl1, cl2):
    return (cl1[0]) == cl2[0] and (cl1[1] == cl2[1])

## Sistema de Pause ##
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)

## Declaração do Score ##
score = 0
scoreN = 0

## Declaração dos comandos ##
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

## Screen ##
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

## Snake ##
snake = [(200,200), (210,200), (220,200)]
snake_head = snake[(0)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

## Apple ##
apple = pygame.Surface((10,10))
apple_pos = on_grid_random()
apple.fill((255,0,0))

## Starter Direction ##
my_direction = LEFT

clock = pygame.time.Clock()

running = True

while running:
    ## Velocidade do Jogo(FPS) ##
    clock.tick(10)

    ## HUD ##
    font = pygame.font.SysFont('arial black',20)
    position1 = font.render('',True,(0, 0, 0),(0,0,0))
    position_pos1 = position1.get_rect()
    position_pos1.center = (5, 25)

    ## Score(HUD) ##
    font = pygame.font.SysFont('arial black',20)
    text = font.render('Score: {}'.format(score),True,(255,255,255),(0,0,0))
    text_pos = text.get_rect()
    text_pos.center = (50,15)

    
    ## Teclas(Controles) ##
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                my_direction = DOWN
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                my_direction = RIGHT
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                my_direction = LEFT

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pause()

         
    ## Colisão com a Maçã ##            
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score  = score + 1
  
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    ## Directions ##
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    screen.blit(text, text_pos) 
    
    for pos in snake:
        screen.blit(snake_skin, pos)

    ## Position(HUD) ##
    font = pygame.font.SysFont('arial black',20)
    position = font.render('Position: {}'.format(pos),True,(255,255,255),(0,0,0))
    position_pos = position.get_rect()
    position_pos.center = (0, 0)

    screen.blit(position, position_pos.fit(position_pos1))

    ## Colisão com a Parede ##
    if pos[0] == 590:
        print('Traumatismo uCraniano!') #Direita
        exit()

    if pos[0] == 0:
        print('Traumatismo uCraniano!') #Esquerda
        exit()

    if pos[1] == 590:
        print('Traumatismo uCraniano!') #Embaixo
        exit()

    if pos[1] == 0:
        print('Traumatismo uCraniano!') #Emcima
        exit()

    pygame.display.update()
