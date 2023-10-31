"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 4 Part 2: Matrices
 Matrix Operations
 
 https://cs-people.bu.edu/azs/fe459/assignments/a4.html
 
 a4task2.py
"""

from a4task1 import *



def add_matrices(A, B):
    """
    Takes as parameters 2 matrices (2d lists) 
    and returns a new matrix which is 
    the element-wise sum of the matrices A and B.
    
    """
    
    # Verify
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Error!"
    
    # New Matrix
    matrix = zeros(len(A), len(A[0]))
    
    # For loop to update new matrix
    for x in range(len(A)):
        for y in range(len(A[x])):
            matrix[x][y] = A[x][y] + B[x][y]
            
    return matrix

### Testing
#A = [[1,2],[4,5]]
#B = [[4,3],[3,1]]
#S = add_matrices(A,B)
#print_matrix(S, 'S')



def mult_scalar(M, s):
    """
    Takes as a parameter a 2-dimension list M (the matrix) 
    and a scalar value s (i.e., an int or float), 
    and returns a new matrix containing the values of the original matrix 
    multiplied by the scalar value.
    
    """
    # New matrix
    matrix = zeros(len(M), len(M[0]))
    
    # For loop to update the new matrix
    for x in range(len(M)):
        for y in range(len(M[x])):
            matrix[x][y] = M[x][y] * s
            
    return matrix

### Testing    
#A = [[3,0,2,1],[2,0,-2,3]]
#print_matrix(A)

#B = mult_scalar(A, 3)
#print_matrix(B)
    
    
    
def sub_matrices(A, B):
    """
    Takes as parameters 2 matrices (2d lists) 
    and returns a new matrix which is the element-wise difference
    of the matrices A and B.
    
    """
    # Call to mult_scalar()
    mult = mult_scalar(B, -1)
    
    # Call to add_matrices()
    matrix = add_matrices(A, mult)
    
    return matrix
 
### Testing   
#A = [[1,2,3],[4,5,6]]
#B = [[4,5,6],[1,2,3]]
#D = sub_matrices(A, B)
#print_matrix(D, 'D')
    


def element_product(A, B):
    """
    Takes as parameters two matrices A and B, 
    and returns a new matrix containing element-wise product of these matrices.

    """
    # Verify
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Error!"
    
    # New Matrix
    matrix = zeros(len(A), len(A[0]))
    
    # For loop to update the new matrix
    for x in range(len(A)):
        for y in range(len(A[x])):
            matrix[x][y]= A[x][y] * B[x][y]
            
    return matrix

### Testing
#A = [[3,0,2], [2,0,-2], [0,1,1]]
#print_matrix(A)
#print()

#B = mult_scalar(A, 2)
#print_matrix(B)
#print()

#P = element_product(A, B)
#print_matrix(P, 'P')
            
    
    
def dot_product(A, B):
    """
    Takes as parameters two matrices M and N, 
    and returns a new matrix containing dot product of these matrices.
    
    """
    
    # Verify
    assert len(A[0]) == len(B), "Error!"
    
    # writing out row and column
    row = len(A)
    col = len(B[0])
    
    # New Matrix
    matrix = zeros(col, row)
    
    # For loop (nested) that took me more than half an hour to write up
    for x in range(row):
        for y in range(col):
            for z in range(len(A[0])):
                matrix[x][y] += A[x][z] * B[z][y] 
                #print (A[x][y], B[y][x],matrix[x][y]) ### Testing thru print
                #print (A[x][z], B[z][y],matrix[x][y]) ### Testing thru print
                #print (A[y][z], B[x][y],matrix[x][y]) ### Testing thru print
                
    return matrix



### Testing
#A = [[1,2,3],[4,5,6]]
#print_matrix(A)
#print()

#B = [[3,2],[4,1],[5,0]]
#print_matrix(B)
#print()

#P = dot_product(A,B)
#print_matrix(P, 'P')


















    
    