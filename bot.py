import math
import time
from queue import PriorityQueue

# c in this file stands for client_info, which contains all information needed for the bot to calculate its path
# Nodes that are connected to the coordinates of the snake game
class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.n = [] # Neighbors
        self.parent = parent

        # Length of amount of parents
        if self.parent:
            self.length = parent.length + 1
        else:
            self.length = 0

        # Distance from fruit
        self.distance = None
    
    # Lesser than comparator
    def __lt__(self, other):
        return False


    # If the node is not the border or part of a snake, it adds it as a neighbor (Excluding things we want to avoid)
    def set_n(self, c):
        snakes = c["snakes"]
        snake_body = c["snake_body"]
        vel = c["velocity"]
        WIDTH, HEIGHT = c["dimensions"]

        def is_safe(x, y):
            # Boolean statements for game_over if test below
            hit_self = (x, y) in snake_body[:-1]
            hit_border = x > WIDTH - 1 or x < 0 or y > HEIGHT - 1 or y < 0
            backwards = (x, y) in snake_body

            hit_snakes = False
            for snake in snakes:
                if (x, y) in snake["position"]:
                    hit_snakes = True

            if hit_self or hit_border or hit_snakes or backwards:
                return False
            else:
                return True

        # UP
        xup, yup = (self.x + 0), (self.y + 1)
        if is_safe(xup, yup):
            self.n.append(Node(xup, yup, self))

        # RIGHT
        xright, yright = (self.x + 1), (self.y + 0)
        if is_safe(xright, yright):
            self.n.append(Node(xright, yright, self))

        # DOWN
        xdown, ydown = (self.x + 0), (self.y - 1)
        if is_safe(xdown, ydown):
            self.n.append(Node(xdown, ydown, self))

        # LEFT
        xleft, yleft = (self.x - 1), (self.y + 0)
        if is_safe(xleft, yleft):
            self.n.append(Node(xleft, yleft, self))

# Returns the distance between the snake head and fruit
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Find the fruit closest to the snake
def closest_fruit(fruit, c):
    WIDTH, HEIGHT = c["dimensions"]
    fruits = c["fruits"]
    pos = c["snake_body"][-1]

    if not fruit:
        fruit = (WIDTH, HEIGHT)

    if fruits:
        for f in fruits:
            new_dist = distance(f, pos)
            old_dist = distance(fruit, pos)

            if new_dist < old_dist:
                fruit = (f[0], f[1])
    else:
        return None

    return fruit

# Find closest path to closest_fruit, all while avoiding obstacles like border and other snakes
# A* algorithm
# Array with coordinates to closest_fruit, next_pos - pos = (velX, velY)
# F(n) = G(n) + H(n)
# F(n) = len(path) + distance(pos, fruit)

# Look at neighbors of node, then pick the one with the shortest F(n)
def find_path(fruit, c):
    pos = c["snake_body"][-1]
    vel = c["velocity"]
    length = 0
    path = []
    checked_nodes = []
    

    # Put in snake head node to start process
    potential_path = PriorityQueue()
    starting_node = Node(pos[0] + vel[0], pos[1] + vel[1], None)
    end_node = starting_node
    potential_path.put(starting_node)
    potential_path_list = [starting_node]

    while not potential_path.empty():
        current_node = potential_path.get()
        potential_path_list.remove(current_node)

        # If the snake head has reached the fruit position, the stop
        if (current_node.x, current_node.y) == fruit:
            end_node = current_node
            break
        
        # Checks the neighbouring nodes to the current one, and compares their distance with each other.
        # The node with the shortest distance gets picked and put into potential path list
        current_node.set_n(c)
        for neighbor_node in current_node.n:
            temp_f = current_node.length + 1 + distance(fruit, (current_node.x, current_node.y))
            neighbor_f = neighbor_node.length + distance(fruit, (neighbor_node.x, neighbor_node.y))

            if temp_f > neighbor_f:
                if neighbor_node not in potential_path_list and neighbor_node not in checked_nodes:
                    potential_path.put(neighbor_node)
                    potential_path_list.append(neighbor_node)

        # The algorithm has checked this node, and it is not the fastest way
        if current_node != starting_node:
            checked_nodes.append(current_node)

    # Appends the the path, by going through each nodes parent, which is the path traversed
    path.append((end_node.x, end_node.y))
    while end_node.parent:
        end_node = end_node.parent
        path.append((end_node.x, end_node.y))

    return path.reverse()
    
# Final bot_main() will look like
"""
draw()
find closest fruit
find path to closest fruit
before moving check if path has changed
move to closest fruit
"""