import random

def create_world(size):
    world = []
    a = []
    for line in range(size):
        world.append([])
        for col in range(size):
            world[line].append(". ")
    return world

def create_rooms(min_w, max_w, min_h, max_h):
    width = random.randint(min_w,max_w)+2
    height = random.randint(min_h,max_h)+2
    room = []
    for line in range(height):
        room.append([])
        for col in range(width):
            if line == 0 or line == height-1:
                room[line].append("# ")
            elif col == 0 or col == width-1:
                room[line].append("# ")
            else:
                room[line].append("_ ")
    return room, width, height

def add_rooms(world, amount, min_w, max_w, min_h, max_h):
    position_max = len(world[0]) - 1
    for x in range(amount):
        line = random.randint(0, position_max)
        col = random.randint(0, position_max)
        roominfo = create_rooms(min_w, max_w, min_h, max_h)
        room = roominfo[0]
        width = roominfo[1]
        height = roominfo[2]
        for linha in range(height):
            for coluna in range(width):
                try:
                    if world[line+linha][col+coluna] != "_ ":
                        world[line+linha][col+coluna] = room[linha][coluna]
                except:
                    pass
    return world

def filter_world(world):
    for line in range(len(world)):
        for col in range(len(world[0])):
            try:
                if world[line][col] == "# " and (world[line-1][col] != ". " and world[line+1][col] != ". " and world[line][col-1] != ". " and world[line][col+1] != ". "):
                    world[line][col] = "_ "
            except:
                pass
    for line in range(len(world)):
        for col in range(len(world[0])):
            try:
                if world[line][col] == ". " and (world[line+1][col-1] == "_ " or world[line+1][col+1] == "_ " or world[line-1][col-1] == "_ " or world[line-1][col+1] == "_ "):
                    world[line][col] = "# "
            except:
                pass
    for line in range(len(world)):
        for col in range(len(world[0])):
            try:
                if world[line][col] == "# " and ((world[line-1][col] == "_ " and world[line+1][col] == "_ ") or (world[line][col-1] == "_ " and world[line][col+1] == "_ ")):
                    world[line][col] = "_ "
            except:
                pass

    world_copy = create_world(len(world)+2)

    for line in range(len(world)):
        for col in range(len(world[0])):
            world_copy[line+1][col+1] = world[line][col]

    for line in range(len(world)):
        for col in range(len(world[0])):
            if line == 0 or line == len(world)-1 or col == 0 or col == len(world[0])-1:
                if world[line][col] == "_ ":
                    world[line][col] = "# "
    for line in range(len(world)):
        for col in range(len(world[0])):
            area = [world_copy[line][col], world_copy[line][col+1], world_copy[line][col + 2],
                    world_copy[line+1][col], world_copy[line+1][col+1], world_copy[line+1][col + 2],
                    world_copy[line + 2][col], world_copy[line + 2][col+1], world_copy[line + 2][col + 2]]
            if "_ " not in area:
                world[line][col] = ". "
    return world

def show_world(world):
    x = ""
    for line in range(len(world)):
        for col in range(len(world[0])):
            x += world[line][col]
        if line < len(world)-1:
            x += "\n"
    return x

def generate_world(world_size_min, world_size_max, room_amount_min, room_amount_max, room_w_min, room_w_max, room_h_min, room_h_max):

    blank_world = create_world(random.randint(world_size_min, world_size_max))
    room_amount = random.randint(room_amount_min, room_amount_max)
    world = add_rooms(blank_world, room_amount, room_w_min, room_w_max, room_h_min, room_h_max)
    world = filter_world(world)
    final_world = show_world(world)
    return final_world

print(generate_world(20, 20, 5, 7, 1, 6, 1, 7))