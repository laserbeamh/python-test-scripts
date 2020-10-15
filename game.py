#!/usr/bin/env python3
import pygame
from math import pi
import random

# Init pygame engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
BROWN	 = ( 165,  42,  42)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

# Set screen size and launch
size = (700, 500)
screen = pygame.display.set_mode(size)
width, height = pygame.display.get_surface().get_size()

# Set window title
pygame.display.set_caption("Buddy's First Snowglobe")

# Manage screen update screen
clock = pygame.time.Clock()

# ----- Trees -----
def draw_tree():
  for x_offset in range(0, 675, 100):
    pygame.draw.polygon(screen, [41,117,47], [[135+x_offset, 375], [75+x_offset, 275], [15+x_offset, 375]])
    pygame.draw.polygon(screen, [41,117,47], [[145+x_offset, 424], [75+x_offset, 300], [5+x_offset, 424]])
    pygame.draw.rect(screen, BROWN, [60+x_offset, 425, 30, 100])
    
# --- Tree lights --- 
green_light_list = []    
for i in range(100):
  x = random.randrange(5, 145)
  y = random.randrange(250, 424)
  green_light_list.append([x,y])
  
red_light_list = []    
for i in range(100):
  x = random.randrange(5, 145)
  y = random.randrange(250, 424)
  red_light_list.append([x,y])

#    for i in range(10):
#      pygame.draw.circle(screen, RED, (red_light_list[i][0]+x_offset,red_light_list[i][1]), 5)
#    for i in range(10):
#      pygame.draw.circle(screen, GREEN, (green_light_list[i][0]+x_offset,green_light_list[i][1]), 5)

# ----- House -----
def draw_house():
  pygame.draw.rect(screen, [210,180,140], [int(((width/2)-50)),425,100,50])
  pygame.draw.rect(screen, [51,153,255], [int(((width/2)-5)),460,10,15])
  pygame.draw.rect(screen, WHITE, [int(((width/2)-32)),440,15,15])
  pygame.draw.rect(screen, WHITE, [int(((width/2)+15)),440,15,15])
  pygame.draw.polygon(screen, [210,180,140], [[int(((width/2)+35)), 425], [int(((width/2)+35)), 395], [int(((width/2)+25)), 395],[int(((width/2)+25)), 425]])
  pygame.draw.polygon(screen, RED, [[int(((width/2)+55)), 425], [int((width/2)), 390], [int(((width/2)-55)), 425]])

# ----- Smoke -----
smoke_list = []
for i in range(50):
  x = random.randrange(int(((width/2)+27)), int(((width/2)+33)))
  y = random.randrange(375, 425)
  smoke_list.append([x, y])

def draw_smoke():
  for i in range(len(smoke_list)):
    pygame.draw.circle(screen, WHITE, [round(smoke_list[i][0]),round(smoke_list[i][1])], 3)
    smoke_list[i][1] -= 0.35
    if smoke_list[i][1] < 300:
      y = random.randrange(375, 410)
      smoke_list[i][1] = y
      x = random.randrange(int(((width/2)+27)), int(((width/2)+33)))
      smoke_list[i][0] = x

# ----- Snow -----
snow_list = []
for i in range(100):
  x = random.randrange(0, 700)
  y = random.randrange(0, 500)
  snow_list.append([x, y])
  
def draw_snow():
  for i in range(len(snow_list)):
    pygame.draw.circle(screen, WHITE, snow_list[i], 2)
    snow_list[i][1] += 1
    if snow_list[i][1] > 475:
      # Reset it just above the top
      y = random.randrange(-50, -10)
      snow_list[i][1] = y
      # Give it a new x position
      x = random.randrange(0, 700)
      snow_list[i][0] = x
      
# ----- Stars -----
star_list = []
for i in range(150):
  x = random.randrange(0, 700)
  y = random.randrange(0, 400)
  star_list.append([x, y])

def draw_stars():  
  for i in range(len(star_list)):
    pygame.draw.circle(screen, WHITE, star_list[i], 1)
  
# ------------- Main Program Loop ----------------
def main():
  """ Main program """
  done = False
  while not done:
    # --- Main event loop ---
    #User did something
    for event in pygame.event.get():
      # If user clicked close
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
        snow_list.append([pos[0],pos[1]])

    # --- Game logic ---
    pos = pygame.mouse.get_pos()

    # --- Drawing code ---
    # --- Background fill ---
    screen.fill(BLACK)
    draw_stars()
    draw_tree()
    pygame.draw.rect(screen, WHITE, [0,475,700,25])
  

    draw_snow()    
    draw_smoke()  
    draw_house()
    # Update screen
    pygame.display.flip()
    # Limit to 60 fps
    clock.tick(60)

  pygame.quit()
  
if __name__ == "__main__":
  main()
