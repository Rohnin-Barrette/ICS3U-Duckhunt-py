#!usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: July 2020
# This is the constants file for the Space Alien game

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160 
SCREEN_Y = 128 
SCREEN_GRID_X = 10 
SCREEN_GRID_Y = 8 
SPRITE_SIZE = 16 
TOTAL_NUMBER_OF_DUCKS = 5
FPS = 160
SPRITE_MOVEMENT_SPEED = 1 
CROSSHAIR_SPEED = 1
DUCKS_SPEED = 0.20 
OFF_SCREEN_X = 160
OFF_SCREEN_Y = 50
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60 
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
  "button_up": "up",
  "button_just_pressed": "just pressed",
  "button_still_pressed": "still pressed",
  "button_released": "button released"
}
# new pallet for filled text

RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
               
BLUE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
