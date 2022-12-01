import pygame
class Puck(pygame.sprite.Sprite):
  def __init__(self,x,y,speed):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/puck.png")
    self.rect = self.image.get_rect()
    self.speed = speed
  def move_right(self):
    '''
    moves the puck to the right
	  args: none
	  return: puck moved to the right
    '''  
    self.x += self.speed
  def move_left(self):
    '''
    moves the puck to the left
	  args: none
	  return: puck moved to the left
    '''  
    self.x -= self.speed
  def move_up(self):
    '''
    moves the puck upwards
	  args: none
	  return: puck moved up
    '''  
    self.y += self.speed
  def move_down(self):
    '''
    moves the puck downwards
	  args: none
	  return: puck moved down
    '''  
    self.y -= self.speed

"""
Purpose of this class is to control function of the puck. The puck will move left, right, up, and down. Its movements will depend upon the actions of the two players.
x: (int) x-coordinate of puck's position
y: (int) y-coordinate of puck's position
speed: (int) how fast the puck moves
No return
"""