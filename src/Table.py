import pygame
class Table(pygame.sprite.Sprite):
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
  def getxcoord(self):
    '''
    gets the current x coordinate of the table
	  args: none
	  return: x coord of table
    '''  
    return self.x
  def getycoord(self):
    '''
    gets the current y coordinate of the table
	  args: none
	  return: y coord of table
    '''  
    return self.y

'''
This class creates the table.
x: (int) x-coordinate of table
y: (int) y-coordinate of table
No return
'''