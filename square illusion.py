import pygame
import random
pygame.init()
import pygame.mixer
pygame.mixer.init()#

pygame.mixer.music.load("music.mp3")#
pygame.mixer.music.play(-1)#

line_color=(255, 0, 0)#
line_width=5#


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))


width = 100
height = 75


GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
PURPLE = (128, 0, 128)
LIME = (0, 255, 0)
NAVY = (0, 0, 128)
OLIVE = (128, 128, 0)
MAROON = (128, 0, 0)
TEAL = (0, 128, 128)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)

COLORS = [GREEN, RED, BLUE, YELLOW, GYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE,
          MAROON, TEAL, SILVER, GOLD]
BACKGROUND_COLORS = [(0,0,0), (255,255,255)]

rects = []


rects.append(pygame.Rect(0,0,width,height))

rects.append(pygame.Rect(0,0,width,height))
rects[-1].topright=(screen_width, 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)

rects.append(pygame.Rect(0,0,width, height))
rects[-1].center=(screen_width//2, screen_height//2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background_color = random.choice(BACKGROUND_COLORS)
    screen.fill(background_color)
    for rect in rects:
        color = random.choice(COLORS)
        pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
    pygame.time.delay(random.randint(700, 800))

pygame.quit()