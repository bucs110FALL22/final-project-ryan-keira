import pygame

screen = pygame.display.set_mode((800, 600))

class Puck(pygame.sprite.Sprite):
  def __init__(self,x,y,speed,dimensions,pos):
    super().__init__()
    self.image = pygame.image.load("/home/runner/final-project-ryan-keira/assets/puck.png")
    default_image_size = (50, 50) #setting defualt size of puck
    self.image = pygame.transform.scale(self.image, default_image_size) #scaling image of puck
    self.rect = self.image.get_rect()
    self.speed = speed
    self.rect.x = x
    self.rect.y = y
    self.vector = (0,0)
    self.board_width = dimensions[0]
    self.board_height = dimensions[1]
    self.pos = pos
  def adjust_position(self):
    '''
    creates vectors for the puck
	  args: none
	  return: none
    '''  
    x_min_plane = self.pos[0]
    x_max_plane = self.pos[0]+self.board_width
    y_min_plane = self.pos[1]
    y_max_plane = self.pos[1]+self.board_height

    if x_min_plane > self.rect.left or x_max_plane < self.rect.right:
      self.vector = (-self.vector[0],self.vector[1])
    if y_min_plane > self.rect.top or y_max_plane < self.rect.bottom:
      self.vector = (self.vector[0],-self.vector[1])
  
  def move_right(self):
    '''
    moves the puck to the right
	  args: none
	  return: none
    '''  
    self.rect.x += self.speed
  def move_left(self):
    '''
    moves the puck to the left
	  args: none
	  return: none
    '''  
    self.rect.x -= self.speed
  def move_up(self):
    '''
    moves the puck upwards
	  args: none
	  return: none
    '''  
    self.rect.y += self.speed
  def move_down(self):
    '''
    moves the puck downwards
	  args: none
	  return: none
    '''  
    self.rect.y -= self.speed

  def update(self):
    '''
    changes x and y values based on vectors
	  args: none
	  return: none
    '''  
    x = self.vector[0]*self.speed
    y = self.vector[1]*self.speed

    self.rect.x+=x
    self.rect.y+=y

    self.adjust_position()
  

screen.blit(screen, (0,0))

 