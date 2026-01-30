import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_x_initial = SCREEN_WIDTH / 2
    player_y_initial = SCREEN_HEIGHT / 2
    p = Player(player_x_initial, player_y_initial)
    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000
        p.draw(screen)
        
        pygame.display.flip()
    
    

if __name__ == "__main__":
    main()
