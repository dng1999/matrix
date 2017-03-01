import math


def print_matrix( matrix ):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            print matrix[c][r],
        print
            
def ident( matrix ):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            if c==r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    return matrix

def scalar_mult( matrix, s ):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            matrix[c][r] *= s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = []
    for c1 in range(len(m1)):
        m.append([])
        for r2 in range(len(m2[0])):
            res = 0
            for c2 in range(len(m2)):
                res += (m1[c1][c2]*m2[c2][r2])
            m[c1].append(res)
    return m
                
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
