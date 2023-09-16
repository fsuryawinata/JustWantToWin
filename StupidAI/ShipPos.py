import random

def getShipPos():
    '''
    THIS IS THE LIST OF SHIPS
    [5,3,3,2,2] 
    That is: 
    1x 5 long
    2x 3 long
    2x 2 long

    Your ships must satisfy this 
    '''

    shipSizes = [5, 3, 3, 2, 2]
    shipPos = []

    for size in shipSizes:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, 9 - size + 1)
                y = random.randint(0, 9)
                positions = [(x + i, y) for i in range(size)]
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9 - size + 1)
                positions = [(x, y + i) for i in range(size)]
            
            if all(0 <= x <= 9 and 0 <= y <= 9 for x, y in positions):
                if all(position not in shipPos for position in positions):
                    shipPos.append(positions)
                    break

    return shipPos
