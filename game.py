from os import system
import keyboard as k
import random
from world_generator_v2 import world_generator, show_world
import time
import copy


def clear():
    system("cls")


menu_text = """
+ -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- +
|                                              |
|               Test RPG Project               |
|                      By                      |
|                   Jakraes                    |
|               + - - - - - - - +              |
|                    [P]LAY                    |
|                  [C]ONTROLS                  |
|                                              |
+ -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- +
"""

controls_text = """
+ -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- +
|   + WASD to walk                             |
|   + ESC to go back to menu                   |
|                                              |
|                                              |
|                                              |
|                                              |
|                                              |
|                                              |
+ -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- +
"""


def menu():
    clear()
    print(menu_text)
    key = k.read_key()
    if key == "p":
        game()
    elif key == "c":
        controls()
    else:
        menu()


def controls():
    clear()
    print(controls_text)
    key = k.read_key()
    if key == "esc":
        menu()
    else:
        controls()


def movement(current_position, world, tiles):
    key = k.read_key()
    if key == "w" and current_position[0] != 0:
        current_position[0] -= 1
        if current_position in tiles["# "]:
            current_position[0] += 1
        return current_position
    elif key == "s" and current_position[0] != len(world) - 1:
        current_position[0] += 1
        if current_position in tiles["# "]:
            current_position[0] -= 1
        return current_position
    elif key == "a" and current_position[1] != 0:
        current_position[1] -= 1
        if current_position in tiles["# "]:
            current_position[1] += 1
        return current_position
    elif key == "d" and current_position[1] != len(world[0]) - 1:
        current_position[1] += 1
        if current_position in tiles["# "]:
            current_position[1] -= 1
        return current_position
    elif key == "esc":
        return "True"
    else:
        movement(current_position, world, tiles)


def game():
    character = {"hp": 10, "attack": random.randint(1, 5), "tile": "@"}
    generation = world_generator()
    world = generation[0]
    tiles = generation[1]
    spawn_tiles = tiles["_ "]
    spawn = random.choice(spawn_tiles)
    current_position = spawn
    playing = True
    copy_world = copy.deepcopy(world)
    copy_world[current_position[0]][current_position[1]] = "@ "
    clear()
    print(show_world(copy_world))
    while character["hp"] > 0 and playing:
        copy_world = copy.deepcopy(world)
        time.sleep(0.2)
        mov = movement(current_position, copy_world, tiles)
        clear()
        if mov == "True":
            playing = False
            menu()
        else:
            copy_world[current_position[0]][current_position[1]] = "@ "
            print(show_world(copy_world))


menu()
