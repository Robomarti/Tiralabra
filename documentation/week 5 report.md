This week I added variation to room count and thus also added more variation to room sizes.

I also somewhat fixed some bugs that appeared when the width or length of the map was less than 16. This application is not meant to be used with values less than 10 anyway, so I decided to not use that much time on that.


Then I moved on to the Delaunay triangulation. At first I did not understand the Delaunay triangulation algorithm from the old articles I found online, so I pretty much copied the stackoverflow code from the stackoverflow source . But even after I fixed the bug in that post, this implementation still did not work correctly, so I deleted everything and implemented it myself using the pseudocode that I found in the wikipedia article that the publisher of the post used as a source. With the pseudocode I finally understood how to implement the Delaunay triangulation, and now it is working correctly.


I then started implementing a maximum spanning tree using a reversed Prim's algorithm, but realised that would cause paths to go through rooms more often so I changed it into a minimum spanning tree.


Next week I will add finding the two most distant rooms and marking them as start and end.


A question that I have is that how necessary for passing the course is it to have implemented user interface. I recall I heard something about ASCII graphics being good enough, and I think my graphics currently are ASCII. I would like to know now if I have to start implementing a main menu system or something, or is my current command-based system ok?


This week's progress took 16 hours.

sources:

https://github.com/jmespadero/pyDelaunay2D

https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
