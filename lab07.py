#Lab07 matplotlib

#import libraries matplotlib.pyplot and numpy
import matplotlib.pyplot as plt

#Problem1 TASK 1: Write function Leibniz.
#function name: Leibniz
#parameter: nterm(datatype: integer)
#two return values: list of x coordinates, list of y coordinates(datatype: list)
def Leibniz(nterm):
    try: 
        
    #Initial values (summation, x list, y list)
        summation = 0
        xlist = []
        ylist = []

    # write a for loop
        for i in range(nterm):
            
        
    #Append each iteration
            xlist.append(i)
                    
    #Summation of Leibniz
            summation = summation + (((-1)**(i))/(2**i + 1))
      
    #Append approximation
            ylist.append(summation)
        print("Updated List: ", summation)
        
    # print out the Summation of Leibniz
        print("Leibniz Sum =", summation)
        
    #print out the PI approximation s*4 = 3.14....
        print("PI approximation =", summation * 4)
        
    # if any error happened, print out "Input is not valid."
    except TypeError:
        ("Input is not valid.")
    
   
    



#Problem1 TASK 2: Wirte function Leibniz_graph
#name: Leibniz_graph
#parameters: list of x coordinates, list of y coordinates (datatype: list)
#return value: no return value.
def Leibniz_graph(x, y):
    x = xlist
    y = summation
    figure = plt.figure()
    plt.plot(x, y)
    ax = fig.add_subplot(200)

    # add the title of the plot
    figure.subtitle('Leibniz Graph')
    
    # add the title of the x axis
    ax.set_xlabel('number of terms')
    
    # add the title of the y axis
    ax.set_ylabel('Terms')
    
    # show the plot
    plt.show()
    


#Problem2 TASK 1: Wirte function plotBarChart
#name: plotBarChart
#parameters: u, p, g (datatype: list)
#return value: no return value.
def plotBarChart(u, p, g):
    ax = plt.subplot()
    label = (['2012', '2013', '2014', '2015', '2016'])
    width = 0.16
    plt.xlabel('Year')
    plt.ylabel('Population')
    x = [2012, 2013, 2014, 2015, 2016]
    rects1 = plt.bar([1,2,3,4,5], u, color = 'black', width = width)
    rects2 = plt.bar([1,2,3,4,5], p, color = 'yellow', width = width)
    rects3 = plt.bar([1,2,3,4,5], g, color = 'grey', width = width)
    plt.title('Purdue')
    plt.legend((rects1[0], rects2[0], rects3[0]), ('Undergraduate', 'Proffesional', 'Graduate'))
    plt.xticks([1,2,3,4,5],[2012, 2013, 2014, 2015, 2016])
    plt.show()
    

#Problem3 TASK 1: Wirte function readData
#function name: readData
#parameter: empty
#return value: return three lists(yellow, red, green)
def readData():
    #initialize lists
                           
                             
    red = open(red.txt, 'r')
    redlist = red.readline()
    xred = []
    yred = []                         

                             
    yellow = open(yellow.txt, 'r')
    yellowlist = yellow.readline()
    xyellow = []
    yyellow = []

    green = open(green.txt, 'r')
    greenlist = green.readline()
    xgreen = []
    ygreen = []  

    #read data from files.
    gdot = green.readline()
    rdot = red.readline()
    ydot = yellow.readline()

    #return three lists.
    for dot in red:
        sublist = dot.split(',')
        xred.append(sublist[0])
        yred.append(sublist[1])
    red = [xred, yred]

    for dot in yellow:
        sublist = dot.split(',')
        xyellow.append(sublist[0])
        yyellow.append(sublist[1])
    yellow = [xyellow, yyellow]

    for dot in green:
        sublist = dot.split(',')
        xgreen.append(sublist[0])
        ygreen.append(sublist[1])
    green = [xgreen, ygreen]
    return(red, yellow, green)


#Problem3 TASK 2: Write function scatterPlot
#function name: scatterPlot
#parameter: three lists (red, yellow, green)
#return value: no return value
def scatterPlot(red, yellow, green):
    plt.scatter(red[0], red[1], c = "red")
    plt.scatter(yellow[0], yellow[1], c = "yellow")
    plt.scatter(green[0], green[1], c = "green")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Colorful Scatter Plot')
    plt.show()


def main():
    #Problem1 TASK 3: Call functions Leibniz and Leibniz_graph.
    # prompt the users to input a number n
    try:
        nterm = eval(input("Please input a number: "))

    # use exception handling 

    # call Leibniz and get two lists
        xlist, ylist = Leibniz(nterm)

    # pass two lists to function Leibniz_graph, draw the plot.

    # when TypeError happened, print out "x, y are not valid."
    except TypeError:
        print("x, y are not valid.")

    # Problem2 TASK 2: Call function plotBarChart
    #creat three lists u, p, g
    #call plotBarChart
    u = ([30147, 29440, 29255, 30523, 33495])
    p = ([946, 941, 947, 956, 973])
    g = ([8163, 8407, 8568, 8983, 9340])
    plotBarChart(u, p, g)
    
    # Problem3 TASK 3: Call function scatterplot
    red, yellow, green = readData()
    scatterPlot(red, yellow, green)

 
main()
