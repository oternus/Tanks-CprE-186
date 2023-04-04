from Conventions import *

def tank_hit_detection(distance_x, distance_y):
    return ((distance_x < (TANK_HITBOX_WIDTH)) and (distance_y < (TANK_HITBOX_HEIGHT)))
