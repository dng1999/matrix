from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
print("Printing matrix.")
print_matrix(matrix)

print("Running ident(matrix)...")
matrix = ident(matrix)
print("Printing result.")
print_matrix(matrix)

print("Running scalar_mult(matrix,2)...")
matrix = scalar_mult(matrix,2)
print("Printing result.")
print_matrix(matrix)

print("Making matrix m1 with (1,2,3)(4,5,6)...")
m1 = []
m1.append([1,2,3])
m1.append([4,5,6])
print("Printing m1.")
print_matrix(m1)

print("Making matrix m1 with (7,8)(9,10)(11,12)...")
m2 = []
m2.append([7,8])
m2.append([9,10])
m2.append([11,12])
print("Printing m2.")
print_matrix(m2)

print("Running matrix_mult(m1,m2)...")
matrix = matrix_mult(m1,m2)
print("Printing result.")
print_matrix(matrix)

matrix = new_matrix()
for i in range(500):
    add_edge(matrix,i,((i*7-3)%402)+53,0,(i+129)/3,250,0)

draw_lines( matrix, screen, color )
display(screen)
#save_extension(screen, "pic.png")
