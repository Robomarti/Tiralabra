# Implementation document:

## Project structure

The main application in src/index.py will start the process and print outputs. To start the application, invoke commands are used from tasks.py file.
All the logic will be happening in src/logic/ directory. There is the dungeon_generation.py that delegates room creation to src/logic/room_generation.py and mostly just creates connections between the generated rooms. In addition to room_generation.py there is also delaunay_triangulation.py that the dungeon generator uses to choose which rooms should have paths between them. I probably did not implement Delaynay triangulation as it should have been since I'm not that good in math, but I think I implemented it well enough for this purpose. The only part missing is that it does not leave further parts of the map unconnected to the main part.


I also created some custom datatypes for the sake of more pleasant programming for me, and they can be found under src/datatypes/ directory.


I implemented a configuration system under src/settings/ directory, where you can either write the values o the config.txt file yourself, or just use the invoke commands which use config.py file to write them to the config.txt file. All configurations are read before the application starts.


Lastly, I have all the unittesting files under src/tests/ directory. More about testing can be read at [here](documentation/Testing%20document.md)


A image of the project structure:

```bash
├── src
    ├── datatypes
        ├── coordinates.py
		├── rectangles.py
        └── rooms.py
    ├── logic
		├── delaunay_triangulation.py
		├── dungeon_generation.py
        └── room_generation.py
	├── settings
		├── config.py
        └── config.txt
	├── tests
		├── delaunay_triangulation_test.py
		├── dungeon_generation_test.py
		├── room_generation_test.py
        └── rooms_test.py
	└── index.py
```



## Implemented time and space complexities 

According to the testing data, time complexity seems to be O(n), where n is the amount of cells. Since the dungeon can be a rectangle too instead of just a square, another way of presenting the time complexity would be O(n*m) where n is the width of the map and m is the length of the map.


#### Random room placement

My implementation of random room placement should pretty much have a time complexity of O(1), since it only has to check if there is room for a room and place the room. It tries at most 20*10 = 200 times to generate a new room until it gives up, so it could be also presented as a time complexity of O(200).


#### Delaunay triangulation

The Bowyer-Watson version of the Delaunay triangulation has a time complexity of O(n log n) where n is the count of all the rooms on the map. However, my implementation of it has a time complexity of O(n^2), since I wanted to prioritize completing the application first, instead of optimizing the algorithm.


#### Prim's algorithm


## Possible flaws and improvements

- The application does not work well with lenght and width of 13 or less for each, but maps that are that small are pretty pointless to generate anyway.


- My implementation of the Bowyer-Watson algorithm could be improved for a time complexity of O(n log n).


## Sources:

https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm

https://stackoverflow.com/questions/71168274/create-custom-data-type-in-python 

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

https://en.wikipedia.org/wiki/Delaunay_triangulation 