import pygame
import os
import sys

class enemy():
    def __init__(self,x, y, animations,frame_width, frame_height, num_frames, damage, health,scale =2,anim_speed = 5):
        self.x = x
        self.y = y
        self.damage = damage
        self.health = health
        self.scale = scale
        self.animations = {}
        

        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.anim_speed = anim_speed
        self.anim_counter = 0

    def get_image(self,animation):
        return null
        #Enemy/Golem_1/PNG/PNG Sequences
        
