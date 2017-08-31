import sys, pygame
import random

BLUE = (0, 0, 200)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
block_list = pygame.sprite.Group()

#Initialize
pygame.init()
size = screen_width, screen_height = 800,450
screen = pygame.display.set_mode(size)


#StartGame


for i in range(50):
    block = Block(BLUE, 25, 25)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(WHITE)
    block_list.draw(screen)
    #for block in block_list:

pygame.quit()
    