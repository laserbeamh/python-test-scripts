#!/usr/bin/env python3
import pygame
from math import pi

# Init pygame engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

# Set screen size and launch
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set window title
pygame.display.set_caption("Buddy's First Game")

# Init done variable
done = False

# Manage screen update screen
clock = pygame.time.Clock()

# ------------- Main Program Loop ----------------
while not done:
  # --- Main event loop ---
  #User did something
  for event in pygame.event.get():
    # If user clicked close
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    elif event.type == pygame.KEYUP:
        print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")

  # --- Game logic ---

  # --- Drawing code ---
  # Fill screen with white
  screen.fill(WHITE)
  pygame.draw.rect(screen, RED, [55, 50, 20, 25], 5)
  pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
  pygame.draw.line(screen, BLUE, [100, 0], [0, 100], 5)
  pygame.draw.line(screen, BLACK, [100, 100], [0, 100], 5)
  
  for y_offset in range(0,490,20):
    pygame.draw.line(screen, BLUE, [175,10+y_offset], [515,10+y_offset], 5)

  for x_offset in range(0,350,20):
    pygame.draw.line(screen, RED, [175+x_offset,10], [175+x_offset,490], 5)
    
  # Select the font to use, size, bold, italics
  font = pygame.font.SysFont('Calibri', 25, True, False)
 
  # Render the text: Text, anti-aliased (if True), color 
  # Note: This line does not put text on the screen.
  text = font.render("Score: ",True,BLACK)
 
  # Put the image of the text on the screen
  screen.blit(text, [50, 250])

  # Update screen
  pygame.display.flip()
  # Limit to 60 fps
  clock.tick(60)

pygame.quit()

# --- Game logic ---
#While not done:
#    For each event (keypress, mouse click, etc.):
#        Use a chain of if statements to run code to handle each event.
#    Run calculations to determine where objects move, what happens when objects collide, etc.
#    Clear the screen
#    Draw everything
