"""
 Man Chi Chan (Fiona)
 
 fich@bu.edu
 
 FE459 - Prof. Aaron Stevens
 
 Assignment 6: Thinking in Objects - Matrix Class
 Task 1: A Matrix class
 
 
 https://cs-people.bu.edu/azs/fe459/assignments/a6.html
 
 a6task1.py
"""

import random

class Matrix:
    """
    Defines a Matrix object
    
    The matrix will support a wide-variety of operations, 
    including printing itself out, row-based operations, 
    and some linear-algebra operations.
    
    """
    
    def __init__(self, m):
        """initializes the Matrix Object"""
        self.m = m


        
    def __repr__(self):
        """Prints a string representation of the Matrix """
        
        # Create empty string
        s = ""
        
        # Concactinate the first bracket to it
        s += '[' 

        # Indexed For loop to print the list out neatly
        for r in range(len(self.m)):
            if (r != 0):
                s += " " #Adding the space
            for c in range(len(self.m[r])):
                if (r == len(self.m) -1 and c == len(self.m[r]) - 1): #Last number in matrix doesn't have comma
                    s += f'{self.m[r][c]:.2f}' + ']]'
                    
                elif (c == 0): #First number has a bracket in front
                    s += f'[{self.m[r][c]:.2f}' + ', '
                    
                elif (c == len(self.m[r]) -1): #Last number in list does not have comma
                    s += f'{self.m[r][c]:.2f}' + ']'
                    
                else: #Numbers that are inbetween
                    s += f'{self.m[r][c]:.2f}' + ', '
                
            s += "\n"
            
        return s
    
    
    
    def __eq__(self, other):
        """Defines the == operator for this Matrix class"""
        
        # Check lengths to see if Matricies are the same length
        if len(self.m) != len(other.m):
            return False 
        
        # For loop to check and see if each value in the matrix is the same
        for r in range(len(self.m)): #Row
            for c in range(len(self.m[r])): #Column
                if self.m[r][c] != other.m[r][c]: # Check to see if value is the same
                    return False # Return False if value is not the same
                
        return True # Return True only if all values in the Matrix are the same
        
        
        
    def add_row_into(self, src, dest):
        """Adds the values in row src to the values in row dest"""
        
        # Verify that the lengths are the same and that the src and dest are not out of bounds
        assert (src < len(self.m) and src >= -1 and dest < len(self.m) and dest >= -1), "Error!"
        
        # For loop to add the values in row dest to the values in row src
        for x in range(len(self.m)): #Row
            for y in range(len(self.m[x])): #Column
                if x == dest: # If the row == destination...
                    self.m[x][y] += self.m[src][y] # Then we add the values in src to it
        
        
        
    def add_mult_row_into(self, mult, src, dest): 
        """Multiplies mult to the values in src and adds them to dest 
        (value of mult does not change) """
        
        # For loop to add the values in row dest to the values in row src
        for x in range(len(self.m)): #Row
            for y in range(len(self.m[x])): #Column
                if x == dest: # If the row == destination...
                    self.m[x][y] += self.m[src][y] * mult # Then we muliply src row by mult and add to dest
                    
    
    
    def swap_rows(self, src, dest):
        """Swaps row src with row dest"""
        
        self.m[src], self.m[dest] = self.m[dest], self.m[src] #Assignment statements to swap rows
        
            

    def add_scalar(self, num):
        """Adds a number (num) to each value in the Matrix.
        This operation returns a new Matrix"""
        
        # Create the new lists that will become the new Matrix Object
        newlist = [] #New list - the foundation of the new Matrix Object
        templist = [] #Temporary list - helps build the Matrix Object
        
        # For loop to add_scalar the values in the list
        for x in range(len(self.m)): #Row
            for y in range(len(self.m[x])): #Column
                templist.append(self.m[x][y] + num) #Add the num to the original value at m[x][y]
                
            newlist.append(templist) #Add the temporary list to the original list
            templist = [] #Reset the temporary list
        
        result = Matrix(newlist) #Create the new Matrix object
        
        return result #returns the new Matrix Object
    
    
    
    def mult_scalar(self, num):
        """Multiplies a number (num) to each value in the Matrix.
        This operation returns a new Matrix"""
        
        # Create the new lists that will become the new Matrix Object
        newlist = [] #New list - the foundation of the new Matrix Object
        templist = [] #Temporary list - helps build the Matrix Object
        
        # For loop to mult_scalar the values in the list
        for x in range(len(self.m)): #Row
            for y in range(len(self.m[x])): #Column
                templist.append(self.m[x][y] * num) #Multiply the num to the original value at m[x][y]
                
            newlist.append(templist) #Add the temporary list to the original list
            templist = [] #Reset the temporary list
        
        result = Matrix(newlist) #Create the new Matrix object
        
        return result #returns the new Matrix Object
        

    #overload the + operator
    def __add__(self, other):
        """Defines the + operator for this Matrix class 
        This operation returns a new Matrix"""
        
        if isinstance(other, int):
            return self.add_scalar(other) #Add directly if other == int
        else:
            assert len(self.m) == len(other.m), "Error!" #Check to see if lenghts are the same
            result = Matrix([[0 for i in range(len(self.m[0]))] for i in range(len(self.m))]) #Create new matrix (to be returned)
            
            # For loop to add the two Matricies together
            for r in range(len(self.m)): #Row
                for c in range(len(self.m[r])): #Column
                    result.m[r][c] = self.m[r][c] + other.m[r][c] 
    
        return result #returns the new Matrix Object
        
    

    #overload the - operator
    def __sub__(self, other):
        """Defines the - operator for this Matrix class
        This operation returns a new Matrix"""
        
        if isinstance(other, int):
            return self.add_scalar(-other) #Subtract directly if other == int
        else:
            assert len(self.m) == len(other.m), "Error!" #Check to see if lenghts are the same
            result = Matrix([[0 for i in range(len(self.m[0]))] for i in range(len(self.m))]) #Create new matrix (to be returned)
            
            # For loop to subtract the two Matricies 
            for r in range(len(self.m)): #Row
                for c in range(len(self.m[r])): #Column
                    result.m[r][c] = self.m[r][c] - other.m[r][c] 
    
        return result #returns the new Matrix Object
        
    
    
    #overload the * operator
    def __mul__ (self, other):
        """ Defines the * operator for this Maxtrix class
        This operation returns a new Matrix"""
        
        if isinstance(other, int):
            return self.mult_scalar(other) #Multiply directly if other == int
        elif len(self.m) != len(other.m): #If the lenghts are not the same, dot product them
            return self.dot_product(other) 
        else: #If the lengths are the same, multiply them
            result = Matrix([[0 for i in range(len(other.m[0]))] for i in range(len(self.m))]) #Create new matrix (to be returned)
            
            # For loop to multiply the two Matricies together
            for r in range(len(self.m)): #Row
                for c in range(len(other.m[r])): #Column
                    result.m[r][c] = self.m[r][c] * other.m[r][c] 
    
        return result #returns the new Matrix Object
    
    
    
    #overload the / operator
    def __truediv__(self, other): 
        """Defines the / operator for this Matrix class
        This operation returns a new Matrix"""
        
        if isinstance(other, int):
            return self.mult_scalar(1/other) #Divide directly if other == int
        else:
            assert len(self.m) == len(other.m), "Error!" #Check to see if lenghts are the same
            result = Matrix([[0 for i in range(len(self.m[0]))] for i in range(len(self.m))]) #Create new matrix (to be returned)
            
            # For loop to Divide the two Matricies together
            for r in range(len(self.m)): #Row
                for c in range(len(self.m[r])): #Column
                    result.m[r][c] = self.m[r][c] / other.m[r][c] 
    
        return result #returns the new Matrix Object



    def transpose(self):
        """Transposes the matrix 
        This operation returns a new Matrix"""
        
        # Create a new list
        newlist = [[0 for i in range(len(self.m))] for i in range(len(self.m[0]))] #create a new list, inverse dimensions of old one
        result = Matrix(newlist)
        
        # For loop to transpose the values in the list
        for x in range(len(self.m)): #Row
            for y in range(len(self.m[x])): #Column
                result.m[y][x] = self.m[x][y] #Swaps the position
        
        return result #returns the new Matrix Object
    
    
    
    def dot_product(self, C):
        """ Calculate the dot product of two matricies
        This operation returns a new Matrix"""
        
        # Verify that C is a Matrix Object
        assert isinstance(C, Matrix), "Error!"
        
        # Verify that the two matricies are valid for a dot product operation
        assert len(self.m[0]) == len(C.m), "Error!"
        
        # Setting up row and column
        row = len(self.m)
        col = len(C.m[0])
        
        # Create the new Matrix Object (full of 0s)
        result = Matrix([[ 0 for i in range(col)] for i in range(row)])
        
        # For loop (nested) that calculates the dot product
        for x in range(row):
            for y in range(col):
                for z in range(len(self.m[0])):
                    result.m[x][y] += self.m[x][z] * C.m[z][y] #Calculate the dot product value and put it in its place

        return result #returns the new Matrix Object


    
    # Class level methods, no "self" (others are object level methods)
    def zeros(row, col = ""):
        """Creates a Matrix Object full of zeroes"""
        if col == "": #If column is empty, return a "square" matrix
            return Matrix([[ 0 for i in range(row)] for i in range(row)])
        else: #If there is a value for column, return a row x column matrix
            return Matrix([[ 0 for i in range(col)] for i in range(row)])
        
        
        
    # Class level methods, no "self" (others are object level methods)
    def ones(row, col = ""):
        """Creates a Matrix Object full of ones"""
        if col == "": #If column is empty, return a "square" matrix
            return Matrix([[ 1 for i in range(row)] for i in range(row)])
        else: #If there is a value for column, return a row x column matrix
            return Matrix([[ 1 for i in range(col)] for i in range(row)])
        
        
    
    # Class level methods, no "self" (others are object level methods)
    def identity(row, col = ""):
        """Creates a Matrix Object with 1s going diagonally across it"""
        
        # Create a new matrix
        matrix = Matrix.zeros(row, col)
        
        # For loop to cycle through the Matrix
        for x in range(len(matrix.m)):
            for y in range(len(matrix.m[x])):
                if x == y:
                    matrix.m[x][y] += 1 #Adds 1 to existing 0 on the diagonal
        
        return matrix
        
        

    def random_int_matrix(row, col = "", r_low = 1, r_high = 10):
        """Creates a random int matrix
        This operation returns a new Matrix"""
        
        # Create a new matrix
        matrix = Matrix.zeros(row, col)
        
        # For loop to cycle through the Matrix
        for x in range(len(matrix.m)):
            for y in range(len(matrix.m[x])):
                matrix.m[x][y] = random.randint(r_low, r_high) #Assign a random int
                    
        return matrix
    
    
    
    def random_float_matrix(row, col = ""):
        """Creates a random float matrix
        This operation returns a new Matrix"""
        
        # Create a new matrix
        matrix = Matrix.zeros(row, col)
        
        # For loop to cycle through the Matrix
        for x in range(len(matrix.m)):
            for y in range(len(matrix.m[x])):
                matrix.m[x][y] = random.random() #Assign a random float
                    
        return matrix
    
    
    
    def describe(self):
        """Describes a Matrix Object"""
        
        # Find row and column
        row = len(self.m)
        col = len(self.m[0])

        # Find Matrix sum
        m_sum = 0
        for x in range(len(self.m)):
            for y in range(len(self.m[x])):
                m_sum += self.m[x][y] #Add values together to get sum
        
        # Find Matrix mean
        m_mean = m_sum/(row*col)
        
        # Set empty list for column sum and column mean
        c_sum = []
        c_mean = []
        temp_sum = 0
        
        # For loop to add the sum (and find the mean) of the columns 
        for c in range(len(self.m[0])): #interate through column
            for r in range(len(self.m)): #iterate through row
                temp_sum += self.m[r][c]
            
            c_sum.append(temp_sum) #Update sum
            c_mean.append(temp_sum/row) #Update mean
            temp_sum = 0
                
        # Describe the matrix
        s = repr(self)
        
        # Descriptions
        s += f'dimensions: {row} x {col}' + '\n'
        s += f'sum of elements: {m_sum}' + '\n'
        s += f'mean of elements: {m_mean}' + '\n'
        s += f'column sums: {c_sum}' + '\n'
        s += f'column means: {c_mean}' 
        
        return s #Return the string
        








if __name__ == '__main__':
    A= Matrix([[1.00, 2.00, 3.00], [4.00, 5.00, 6.00]])
    C= Matrix([[7.00, 8.00], [9.00, 10.00], [11.00, 12.00]])
    
    # A = Matrix([[1,2,3],[4,5,6], [7,8,9]])
    
    # B = Matrix([[4,5,6],[1,2,3]])
    
    # C = Matrix([[7,8,4],[9,10,3],[11,12,5]])
            
            
            
            
            
            
    