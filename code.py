#!usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: november 2021
# This program is the "Duck Hunt" program on the PyBadge

import ugame
import stage
import random
import time
import supervisor

import constants

def splash_scene():
    # function is the splash scene
    
    #image banks for CircutPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    

    # create a stage for background to show up on
    #   and set frame rate to 60fps
    # sets the background to image 0 in the image Bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
                            
       # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    
    #create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # Wait 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # function is the main game game_scene
    
    #image banks for CircutPython
    image_bank_mt_background = stage.Bank.from_bmp16("sprites.bmp")
    
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    
    
    # sets the background to image 0 in the image Bank
    #   and the size (10x8 tiles of the size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    
    #create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = text + [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
       for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 1)
            background.tile(x_location, y_location, tile_picked)

                            
    # create a stage for the background to show up once
    #    and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely only render background once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprite 
        game.tick() # wait until refresh rate finishes

def game_scene():
    # function is the main game game_scene

    score = 0

    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))
    

    def show_duck():
        # this function takes an alien off screen and moves it on screen 
        for duck_number in range(len(ducks)):
            if ducks[duck_number].x < 0: 
                ducks[duck_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                            constants.SCREEN_X - 
                                                            constants.SPRITE_SIZE), 
                                        constants.OFF_TOP_SCREEN)
                break

    
    #image banks for CircutPython


    image_bank_sprites = stage.Bank.from_bmp16("sprites.bmp")
    
    # buttons that I want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

     
    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    #set the background to image 0 in the image Bank
    #   and the size (10x8 tiles of the size 16x16)
    background = stage.Grid(image_bank_sprites, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
       for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 1)
            background.tile(x_location, y_location, tile_picked)
    
    # a sprite that will be updated every frame
    
    # a sprite that will be updated every frame
    duck = stage.Sprite(image_bank_sprites, 3, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
      # create a list of ducks for when we shoot
    ducks = [] 
    for duck_number in range(constants.TOTAL_NUMBER_OF_DUCKS):
        a_single_duck = stage.Sprite(image_bank_sprites, 3,
                                        constants.OFF_SCREEN_X,
                                        constants.OFF_SCREEN_Y)
        ducks.append(a_single_duck)
        # place 1 duck on the screen 
    show_duck()
    
    crosshair = stage.Sprite(image_bank_sprites, 2, 75, 66)
    
    #create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [score_text] + ducks + [crosshair] + [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # A button preto firessed
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
           pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if crosshair.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                crosshair.move(crosshair.x + 1, crosshair.y)
            else:
                crosshair.move(constants.SCREEN_X - constants.SPRITE_SIZE, crosshair.y)
        if keys & ugame.K_LEFT:
            if crosshair.x >= 0:
                crosshair.move(crosshair.x - 1, crosshair.y)
            else:
                crosshair.move(0, crosshair.y)
        if keys & ugame.K_UP:
            if crosshair.y >= 0:
                crosshair.move(crosshair.x, crosshair.y - 1)
            else:
                crosshair.move(crosshair.x, 0)
        if keys & ugame.K_DOWN:
            if crosshair.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:
                crosshair.move(crosshair.x, crosshair.y + 1)
            else:
                crosshair.move(crosshair.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            
        
        # update game logic


 # each frame move the ducks down,that are on the screen
        for duck_number_number in range(len(ducks)):
            if ducks[duck_number].x + constants.SPRITE_SIZE> 0: 
                ducks[duck_number].move(ducks[duck_number].x - constants.DUCKS_SPEED,
                                            ducks[duck_number].y)
                    
                if ducks[duck_number].x + constants.SPRITE_SIZE < 0:
                    ducks[duck_number].move(constants.OFF_SCREEN_X,
                                                random.randint(0 + constants.SPRITE_SIZE, 
                                                constants.SCREEN_Y - constants.SPRITE_SIZE))
                    show_duck()
                    score -= 1
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))
                    game.render_block()
# to check if the target is touching the duck
        
        for duck_number in range(len(ducks)):
                    if stage.collide(crosshair.x + 16, crosshair.y + 2,
                                    crosshair.x + 11, crosshair.y + 12,
                                    ducks[duck_number].x + 1, ducks[duck_number].y,
                                    ducks[duck_number].x + 15, ducks[duck_number].y + 15):
                        # if you hit a duck
                        ducks[duck_number].move(constants.OFF_SCREEN_X,
                                                random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_Y 
                                                - constants.SPRITE_SIZE))
                        sound.stop()
                        sound.play(pew_sound)
                        show_duck()
                        score = score + 1
                        score_text.clear()
                        score_text.cursor(0,0)
                        score_text.move(1,1)
                        score_text.text("Score: {0}".format(score))
                        game.render_block()
        # redraw Sprite 
        game.render_sprites(ducks + [crosshair])
        game.tick() # wait until refresh rate finishes
        
        if score >= 10 or score < -3:
            game_over_scene(score)
        
def game_over_scene(final_score):
    # this function is the game over scene
    
    # image banks for CircutPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # sets the background image to 0 in the image bank 
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
                            
    # add text objects
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22,20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)
    
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(43,60)
    text2.text("GAME OVER")
    text.append(text2)
    
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)
    
    #create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = text + [background]
    # render all sprites
    #   most likely you will only render the background once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
            
        # update game logic
        game.tick() # wait until refresh rate fineshes

        
if __name__ == "__main__":
    splash_scene()
    
