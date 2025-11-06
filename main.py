import pygame
from constants import *
from logger import log_state
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        for x in drawable:
            x.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000 #fps limit


if __name__ == "__main__":
    main()
    
