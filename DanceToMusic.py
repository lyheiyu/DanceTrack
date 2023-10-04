import keras
import midiutil.MidiFile
import tensorflow as tf
import pygame
import random
import math
from midiutil.MidiFile import MIDIFile
from pydub import AudioSegment
# Create the MIDIFile Object with 1 track


# initializing pygame
pygame.init()

# setting up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# setting the background music and playing it
# pygame.mixer.music.load('background.mp3')
# pygame.mixer.music.play(loops=-1)

# setting up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# setting the game window caption
pygame.display.set_caption('Dance Motion Generator')

# setting up the frames per second
clock = pygame.time.Clock()

# setting up the dance motion variables
x, y = 50, 50
change_x, change_y = 0, 0


# defining the movements of the dance
def motion_dance():
    global x, y, change_x, change_y

    # movement of the player
    x += change_x
    y += change_y

    if x > width - 20:
        x = width - 20
    elif x < 0:
        x = 0

    if y > height - 20:
        y = height - 20
    elif y < 0:
        y = 0

import os
# defining the music generator

def generate_music():
    # setting up the music note
    # note_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    note_list = ['1', '2', '3', '4', '5', '6', '7','8','9']
    note_index = random.randint(1, 99)
    # note = note_list[note_index]

    # setting up the tempo
    #tempo_list = [60, 70, 80, 90, 100]
    tempo_list = [10, 20, 30, 40, 50]
    tempo_index = random.randint(0, len(tempo_list) - 1)
    tempo = tempo_list[tempo_index]

    # playing the music note
    # pygame.mixer.music.load('note_' + note + '.mp3')
    # pygame.mixer.music.play(loops=-1, tempo=tempo)

    pygame.mixer.music.load('midFile/output'+str(note_index)+'.mid ')

    pygame.mixer.music.play(loops=-1)



    return 'midFile/output'+str(note_index)+'.mid '

# main game loop
run = True
import  time
musicTotal=pygame.mixer.music.load('midFile/output1'+'.mid ')


while run:
    clock.tick(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # getting the movement of the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -50
            elif event.key == pygame.K_RIGHT:
                change_x = 50
            elif event.key == pygame.K_UP:
                change_y = -50
            elif event.key == pygame.K_DOWN:
                change_y = 50
            time.sleep(0.2)

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         change_x = 0
        #     elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         change_y = 0


    # calling the functions
    motion_dance()
    print('d')
    basemusic=generate_music()
    print(basemusic)
    print('m')
    # filling the background color
    screen.fill(white)

    # drawing the player
    pygame.draw.rect(screen, red, (x, y, 20, 20))

    # updating the display
    time.sleep(0.3)
    pygame.display.update()

# quitting the window
pygame.quit()