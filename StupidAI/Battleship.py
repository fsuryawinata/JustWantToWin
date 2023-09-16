import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    if storage == []:
        storage = [[],[]]
    board = getBoard()
    coords = randCoord(p1ShotSeq, storage)

    if (p1PrevHit):
        storage[1].append(p1ShotSeq[-1]) # Get latest hit
        storage = add_neighbours(coords, storage, p1ShotSeq)

    if len(storage[0]) != 0:
        coords = storage[0].pop()
    else:
        coords = randCoord(p1ShotSeq, storage)
    
    return coords, storage

def getBoard():
    board = []
    for x in range(1, 11): 
        for y in range(1, 11):
            board.append([x,y])
    return board

def getBlackSquares():
    black_squares = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 2 == 0]
    return black_squares
    

def randCoord(p1ShotSeq, storage):
    if len(storage[1]) != 0:
        foundShip = storage[1].pop()

        # Calculate coordinates of neighboring black squares 2 to 4 blocks away
        neighboring_squares = []

        black_squares = getBlackSquares()  # Get the list of black squares

        for x in range(foundShip[0] - 4, foundShip[0] + 5):
            for y in range(foundShip[1] - 4, foundShip[1] + 5):
                # Check if the coordinates are within the bounds of the 10x10 grid
                if 1 <= x <= 10 and 1 <= y <= 10:
                    # Check if the distance from the found ship coordinates is between 2 and 4 blocks away
                    distance = abs(x - foundShip[0]) + abs(y - foundShip[1])
                    if 2 <= distance <= 4:
                        # Check if the coordinate is a black square
                        if (x, y) in black_squares:
                            neighboring_squares.append((x, y))

        # Filter out coordinates that have already been shot at
        available_neighbors = [coord for coord in neighboring_squares if coord not in p1ShotSeq]
        if len(available_neighbors) != 0:
            return random.choice(available_neighbors)
        else:
            return (random.randint(1, 10), random.randint(1, 10))
    else:
        # If all neighboring squares have been shot at, choose a random coordinate
        return (random.randint(1, 10), random.randint(1, 10))


#checking for consecutive neighbours 
def add_neighbours(coord, storage, p1ShotSeq):
    row = coord[0]
    col = coord[1]
    up_neigh = [row - 1, col]
    down_neigh = [row + 1, col]
    left_neigh = [row, col - 1]
    right_neigh = [row, col + 1]

    if (up_neigh in p1ShotSeq) & check_bound(up_neigh):
        storage[0].append(up_neigh)

    if (down_neigh in p1ShotSeq) & check_bound(down_neigh):
        storage[0].append(down_neigh)

    if (left_neigh in p1ShotSeq) & check_bound(left_neigh):
        storage[0].append(left_neigh)

    if (right_neigh in p1ShotSeq) & check_bound(right_neigh):
        storage[0].append(right_neigh)

    return storage


#checking if the coordinates are not out of the boundaries
def check_bound(coords):
    row = coords[0]
    col = coords[1]
    if row < 1 and row > 10 and col < 1 and col > 10:
        return False
    else:
        return True
