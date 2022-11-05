Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Puck:
  def __init__(self,x,y,image):
    self.x = x
    self.y = y
    self.image = puck_image
  def move_right(self,amount):
    self.x = self.x + amount
  def move_left(self,amount):
    self.x = self.x - amount
  def move_up(self,amount):
    self.y = self.y + amount
  def move_down(self,amount):
    self.y = self.y - amount

## Class Interface 2

class Goal:
  def __init__(self,x,y,goal_image):
    self.x = x
    self.y = y
    self.image = goal_image
  def move_up(self,amount):
    self.y = self.y + amount
  def move_down(self,amount):
    self.y = self.y - amount

## Class Interface 3

class Table:
  def __init__(self,x,y,table_image):
    self.x = x
    self.y = y
    self.image = table_image
  def vanish(self,transparent_image):
    self.image = transparent_image
  
