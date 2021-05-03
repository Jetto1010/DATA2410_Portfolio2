import math

# Find the fruit closest to the snake
def closest_fruit(fruit, c):
    WIDTH = c["dimensions"][0]
    HEIGHT = c["dimensions"][1]
    fruits = c["fruits"]
    pos = c["pos"]


    if not fruit:
        fruit = (WIDTH, HEIGHT)

    if fruits:
        for f in fruits:
            # Distance between snake head and fruit
            new_dist = math.hypot(f[0] - pos[0], f[1] - pos[1])
            old_dist = math.hypot(fruit[0] - pos[0], fruit[1] - pos[0])

            print(new_dist, old_dist, new_dist < old_dist)
            if new_dist < old_dist:
                fruit = (f[0], f[1])
    else:
        return None

    return fruit

# Find closest path to closest_fruit, all while avoiding obstacles like border and other snakes
# Djikstra's algorithm
# Array with coordinates to closest_fruit, next_pos - pos = (velX, velY)
def find_path():
    return

# Final bot_main() will look like
"""
draw()
find closest fruit
find path to closest fruit
before moving check if path has changed
move to closest fruit
"""