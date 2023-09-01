# Implementation document:

## Project structure

The main application in src/index.py will start the process and print outputs. To start the application, invoke commands are used from tasks.py file.
All the logic will be happening in src/logic/ directory. 

In the src/logic/ directory there is dungeon_generation.py that delegates room creation to src/logic/room_generation.py and mostly just creates connections between the generated rooms. In addition to room_generation.py there is also delaunay_triangulation.py. It contains a Delaunay triangulation algorithm that the dungeon generator uses to choose which rooms should have paths between them. 

Then the dungeon generator uses the minimum_spanning_tree.py, which uses Prim's algorithm to choose the paths that result in shortest lengths of paths that still connect the whole map. After this, other paths are discarded.


Finally, src/logic/flood_fill.py replaces all the empty tiles (room tiles) with blue color, and all the dots (paths between rooms) with yellow color. After that datatypes/rooms.py contains the function find_longest_path() which finds the two most distant rooms from each other, and assigns them as the start and end rooms.


I also created some custom datatypes for the sake of more pleasant programming for me, and they can be found under src/datatypes/ directory.


I implemented a configuration system under src/settings/ directory, where you can either write the values o the config.txt file yourself, or just use the invoke commands which use config.py file to write them to the config.txt file. All configurations are read before the application starts.


Lastly, I have all the unittesting files under src/tests/ directory. More about testing can be read at [here](documentation/Testing%20document.md)


A image of the project structure:

```bash
├── src
    ├── datatypes
        ├── coordinates.py
		├── rectangles.py
        ├── rooms.py
		└── triangle.py
    ├── logic
		├── delaunay_triangulation.py
		├── dungeon_generation.py
		├── flood_fill.py
		├── minimum_spanning_tree_test.py
        └── room_generation.py
	├── settings
		├── config.py
        └── config.txt
	├── tests
		├── config_test.py
		├── delaunay_triangulation_test.py
		├── dungeon_generation_test.py
		├── flood_fill_test.py
		├── minimum_spanning_tree_test.py
		├── room_generation_test.py
        ├── rooms_test.py
		└── triangle_test.py
	└── index.py
```



## Implemented time and space complexities 

According to the testing data, time complexity seems to be O(n), where n is the amount of cells. Since the dungeon can be a rectangle too instead of just a square, another way of presenting the time complexity would be O(n*m) where n is the width of the map and m is the length of the map.


#### Random room placement

My implementation of random room placement should pretty much have a time complexity of O(1), since it only has to check if there is room for a room and place the room. It tries at most 20*10 = 200 times to generate a new room until it gives up, so it could be also presented as a time complexity of O(200).


#### Bowyer-Watson algorithm

The Bowyer-Watson version of the Delaunay triangulation has a time complexity of O(n log n) where n is the count of all the rooms on the map. However, my implementation of it has a time complexity of O(n^3), since I wanted to prioritize completing the application first, instead of optimizing the algorithm. The time complexity of O(n^3) instead of O(n^2) comes from a quick workaround I had to do to fix the faulty Wikipedia pseudocode.


#### Prim's algorithm

O(n*m), where n is the count of vertices (center points of room), and m is the count of all the paths that the algorithm should use. This is because I first loop through all the vertices and inside that loop I loop over all the paths. Note that this is usually larger than the normal O(n^2) time complexity, since there can be a lot more paths than vertices.


#### Breadth-first search

I got the idea to use Breadth-first search for the diameter of the graph from [saturncloud](https://saturncloud.io/blog/algorithm-for-diameter-of-a-graph-explained-for-data-scientists/#:~:text=The%20Algorithm%3A%20Breadth-First%20Search,from%20a%20given%20source%20node). I used the pseudocode from [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search), and its worst case time complexity is O(V^2), where V is the count of vertices and. However, my version does not search a certain goal, instead it just connects the rooms to their parents, and after that uses another function to find the maximum distance.

#### Flood fill

I used the pseudocode from [Wikipedia](https://en.wikipedia.org/wiki/Flood_fill), and used a data structure (in this case queue) based implementation. The worst case time complexity is O(n) where n is the count of all the cells.


## Possible flaws and improvements

- The application does not work well with lenght and width of 13 or less for each, but maps that are that small are pretty pointless to generate anyway.


- My implementation of the Bowyer-Watson algorithm could be improved for a time complexity of O(n log n).


## Sources:

https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm

https://stackoverflow.com/questions/71168274/create-custom-data-type-in-python 

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

https://en.wikipedia.org/wiki/Delaunay_triangulation 

https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/

https://saturncloud.io/blog/algorithm-for-diameter-of-a-graph-explained-for-data-scientists/#:~:text=The%20Algorithm%3A%20Breadth-First%20Search,from%20a%20given%20source%20node

https://en.wikipedia.org/wiki/Breadth-first_search

https://en.wikipedia.org/wiki/Flood_fill