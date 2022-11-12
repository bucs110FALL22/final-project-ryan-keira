import pygame
class Goal(pygame.sprite.Sprite):
  def __init__(self,x,y,speed):
    self.x = x
    self.y = y
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.speed = speed
  def move_up(self):
    '''
    moves the goal upwards
	  args: none
	  return: goal moved up
    '''  
    self.y += self.speed
  def move_down(self):
    '''
    moves the goal downwards
	  args: none
	  return: goal moved down
    '''  
    self.y += self.speed


"""
Purpose of this class is to control function of the goal. The goal can move up and down. 
x: (int) x-coordinate of goal's position
y: (int) y-coordinate of goal's position
speed: (int) how fast the goal will move
No return
"""