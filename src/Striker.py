import pygame

screen = pygame.display.set_mode((800, 600))

class Striker(pygame.sprite.Sprite):
  def __init__(self,image,x,y,speed,dimensions,pos):
    super().__init__()
    self.image = pygame.image.load(image)
    default_image_size = (40, 40) #setting default size of striker 1 
    self.image = pygame.transform.scale(self.image, default_image_size) #scaling image of striker 1
    self.rect = self.image.get_rect()
    self.speed = speed
    self.rect.x = x
    self.rect.y = y
    self.board_width = dimensions[0]
    self.board_height = dimensions[1]
    self.pos = pos

  def adjust_position(self):
    '''
    creates vectors for the strikers
	  args: none
	  return: none
    '''  
    puck_width = self.rect.w
    x_min_plane = self.pos[0]
    x_max_plane = self.pos[0]+self.board_width-puck_width
    y_min_plane = self.pos[1]
    y_max_plane = self.pos[1]+self.board_height-puck_width

    if x_min_plane > self.rect.x:
      self.rect.x = x_min_plane
    if y_min_plane > self.rect.y:
      self.rect.y = y_min_plane

    if x_max_plane < self.rect.x:
      self.rect.x = x_max_plane
    if y_max_plane < self.rect.y:
      self.rect.y = y_max_plane   

  
  def move_right(self):
    '''
    moves the striker to the right
	  args: none
	  return: none
    '''  
    self.rect.x += self.speed
    self.adjust_position()
  
  def move_left(self):
    '''
    moves the striker to the left
	  args: none
	  return: none
    '''  
    self.rect.x -= self.speed
    self.adjust_position()
  
  def move_up(self):
    '''
    moves the striker upwards
	  args: none
	  return: none
    '''  
    self.rect.y -= self.speed
    self.adjust_position()
  
  def move_down(self):
    '''
    moves the striker downwards
	  args: none
	  return: none
    '''  
    self.rect.y += self.speed
    self.adjust_position()

screen.blit(screen, (0,0))
