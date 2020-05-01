import pygame
import random
import math
import os
import time
pygame.font.init()

winW = 500
winH = 800

BACKGROUND = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bg.png")))


def draw_win(win):
    win.blit(BACKGROUND, (0, 0))
    pygame.display.update()


def main():
    run = True
    win = pygame.display.set_mode((winW, winH))
    clock = pygame.time.Clock()

    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        draw_window(win)


if __name__ == "__main__":
    main()
