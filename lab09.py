# PROB 1 TASK 1: Write the required function
'''
•	Input parameters:
o	rowCount: The number of rows. (int)
o	colCount: The number of columns. (int)
o	dataList: a list of values that should be used to initialize the elements of the matrix. (list of strings)
•	Return: the created matrix
'''
def createMatrix(rowCount, colCount, dataList):
    global mat
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)
    return(mat)
        
    
                    
# =========================================
# PROB 2 TASK 1: Write the required function.
'''
o	Input parameters:
o	A matrix to print
o	Return: Nothing
'''
def prettyPrint(mat):
    for i in range(0, len(mat)):
        if(i != 0):
           print()
        for j in range(0, len(mat[0])):    
            print(str(mat[i][j]) + '\t', end = "")

	
# =========================================
# PROB 3 TASK 1: Write the required function.
'''
o	Input parameters:
o	a matrix: a list of lists of strings
o	peelOff: integer
o	Return: a list of strings.
'''
def specialPrint(mat, peelOff):
    elements = []
    if(elements == float):
       for i in range(0, mat):
           if peelOff < i < (mat - (2 * peelOff )):
              for j in range(0, b):
                  if peelOff < j < (peelOff - (2 * peelOff)):
                     element.append(mat[i][j])
    print(elements)
	
	
	
	
	
	
	
def main():  
    alpha = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']	
    #problem 1    	
    #call createMatrix to create a 5x5 matrix using alpha as data.
    createMatrix(4, 6, alpha)
    print(mat)
	
    #==========================
    #problem2
    #call prettyPrint to print the matrix created in problem 1
    prettyPrint(mat)
    #==========================
    #problem3
    #call specialPrint couple of times to print the matric created in problem 1
    #with peeloff equals 1,2,3,0
    print(specialPrint(mat, 0))
	

    
main()
