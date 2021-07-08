def SoSoSplotchy(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 2
    else:
        return 2*SoSoSplotchy(n-1) + SoSoSplotchy(n-2)
    
    
   

def getMin(A):
    if len(A) == 1:
        return A[0]
    else:
        min = getMin(A[1:])
        if A[0] < min:
            return A[0]
        else:
            return min
        
    
def log(x,y):
    if x < y:
        return 0
    return 1 + log(x / y, y)
    
    
    
    

    
def main():
    print(SoSoSplotchy(5)) # should print 70
    print(getMin([3, -1, 5, 7, 2, 4])) #should print -1
    print(log(16,2)) #should print 4
    
main()
