This week I found out that my implementation of the Wikipedia pseudocode for Prim's algorithm did not work so i had to do it again, fortunately the tirakirja had a chapter about prim's algorithm too so I used its explanation to create a more simple (and more importantly working) implementation.

Then I added a feature to find the two most distant rooms by using breadth-first search.

Then I added flood fill algorithm using pseudocode from Wikipedia, which uses a list as a queue, so it is based on breadth-first search. 


I looked into a bug in the Bowyer-Watson algorithm, in which the algorithm does not necessarily connect all the points of the triangle (a.k.a. the center points of rooms). When I first discovered it I thought it was a result of a faulty triangle, in which all points were on the same line. After more research it seems to stem from the [faulty pseudocode on Wikipedia](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm#Pseudocode), which fails to mention the fact that the supertriangles should contain all of the circumcircles and not just the circumcenters of the circumcircles. Not many people seem to have noticed this judging from the lack of comments in the talk section of the Wikipedia site, but [stackexchange](https://math.stackexchange.com/questions/4001660/bowyer-watson-algorithm-for-delaunay-triangulation-fails-when-three-vertices-ap) had a workaround. But even after I tried to implement the workaround, the algorithm would not work correctly. So instead of using points in infinity in my super triangle, I use two super triangles, whose points are the largest radius of a any possible triangle away from all points.


Next week I will focus on creating better tests for my algorithms, as well as adding an option to not use the minimum spanning tree for the paths and adding more documentation.


This week's progress took 17 hours.

sources:

https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/

https://en.wikipedia.org/wiki/Flood_fill