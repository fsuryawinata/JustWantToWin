import random
def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    board = getBoard()
    coords = randCoord(p1ShotSeq)

    if (p1PrevHit):
        storage = add_neighbours(coords, storage)

    if len(storage) != 0:
        for possible_sq in storage:
            if possible_sq in board:
                if len(board) != 0:
                    board.remove(possible_sq)
                    coords = board.pop()
                else:
                    coords = storage.pop()
    
    return coords, storage

def getBoard():
    board = []
    for x in range(1, 11):  # Range from 1 to 9
        for y in range(1, 11):  # Range from 1 to 9
            board.append([x,y])
    return board


def randCoord(p1ShotSeq):
    while True:
        x = random.randint(1, 10)  # Random x-coordinate between 0 and 9
        y = random.randint(1, 10)  # Random y-coordinate between 0 and 9
        new_coords = (x, y)
        if new_coords not in p1ShotSeq:
            return new_coords

#checking for consecutive neighbours 
def add_neighbours(coord, storage):
    row = coord[0]
    col = coord[1]
    up_neigh = [row - 1, col]
    down_neigh = [row + 1, col]
    left_neigh = [row, col - 1]
    right_neigh = [row, col + 1]

    storage.append(up_neigh)
    storage.append(down_neigh)
    storage.append(left_neigh)
    storage.append(right_neigh)
    return storage


#checking if the coordinates are not out of the boundaries
def check_bound(row, col):
    if 0 > row and row > 9 and 0 > col and col > 9:
        return 1
    else:
        return 0
