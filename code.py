#!/usr/bin/env python3

# Cereated by: Rohnin Barrette
# Created on: October 2021
# This program is the "Duck Hunt" program for the PyBadge

import ugame
import stage

def game_scene():
    # this function is the main game_scene
    print("game scene start  ")
    # image blanks for CircutPython
    image_bank_background = stage.Bank.from_bmp16("duckhuntbackground.bmp")
    
    # set the background to image 0 in the image Bank
    #   and the size (10x8 tiles of the size (16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    for x_location in range(10):
        for y_location in range(8):
            background.tile(x_location, y_location, 1)
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites
    #   most likely you will only render the background once per game game_scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        pass # just a placeholder for now
    
if __name__ == "__main__":
    game_scene()
