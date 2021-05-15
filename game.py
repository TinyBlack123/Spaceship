from tkinter import *
import time
import random


tk=Tk()
width=800
heigh=600
tk.title("Spaceship")
screenwidth = tk.winfo_screenwidth()
screenheight = tk.winfo_screenheight()
tk.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
canvas=Canvas(tk,width=800,height=600,bg="skyblue",bd=0,highlightthickness = 0)
tk.resizable(0,0)
canvas.pack()
tk.update()
class Ball:
  def __init__(self,canvas,paddle,color):
    self.canvas=canvas
    self.paddle=paddle
    self.id=canvas.create_oval(10,10,25,25,fill=color)
    self.canvas.move(self.id,240,100)
    stat=[-3,-2,-1,1,2,3]
    random.shuffle(stat)
    self.x=stat[0]
    self.y=-3
    self.canvas_height=self.canvas.winfo_height()
    self.canvas_width=self.canvas.winfo_width()
    self.hit_ship = False
  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id )
    if pos[2]>= paddle_pos[0] and pos[0]<= paddle_pos[2]:
      if pos[3]>= paddle_pos[1] and pos[3]<= paddle_pos[3]:
        return True
    return False
  def draw(self):
    self.canvas.move(self.id,self.x,self.y)
    pos=self.canvas.coords(self.id)
    if pos[1]<=0:
      dire = [1, 2, 3]
      random.shuffle(dire)
      self.y=dire[0]
    if pos[3]>=self.canvas_height:
      dire = [-1, -2, -3]
      random.shuffle(dire)
      self.y = dire[0]
    if self.hit_paddle(pos)==True:
      self.hit_ship = True
    if pos[0]<=0:
      dire = [1, 2, 3]
      random.shuffle(dire)
      self.x=dire[0]
    if pos[2]>=self.canvas_width:
      dire = [-1, -2, -3]
      random.shuffle(dire)
      self.x=dire[0]
class Ship:
  def __init__(self,canvans,color):
    self.canvas=canvas
    self.id=canvas.create_rectangle(0,0,50,50,fill=color)
    self.canvas.move(self.id,400,450)
    self.x=0
    self.canvas_width=self.canvas.winfo_width()
    self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
    self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
  def turn_left(self,event):
    self.x=-5
  def turn_right(self,event):
    self.x=5
  def draw(self):
    pos=self.canvas.coords(self.id)
    self.canvas.move(self.id, self.x, 0)
    if pos[0]<=0:
      self.x=0
    if pos[2]>=self.canvas_width:
      self.x=0
Ship=Ship(canvas,"blue")
balls = [Ball(canvas,Ship,"black") for i in range(6)]
time_start = time.time()
while True:
  time_survive = time.time()-time_start
  for ball in balls:
    if ball.hit_ship == True:
      tk.destroy()
      tk = Tk()
      tk.title("Spaceship")
      tk.geometry('%dx%d+%d+%d' % (width, heigh, (screenwidth - width) / 2, (screenheight - heigh) / 2))
      w = Label(tk, text="Game Over! You Survive " + str('%d' % time_survive) + 's')
      w.pack()
      tk.update()
      break
  for ball in balls:
    ball.draw()
  Ship.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)
