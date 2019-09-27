# Author: Jordan Spangenberg
# Email: jordan.spang at gmail dot com
# 

def add(*argv):
    if len(argv) < 1:
        raise ValueError('add() takes at least one argument')
    #if not all(matrix is type("class 'list'") for matrix in argv):
        #raise TypeError('Function accepts n number of x by y int arrays')
    if not all(len(col) == len(argv[0]) for col in argv):
        raise ValueError('Matrices are not uniform')
    for i in range(len(argv)):
        cellLen = len(argv[i][0])
        for j in range(len(argv[i])):
            if len(argv[i][j]) != cellLen:
                raise ValueError('Cells are not of the same length')

    res = [[ 0 for col in range(len(argv[0][0])) ] for row in range(len(argv[0]))]
    for matrix in argv:
        res = addTwo(res, matrix)
    return res


def addTwo(matrix1, matrix2):
    '''
    Helper method to add two matrices together
    '''
    res = []
    for n, m in zip(matrix1, matrix2):
        res.append( [x + y for x,y in zip(n,m)])
    return res
