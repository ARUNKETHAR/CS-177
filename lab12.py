'''
Uuse the prelab class, then do the needed modifications.
Here is a list of modifications:
1) You should add a list of actor objects as a data member in the class movie. This list holds the actor objects who acted in the movie.
2) You should modify the print_summary() method in the class movie to print the summaries of the actors of the movie as well. Which means, in addition to the printing the summary of the movie, you need to loop through the actors of the movie and call print_summary() of each actor.
'''
class movie:
    f = open("prelab_movies.txt", "r")
    c = f.read()
    print(c)
    f.close()
    
'''
Problem 1: Class actor   
name: the name of the actor (string)
birthPlace: The country the actor was born (string)
movieList: A list of all the movies he/she appeared in (list of strings)
The constructor
print_summary(): This method should print out a summary of the actor information.
'''
class actor:
    name=""
    birthPlace=""
    movieList=[]
    eCount = 0
    
def __init__(self, name, birthPlace, movieList):
    self.name = name
    self.birthplace = birthPlace
    self.movieList = movieList
    actor.eCount += 1
        
def read_actors():
    for i in range(len(movieList)):
        print (actor.self)
        print (actor.name)
        print (actor.birthPlace)
        print (actor.append(movieList))
            
        
# Use the prelab function
def read_movies():
    myFile = open("actors.txt", "r")
    content = myfile.read()
    print(content)
    myFile.close()
    

#Problem 2: Creating a list of actors
#returns: A list of actor objects (list) This
def read_actors():
    f = open("prelab_movies.txt", "r")
    c = f.read()
    print(c)
    f.close()
    
'''
Problem 3: Linking Movies to Actors
Inputs: 
movies (list of movie objects). 
actors (list of actor objects).
You are required to add the actors to their corresponding movies.
Note: An actor can be added to more than one movie
'''
def link_movies_actors(movies, actors):
    self.movies = movies
    if not self.birthPlace:
        print(read_actors())
    else:
         print(link_movies_actors)
    
'''
Problem 4: Movies with Maximum Number of Actors    
Using the movie's print_summary() you are required to print out all movies
with maximum number of actors.
'''
def print_max_actors_movies(movies):
    actorList = []
    charList = []
    aList = list(movies())
    print(aList)
    print(aList[0])
    for i in range(len(aList[i])):
        if i % 2 == 0:
            charList.append(aList[i])
        else:
             actorList.append(aList[i])
    print(charList)
    print(actList)
        
    
    
def main():
	#call read_movies
    read_movies()
	
	#call read_actors
    read_actors()
	
	#call link_movies_actors
    link_movies_actors()
	
	#call print_max_actors_movies
    max_actors_movies()
    
    
main()
    
    
     
