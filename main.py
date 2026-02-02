import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots :
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
                    
                
            
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
    
    

if __name__ == "__main__":
    main()
