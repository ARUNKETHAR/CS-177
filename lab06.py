# Lab06 Functions and Files

# Problem1
# Function name: checkCourse
# Parameters: course_nos, course_titles, coursenum
# Return value: the course name
def checkCourse(course_nos, course_titles, coursenum):
# check if the course number in the list course_nos
    for i in range(len(course_nos)):
        if (course_nos[i].find(coursenum) != -1):
            return course_titles[i]
    return "Sorry, the course is not available for spring 2017"

# Problem1
# Function name: readFile
# Parameters: filename
# Return value: course_nos, course_titles
def readFile(filename):
    course_nos = []
    course_titles = []
    f = open('spring2017courses.txt', 'r')
    for line in f:
        splitline = line.split(',')
        course_nos.append(splitline[0])
        course_titles.append(splitline[1].strip())
    f.close()
    return course_nos, course_titles

# =========================================

# Problem2
# Function name: heroVillainUniverse’ 
# Parameters: 
# heroes
#The heroes’ file name (type: string)
# villains    The villains’ file name (type: string)
# universes   The comic book universe’s file name (type: string)
# outName The name of the output hero/villain/comic file name (type: string)
# Return value: No return

#TASK 1: Write the definition of the function 'heroVillainUniverse'
def heroVillainUniverse(heroes, villains, universes, outName):
    #TASK 2: Open and read the files.
    hero = open(heroes, 'r')
    villain = open(villains, 'r')
    universe = open(universes, 'r')
    tempOutDC = []
    tempOutMarvel = []
    outFile = open(outName, 'w')
    #TASK 3: Form the hero/villain/comic triplet in a string separated by commas
    for hLine in hero:
        vLine = villain.readline()
        uLine = universe.readline()
        if(uLine.find('DC') != -1):
            tempOutDC.append('1' + hLine.strip() + ', ' + vLine.strip() + ', ' + uLine.strip() +'\n')
        else:
            tempOutMarvel.append('0' + hLine.strip() + ', ' + vLine.strip() + ', ' + uLine.strip() +'\n')
    #TASK 4: Write the triplets to the specified file in the required order
    for i in tempOutDC:
        outFile.write(i[1:])
    for i in tempOutMarvel:
        outFile.write(i[1:])
        
    hero.close()
    villain.close()
    universe.close()
    
def main():  
#problem 1
    # invoke readFile to open the file, read all the data into two lists
    a, b = readFile('spring2017courses.txt')
    # prompt the user to input the number of the course.
    userIn = input("Please input a course number: ")
    # invoke checkCourse to check if the course is available for registration
    print(checkCourse(a, b, userIn))
    #==========================
        #problem2
    # define the names of the three input files and the output file
    # either by user input, or just by assigning the file names to variables.
    hero = 'heroes.txt'
    villain = 'villains.txt'
    universe = 'comicBook.txt'
    # invoke heroVillainUniverse’ with these file names
    heroVillainUniverse(hero, villain, universe, 'output.txt')
    
main()
