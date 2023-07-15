import pygame as pg
import sys

HEIGHT = 780
WIDTH = 345

RES = HEIGHT, WIDTH

pg.display.set_mode([RES] * 5)
pg.display.set_caption("A Custom Project")

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
