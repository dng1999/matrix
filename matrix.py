import math


def print_matrix( matrix ):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            print matrix[c][r],
        print
            
def ident( matrix ):
    m = []
    m.append([1,0,0,0])
    m.append([0,1,0,0])
    m.append([0,0,1,0])
    m.append([0,0,0,1])
    return m

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
            for r1 in range(len(m1[0])):
                res += (m1[c1][r1]*m2[r2][c1])
            m[c1].append(res)
    return m
                
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
