import pygame
import sys
import time
from src.Puck import Puck
from src.Striker import Striker

black=(0,0,0)
white=(255,255,255)
startcoord = 0

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Air Hockey Game!")
screensize = (400,200)
screen = pygame.display.set_mode(screensize)

striker1_img = "/home/runner/final-project-ryan-keira/assets/striker1.png"
striker2_img = "/home/runner/final-project-ryan-keira/assets/striker2.png"

class Controller:
  
  def __init__(self, puckspeed, strikerspeed):
    self.puckspeed = puckspeed
    self.strikerspeed = strikerspeed
    self.state = "BEGIN"
    self.striker1score = 0
    self.striker2score = 0
    self.font = pygame.font.SysFont("Times New Roman",14)

  def gameOver(self):
    pygame.quit()
    sys.exit()

  """
  This function quits the program
  No input
  No return
"""

  def loadbg(self): #Table Setup
    bg1 = pygame.image.load("/home/runner/final-project-ryan-keira/assets/table.png")
    self.bg = pygame.transform.scale(bg1, (screensize)) 
    
  """
  This function loads the background onto the output screen
  No input
  No return
"""
    
  def loadstriker1(self,x,y): #Striker 1 Setup
    self.striker1 = Striker(striker1_img,x,y,self.strikerspeed,(screensize[0]//2,screensize[1]),(0,0))
    self.striker1_group = pygame.sprite.Group()
    self.striker1_group.add(self.striker1)

  """
  This function loads Striker1 onto the output screen
  x: (int) x-coordinate of Striker1
  y: (int) y-coordinate of Striker1
  No return
"""
      
  def loadstriker2(self,x,y): #Striker 2 Setup
    self.striker2 = Striker(striker2_img,x,y,self.strikerspeed,(screensize[0]//2,screensize[1]),(screensize[0]//2,0))
    self.striker2_group = pygame.sprite.Group()
    self.striker2_group.add(self.striker2)

  """
  This function loads Striker2 onto the output screen
  x: (int) x-coordinate of Striker2
  y: (int) y-coordinate of Striker2
  No return
"""
      
  def loadpuck(self,x,y): #Puck Setup
    self.puck = Puck(x,y,self.puckspeed,screensize,(0,0))
    self.puck_group = pygame.sprite.Group()
    self.puck_group.add(self.puck)

  """
  This function loads the puck image onto the output screen
  x: (int) x-coordinate of the puck
  y: (int) y-coordinate of the puck
  No return
"""

  def gamePlay(self):
    self.loadbg() 
    self.gameReset()
    while True:
      screen.blit(self.bg, (startcoord,startcoord))
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          pygame.quit()
          sys.exit()
      if self.gameLogic():
        self.gameReset()
        if self.striker2score > 2:
          print("PLAYER 2 WINS")
          screen.fill('black')
          pygame.display.flip()
          time.sleep(1)
          self.state = "QUIT"
          return
        if self.striker1score > 2:
          print("PLAYER 1 WINS")
          screen.fill('black')
          pygame.display.flip()
          time.sleep(1)
          self.state = "QUIT"
          return
      self.striker1_group.draw(screen)
      self.striker2_group.draw(screen)
      self.puck_group.draw(screen)
      clock.tick(60)
      pygame.display.flip()

    """
This function loads the background and sets inital position for Striker 1, Striker2, and the puck and puts them at their respective coordinates.
No args
No return
"""

  def gameReset(self):
    self.loadstriker1(screensize[0]*1/5,screensize[1]*4/10)
    self.loadstriker2(screensize[0]*7/10,screensize[1]*4/10)
    self.loadpuck(screensize[0]*141/320,screensize[1]*15/40)

  """
This function rests the game and puts the sprits back to their respective positions
No inputs
No return
"""

  def mainLoop(self):
    while True:
      if self.state == "BEGIN":
        msg2 = ["Player 1 will use the keypad", "to control their striker and the", "other player will use wasd.", "First to 3 wins.", "Press space to begin!"]
        screen.fill('black')
        for i,m in enumerate(msg2):
            msg = self.font.render(m,False,'white')
            screen.blit(msg,(10,10+i*30))
        pygame.display.update()
        #print(msg2)
        self.gameLoop()
      elif self.state == "GAME":
        self.gamePlay()
      elif self.state == "QUIT": 
         self.gameOver()
  """
This function prints message2 onto output screen
No inputs
Returns message on output screen
"""
    

  def gameLoop(self):
    while True:
       for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              self.state = "GAME"
              return
            #self.mainLoop()
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

  """
This function allows for use of keys if game is not over.
No inputs
No returns
"""
#Players can use arrows and WASD keys to control their strikers. 
  def gameLogic(self): 
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
          self.striker1.move_left()
      elif keys[pygame.K_d]:
          self.striker1.move_right()
      elif keys[pygame.K_w]:
          self.striker1.move_up()
      elif keys[pygame.K_s]:
          self.striker1.move_down()
      elif keys[pygame.K_LEFT]:
          self.striker2.move_left()
      elif keys[pygame.K_RIGHT]:
          self.striker2.move_right()
      elif keys[pygame.K_UP]:
          self.striker2.move_up()
      elif keys[pygame.K_DOWN]:
          self.striker2.move_down()

      if self.puck_collide(self.puck,self.striker1):
        self.puck.vector = self.new_direction(self.puck,self.striker1)
    
      if self.puck_collide(self.puck,self.striker2):
        self.puck.vector = self.new_direction(self.puck,self.striker2)

        
        #Scoring
      if self.puck.rect.left <= 0 and screensize[1]*1/5<self.puck.rect.y<screensize[1]*11/20:
        self.striker2score += 1
        return True
      if self.puck.rect.right >= screensize[0] and screensize[1]*1/5<self.puck.rect.y<screensize[1]*11/20:
        self.striker1score += 1
        return True

      self.puck.update()

  """
This function alllows for use of arrow keys and w,s,a,d keys to move strikers. Allows sets parametrs when the puck hits either striker. Also uses puck's position for tracking score.
No input
No return
  """

  def puck_collide(self,puck,player):
    puck_radius = puck.rect.width/2
    player_radius = player.rect.width/2
  
    puck_center = puck.rect.center
    player_center = player.rect.center
  
    if (puck_center[0]-player_center[0])**2+(puck_center[1]-player_center[1])**2 <= (puck_radius+player_radius)**2:
      return True
  
    return False

  """
This function uses the puck's radius and its center coordinates to account for when it is hit by the strikers.
puck_radius: (int) radius of the puck
player_radius: (int) radius of striker
returns True if puck is hit by striker. returns False if it is not hit.
"""

  def new_direction(self,puck,player):
    puck_center = puck.rect.center
    player_center = player.rect.center
    
    x_new = puck_center[0]-player_center[0]
    y_new = puck_center[1]-player_center[1]
    vec_norm = (x_new**2+y_new**2)**.5
    
    return (x_new/vec_norm,y_new/vec_norm)


"""
This function makes sure that when the puck is indeed hit, it changes direction.
puck_center: (int) center of puck
player_center: (int) center of striker
Returns the new x and y coordinate of the hit puck
"""
