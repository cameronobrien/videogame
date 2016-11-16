"""
main

Handles the core game loop

:author: Cameron O'Brien
"""

import pygame
import random
from character import Character
width, height = 1280, 720
background_color = (255, 255, 255)
bg = pygame.image.load("background_image.png")
player_health = 100
pygame.display.set_caption('Realm of the Crab God')


class Game:

    def __init__(self):
        clock = pygame.time.Clock()
        self.all_sprites_list = pygame.sprite.Group()
        screen = pygame.display.set_mode((width, height))
        sprite = Character("warrior", 15, 15, 64, 64)
        self.all_sprites_list.add(sprite)
        running = True
        pygame.key.set_repeat(10, 10)
        file = 'music/background_music1.mp3'
        pygame.mixer.init()  # Initialize background music
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit conditional
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        sprite.move(-5, 0)
                    elif event.key == pygame.K_RIGHT:
                        sprite.move(5, 0)
                    elif event.key == pygame.K_UP:
                        sprite.move(0, -5)
                    elif event.key == pygame.K_DOWN:
                        sprite.move(0, 5)
            screen.blit(bg, (0, 0))
            self.all_sprites_list.update()  # Game Logic
            self.all_sprites_list.draw(screen)  # Draw sprites
            pygame.display.flip()  # Refresh screen
            clock.tick(60)  # Number of frames per second


g = Game()
