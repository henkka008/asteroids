import pygame
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from sys import *
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()

    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for x in asteroids:

            for b in shots:
                if b.collide(x):
                    log_event("asteroid_shot")
                    x.split()
                    b.kill()

            if p1.collide(x) == True:
                log_event("player_hit")
                print("Game over!")
                pygame.quit()
                exit()

        pygame.Surface.fill(screen, (0,0,0))
        for x in drawable:
            x.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000 #fps limit


if __name__ == "__main__":
    main()
    
