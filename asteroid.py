from circleshape import CircleShape    
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        pass

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
        pass    
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        pass
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        else :
            log_event("asteroid_split")
            angule = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = self.velocity.rotate(angule)
            new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid1.velocity= angle * 2
            new_asteroid2.velocity = (angle * -1) * 2
            
            
            
            
            
            
            
    
