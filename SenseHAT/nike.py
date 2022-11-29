from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True
blue = (0, 0, 255)
white = (255,255,255)

def b():
  B = blue
  O = white
  logo = [
  O, O, O, O, O, O, O, B,
  O, O, O, O, O, O, B, B,
  O, O, O, O, O, B, B, B,
  B, O, O, O, B, B, B, O,
  B, B, O, B, B, B, O, O,
  B, B, B, B, B, O, O, O,
  O, B, B, B, O, O, O, O,
  O, O, B, O, O, O, O, O,
  ]
  return logo
  
images = [b]
count = 0

while True:
  s.set_pixels(images[count % len(images)]())
  time.sleep(.75)
  count +=1
