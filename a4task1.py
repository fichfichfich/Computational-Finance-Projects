"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 4 Part 1: Matrices
 Implementing a Matrix as a 2-D List
 
 https://cs-people.bu.edu/azs/fe459/assignments/a4.html
 
 a4task1.py
"""



def print_matrix(m, label = ""):
    """ 
    Takes two parameters, m which is a 2-dimension list (the matrix)
    and label (a string), and creates a nicely-formatted printout.
    
    Ver. 1 (with label)
    
    """

    # Printing the optional label
    if label != "":
        print (label, "=")
        
    # Printing the first bracket
    print('[', end ='')

    # Indexed For loop to print the list out neatly
    for r in range(len(m)):
        if (r != 0):
            print(" ", end ='') #Adding the space
        for c in range(len(m[r])):
            if (r == len(m) -1 and c == len(m[r]) - 1): #Last number in matrix doesn't have comma
                print(f'{m[r][c]:.2f}', end =']]')
                
            elif (c == 0): #First number has a bracket in front
                print(f'[{m[r][c]:.2f}', end =', ')
                
            elif (c == len(m[r]) -1): #Last number in list does not have comma
                print(f'{m[r][c]:.2f}', end =']')
                
            else: #Numbers that are inbetween
                print(f'{m[r][c]:.2f}', end =', ')
            
        print() #Line seperation
        
### Testing
A = [[3,0,2,1],[2,0,-2,3],[0,2,3,4]]
print_matrix(A)



def zeros(n, m = ""):
    """
    Creates and returns an n * m matrix containing all zeros.

    """
    # Empty matrix to be returned
    matrix = []
    
    if (m == ""):
        m = n
    
    # For loop to create the matrix
    for x in range(n):
        mylist = [] #Empty list to make list of list/matrix
        for y in range(m):
            mylist.append(0.00) #Append a float

        matrix.append(mylist) #Append to matrix
        
    return matrix

### Testing
#print_matrix(zeros(3,5))
#print_matrix(zeros(3))



def identity_matrix(n):
    """
    Creates and returns an n * n identity matrix containing the 
    value of 1 along the diagonal.

    """
    
    # Call to zeros() function
    matrix = zeros(n, n)
    
    # For loop to find the diagonals
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x == y:
                matrix[x][y] += 1 #Adds 1 to existing 0
                
    return matrix
    
### Testing
#I = identity_matrix(3)
#print_matrix(I, 'I')

#A = [[1,2,3],[4,5,6]]
#print_matrix(A, 'A')
    


def transpose(M):
    """
    Creates and returns the transpose of a matrix.

    """
    
    # New matrix to be filled
    matrix = zeros(len(M[0]),len(M))
    
    # For loop to swap the positions
    for x in range(len(M)):
        for y in range(len(M[x])):
            matrix[y][x] = M[x][y] #Swaps the position
        
    return matrix

### Testing
#A = [[1,2,3],[4,5,6]]
#print_matrix(A)

#AT = transpose(A)
#print_matrix(AT, 'AT')
            


def swap_rows(M, src, dest):
    """
    This function will modify the matrix M 
    such that its row order has changed, 
    but none of the values within the rows have changed.
    
    """
    M[src], M[dest] = M[dest], M[src] #Assignment statements

"""
### MISTAKEEE NO LOOPS!

    # New matrix to be filled
    matrix = zeros(len(M),len(M[0]))
    
    # For loop to create a copy of M
    for x in range(len(M)):
        for y in range(len(M[x])):
            matrix[x][y] = M[x][y]

    # For loop to modify M
    for x in range(len(M)):
        for y in range(len(M[x])):
            if (x == src):
                M[x][y] = matrix[dest][y] #Modifies the list to swap src with dest
            if (x == dest):
                M[x][y] = matrix[src][y] #Modifies the list to swap dest with src
"""

### Testing
#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
#print_matrix(A)
#print()

#swap_rows(A, 1, 2) # swap rows 1 and 2
#print_matrix(A)
#print()

#swap_rows(A, 0, 2)
#print_matrix(A)



def mult_row_scalar(M, row, scalar):
    """
    Perorms the elementary row operation 
    that multiplies all values in the row row by the numerical value scalar.

    """
    
    # Verify
    assert (row < len(M) and row >= -1), "Error!"
    
    # For loop to create a copy of M
    for x in range(len(M)):
        for y in range(len(M[x])):
            if (x == row):
                M[x][y] = M[x][y] * scalar #Multiplies by scalar
                
 
### Testing           
#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
#print_matrix(A)
#print()

#mult_row_scalar(A, -1, -1) # multiply row 1 by -1
#print_matrix(A)
#print()

#mult_row_scalar(A, 1, 0.5) # multiply row 1 by 0.5
#print_matrix(A)
            
            

def add_row_into(M, src, dest):
    """
    Performs the elementary-row operation to add the src row into the dest row. 
    That is, each element of row src is to be 
    added into the corresponding element of row dest.
    
    """
    
    # Verify
    assert (src < len(M) and src >= -1 and dest < len(M) and dest >= -1), "Error!"
    
    # New matrix to be filled
    matrix = zeros(len(M),len(M[0]))
    
    # For loop to create a copy of M
    for x in range(len(M)):
        for y in range(len(M[x])):
            matrix[x][y] = M[x][y]

    # For loop to modify M
    for x in range(len(M)):
        for y in range(len(M[x])):
            if (x == dest):
                M[x][y] += matrix[src][y] #Modifies matrix M
 
### Testing
#A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
#print_matrix(A)
#print()

#add_row_into(A, 2, -1) # add row 2 into row 1
#print_matrix(A)
#print()

#add_row_into(A, 2, 1) # add row 2 into row 1
#print_matrix(A)
#print()
    
    
    
    
    