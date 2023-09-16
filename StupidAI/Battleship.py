import random

# Define constants for directions
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

def initialize_storage():
    return [[], [], 0]  # [direction, confirmed_hit, hits_in_direction]

def validate_coord(coord):
    # Ensure the coordinate is within the range of 1 to 10
    return 1 <= coord <= 10

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    if storage == []:
        storage = initialize_storage()

    # If there was a previous hit, continue in the current direction
    if p1PrevHit:
        if storage[0] is None:
            # Choose a random direction if starting a new direction
            storage[0] = random.choice(DIRECTIONS)
        elif storage[2] == 1:
            # Reverse direction if we didn't get a hit after the first shot
            storage[0] = (-storage[0][0], -storage[0][1])

        # Update the last hit coordinates and increment hits_in_direction
        storage[1] = p1ShotSeq[-1]
        storage[2] += 1
    else:
        # If there was no hit, reset the direction and hits_in_direction
        storage[0] = None
        storage[2] = 0

    # Choose the next coordinates based on the current direction or a random direction
    if storage[0]:
        next_coords = [storage[1][0] + storage[0][0], storage[1][1] + storage[0][1]]
    else:
        next_coords = randCoord(p1ShotSeq, storage)
    
    # Ensure the coordinates are within the range of 1 to 10
    next_coords = [max(1, min(coord, 10)) for coord in next_coords]

    return next_coords, storage

def getBoard():
    board = []
    for x in range(1, 11): 
        for y in range(1, 11):
            board.append([x, y])
    return board

def getBlackSquares():
    black_squares = [[x, y] for x in range(1, 11) for y in range(1, 11) if (x + y) % 2 == 0]
    return black_squares
    

def randCoord(p1ShotSeq, storage):
    if len(storage[1]) != 0:
        foundShip = storage[1]

        # Calculate coordinates of neighboring black squares 2 to 4 blocks away
        neighboring_squares = []

        black_squares = getBlackSquares()  # Get the list of black squares

        for x in range(foundShip[0] - 4, foundShip[0] + 5):
            for y in range(foundShip[1] - 4, foundShip[1] + 5):
                # Check if the coordinates are within the bounds of the 10x10 grid
                if validate_coord(x) and validate_coord(y):
                    # Check if the distance from the found ship coordinates is between 2 and 4 blocks away
                    distance = abs(x - foundShip[0]) + abs(y - foundShip[1])
                    if 2 <= distance <= 4:
                        # Check if the coordinate is a black square
                        if [x, y] in black_squares:
                            neighboring_squares.append([x, y])

        # Filter out coordinates that have already been shot at
        available_neighbors = [coord for coord in neighboring_squares if coord not in p1ShotSeq]
        if len(available_neighbors) != 0:
            return random.choice(available_neighbors)
        else:
            return [random.randint(1, 10), random.randint(1, 10)]
    else:
        # If all neighboring squares have been shot at, choose a random coordinate
        return [random.randint(1, 10), random.randint(1, 10)]


#checking for consecutive neighbors 
def add_neighbours(coord, storage, p1ShotSeq):
    row = coord[0]
    col = coord[1]
    up_neigh = [row - 1, col]
    down_neigh = [row + 1, col]
    left_neigh = [row, col - 1]
    right_neigh = [row, col + 1]

    if up_neigh in p1ShotSeq and validate_coord(up_neigh[0]) and validate_coord(up_neigh[1]):
        storage[0] = [0, -1]  # Update direction to go up
    elif down_neigh in p1ShotSeq and validate_coord(down_neigh[0]) and validate_coord(down_neigh[1]):
        storage[0] = [0, 1]   # Update direction to go down
    elif left_neigh in p1ShotSeq and validate_coord(left_neigh[0]) and validate_coord(left_neigh[1]):
        storage[0] = [-1, 0]  # Update direction to go left
    elif right_neigh in p1ShotSeq and validate_coord(right_neigh[0]) and validate_coord(right_neigh[1]):
        storage[0] = [1, 0]   # Update direction to go right

    return storage
