#Lab08
#You are not allowed to use factorial function in the math library.


# Problem 1 Task 1: Write function factFunc
# Function name: factFunc
# Parameter: n (datatype: integer)
  # Return value: factorial of the input number(datatype: integer)
def factFunc(n):
    j = 1
    count = 1
    while j >= n:
        count = int(count) * j
        j <= 1
    
    #return the factorial of the input number
    return (count)
    
    

# Problem 1 Task 2: Write function pascalTriangle.
# Function name: pascalTriangle
# Parameter: num (datatype: integer)
# Return value: empty
def pascalTriangle(num):
    # initialize index variable
    
    r1 = [1]
    r2 = [1, 1]

    value = 1
    
    # while loop for each row

    while value <= num:
        print(r1)
        
    # while loop to print spaces and while loop for printing numbers
    while r1 <= num and r2 <= num:
        r1, r2 = r2, [1] + [sum(space) for space in zip(r2, r2[1: ])
                        
    
        
        
   
# Problem 2 Task 1: Write function maxCharCount.
# Function name: maxCharCount
# Parameter: mystring (datatype: string)
# Return value: a list of all characters of maximum occurrence with no duplicates(datatype: list)
def maxCharCount(myString):
    a = list(myString)
    b = []
    x = 0
    count = 0.0
    while x < len(a):
        if(a[x] in c):
          a[x[c]] = 1 + a[x[c]] 
        else:
             c[a[x]] = 1
            if c[a[x]] > count):
                count = c[a[x]]
            i = i + 1
        for x in c:
            if[c[x] == m]:
                b.append(x)
        return (b)

def main():
# Problem 1 Task 3: Call function pascalTriangle in main.
    # prompt the user to input the number of the rows.
    funcFact(n)
    n = eval(input("Enter the number of rows: " ))
             
    # call pascalTriangle function
    pascalTriangle(num)
    

# Problem 2 Task 2: Call maxCharCount in main.
    # prompt the user to input a string.
    a = eval(input("Enter a string: "))
    print(a)
    
    # call maxCharCount function
    maxCharCount(myString)
    
main()
