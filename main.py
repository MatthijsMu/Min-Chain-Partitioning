from minChainPartition import MinChainPartition

'''
This file contains code relevant to the specific problem statement.
'''


def fitsIn(boxA, boxB):
    '''
    Defines the partial ordering relationship on boxes (a box is a sorted tuple of floats)
    '''
    return boxA[0] < boxB[0] and boxA[1] < boxB[1] and boxA[2] < boxB[2]

def volume(box):
    '''
    Volume of the box (i.e. product of its dimensions)
    '''
    return box[0] * box[1] * box[2]

def inputBoxes():
    '''
    Function for parsing input in the format specified in the problem statement.
    '''
    n = int(input())
    boxes = []
    for _ in range(n):
        [x,y,z] = input().split()
        x = float(x)
        y = float(y)
        z = float(z)
        boxes.append(tuple(sorted([x,y,z])))

    return boxes


'''
main code:
'''
boxes = inputBoxes()
#print("done with input") # Debugging!
minChainPartition = MinChainPartition(boxes, fitsIn, volume)
#print("done creating partition problem") # Debugging!
minChainPartition.solvePartition()
#print("done solving partition problem") # Debugging!
# partition = minChainPartition.solvePartition() # Debugging
# print(partition)
print(minChainPartition.getNrOfChains())
