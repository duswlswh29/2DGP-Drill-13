from pico2d import *
import game_world
import common

class Ball:
  image=None

  def __init__(self,x=None,y=None):
     if Ball.image is None:
         Ball.image=load_image('ball21x21.png')
     self.x=x
     self.y=y

  def update(self):
       pass


  def draw(self):
    sx = self.x - common.court.window_left
    sy = self.y - common.court.window_bottom
    self.image.draw(sx,sy)
