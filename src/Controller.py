import pygame


class Controller:
  
  def __init__(self, fontsize, goalheight, goalwidth, screensize, puckspeed, strikerspeed):
    pygame.init()
    white = (255,255,255)
    black = (0,0,0)
    self.screen = pygame.display.set_mode(screensize)
    self.divline1 = screen.get_width()/2, 0
    self.divline2 = screen.get_width()/2 ,screen.get_height()
    self.goalheight=goalheight
    self.goalwidth=goalwidth
    self.goal1 = pygame.Rect(0,screen.get_height()/2 - 50,10,100)
    self.goal2 = pygame.Rect(screen.get_width()-10,screen.get_height()/2-goalheight,10,100)
    self.striker1=pygame.Rect(screen.get_width()/2-200,screen.get_height()/2,20,20)
    self.striker2= pygame.Rect(screen.get_width()/2+200,screen.get_height()/2,20,20)
    self.strikerspeed=strikerspeed
    self.puck=pygame.Rect(screen.get_width()/2,screen.get_height()/2,20,20)
    self.puckspeed=puckspeed
    self.img = pygame.image.load('assets/puck.png')
    self.greenstriker = pygame.image.load('assets/striker1.png')
    self.bluestriker = pygame.image.load('assets/striker2.png')
    self.score1=0
    self.score2=0
    self.font = pygame.font.SysFont("calibri" , fontsize)

  def setup(self):
    pygame.display.set_caption('First to 5 wins')
    screen.fill(black)
    white = (255,255,255)
    black = (0,0,0)
    pygame.draw.rect(self.screen, (255,100,100), self.striker1)
    pygame.draw.rect(self.screen, (20,20,100), self.striker2)
    pygame.draw.rect(self.screen,white,self.goal1)
    pygame.draw.rect(self.screen,white,self.goal2)
    screen.blit(self.img,(self.puck.x,self.puck.y))   
    screen.blit(self.greenstriker,(self.striker1.x-5,self.striker1.y-5))
    screen.blit(self.bluestriker,(self.striker2.x-5,self.striker2.y-5))
    pygame.draw.circle(self.screen, white , (self.screen.get_width()/2, self.screen.get_height()/2), self.screen.get_width()/10,5)
    pygame.draw.line(self.screen, white, self.divline1, self.divline2,5 )
    pygame.draw.line(self.screen, white, (0,0), (self.screen.get_width()/2 - 5,0) ,5)
    pygame.draw.line(self.screen, white,(0,self.screen.get_height()), (self.screen.get_width()/2 - 5,self.screen.get_height()) ,5)
    pygame.draw.line(self.screen, white, (self.screen.get_width()/2+5,0), (screen.get_width() ,0) ,5)
    pygame.draw.line(self.screen, white, (self.screen.get_width()/2 + 5,self.screen.get_height()) , (self.screen.get_width(),self.screen.get_height()) ,5)
    pygame.draw.line(self.screen, white, (0,0), (0,self.screen.get_height()/2-goalheight) ,5)
    pygame.draw.line(self.screen, white, (0,self.screen.get_height()/2 + self.goalheight), (0,self.screen.get_height()) ,5)
    pygame.draw.line(self.screen, white, (self.screen.get_width(),0), (self.screen.get_width(),self.screen.get_height()/2-self.goalheight) ,5)
    pygame.draw.line(self.screen, white, (self.screen.get_width(),self.screen.get_height()/2 + self.goalheight), (self.screen.get_width(),self.screen.get_height()) ,5)
    pygame.display.update()
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
