import time

from sense_hat import SenseHat
sense = SenseHat()

off = [[0,0,0]] * 64
red = [[255,0,0]] * 64
green = [[0,255,0]] * 64
blue = [[0,0,255]] * 64
yellow = [[255,255,0]] * 64
orange = [[255,140,0]] * 64
purple = [[147,112,219]] * 64
cyan = [[0,255,255]] * 64
magenta = [[255,0,255]] * 64
on = [[255,255,255]] * 64

senseColors = { 'off' : off }
senseColors['r'] = red
senseColors['g'] = green
senseColors['b'] = blue
senseColors['y'] = yellow
senseColors['o'] = orange
senseColors['p'] = purple
senseColors['c'] = cyan
senseColors['m'] = magenta
senseColors['on'] = on

def lightColorList ( colorList ):
   for color in colorList:
      sense.set_pixels(senseColors[color])
      time.sleep(1)
   sense.set_pixels(senseColors['off'])
   return
