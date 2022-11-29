from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def space():
  P = pink
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
def diode():
  P = pink
  O = nothing
  logo = [
  O, O, O, P, P, O, O, O,
  P, P, P, P, P, P, P, P,
  O, O, O, P, P, O, O, O,
  O, O, P, O, O, P, O, O,
  O, P, O, O, O, O, P, O,
  P, P, P, P, P, P, P, P,
  O, O, O, P, P, O, O, O,
  O, O, O, P, P, O, O, O, 
  ]
  return logo

def giveway():
  P = pink
  O = nothing
  logo = [
  P, P, P, O, O, O, O, O,
  P, P, P, P, O, O, O, O,
  P, P, O, P, P, O, O, O,
  P, P, O, O, P, P, O, O,
  P, P, O, O, P, P, P, O,
  P, P, O, P, P, P, O, O,
  P, P, P, P, O, O, O, O,
  P, P, P, O, O, O, O, O,
  ]
  return logo

images = [diode, space, giveway, space]
count = 0

while True:
  s.set_pixels(images[count % len(images)]())
  time.sleep(.75)
  count += 1
