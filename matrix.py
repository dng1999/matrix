import math


def print_matrix( matrix ):
    for r in range(0,4):
        print("%d %d %d %d" % (matrix[0][r],matrix[1][r],matrix[2][r],matrix[3][r]))
            
def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    for c in range(0,4):
        for r in range(0,4):
            matrix[c][r] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
