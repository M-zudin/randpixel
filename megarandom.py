from random import randint as rand
import pygame
from time import sleep
pygame.init()
w=int(input('Ширина: '))
h=int(input('Высота: '))
if w*h>62500:
    disp=False
    print('Из-за большого размера показ в реальном времени выключен')
else:
    disp=True
screen = pygame.display.set_mode([w,h])
print('Генерация...')
for x in range(0,w):
    for y in range(0,h):
        pygame.draw.rect(screen,(rand(0,255),rand(0,255),rand(0,255)),[x,y,x,y])
        if disp:
            pygame.display.update()
print('Генерация завершена')
pygame.display.update()
while True:
    pass
