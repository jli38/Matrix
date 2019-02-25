from display import *
from draw import *
from matrix import *
import math
import random

screen = new_screen()
color = [ 0, 255, 0 ]

matrix1 = new_matrix(0)
matrix2 = new_matrix(0)
print "m1: adding edge (1,2,3) & (4,5,6)"
add_edge(matrix1,1,2,3,4,5,6)
print "m1: adding edge (5,2,3) & (1,5,2)"
add_edge(matrix1,5,2,3,1,5,2)
print_matrix(matrix1)

print "m2: adding edge (1,2,3) & (18,100,2)"
add_edge(matrix2,1,2,3,18,100,2)
print "m2: adding point (2,4,6)"
add_point(matrix2,2,4,6)
print "m2: adding point (100,50,5)"
add_point(matrix2,100,50,5)
print_matrix(matrix2)

print "multiplying m1 & m2"
matrix_mult(matrix1,matrix2)
print_matrix(matrix2)

print "identifying m2"
ident(matrix2)
print_matrix(matrix2)

clear_screen(screen)
matrix = new_matrix(0)
x, y, z = 250, 250, 1
for i in range(250):
	add_edge(matrix, x, y, z, int( i * math.sin(i*math.pi)) + 200, int( i * math.cos(i*math.pi)) + 200 , 1)
	x = int( i*math.pi ) + random.randrange(50)
	y = int( i*math.pi ) + random.randrange(50)
	z = 1
add_edge(matrix, x, y, z, 250, 250, 1)
draw_lines(matrix,screen,color)

save_extension(screen,"img.png")
display(screen)
