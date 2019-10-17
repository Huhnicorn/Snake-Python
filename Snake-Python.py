from gturtle import *

LEFT = 37
RIGHT = 39
UP = 38
DOWN = 40

def onKeyPressed(key):
   if key == LEFT:
      setHeading(-90)
   elif key == RIGHT:
      setHeading(90)
   elif key == UP:
      setHeading(0)
   elif key == DOWN:
      setHeading(180)

makeTurtle(keyPressed = onKeyPressed)
setPenColor("black")
setPenWidth(3)


    
wrap()
while True:
    forward(3)
    if getPixelColorStr == "black":    
        setPenColor("red")