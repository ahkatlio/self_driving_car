from asyncio import windows_events
import pygame
from pygame import *
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load("road.png")
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (50,50))
car_x = 150
car_y  = 300
cam_x_offset = 0
cam_y_offset = 0
clock = pygame.time.Clock()
terget_distance = 25
direction = 'up'
drive = True
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - terget_distance))[0]
    down_px = window.get_at((cam_x, cam_y + terget_distance))[0]
    right_px = window.get_at((cam_x + terget_distance, cam_y))[0]
    print(up_px, right_px, down_px )
    #turn
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and  down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_y_offset = 0
        cam_x_offset = 30
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction= 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    #drive
    if direction == 'up' and up_px == 255:
        car_y = car_y-2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 50)
    
    window.blit(track, (0,0))
    window.blit(car, (car_x, car_y))
    pygame.display.update()