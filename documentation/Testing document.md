## Coverage report:
![Coverage-report](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/coverage.png)


## What has been tested, and how


#### Configs

I tested:

	- that the configs work with wrong type of user input.

	- that the configs set width and lenght of less than 20 as 20




#### Bowyer-Watson

I tested:

	- the edge_not_in_other_bad_triangles() function by giving it input with edge in and edge not in other triangles.

	- the whole algorithm by giving it input, and comparing the algorithm's output to the one I calculated with GeoGebra.

	- that the algorithm does not work with three points that are on the same y- or x-axis, as this algorithm should not work with them.




#### Dungeon generation

I tested:

	- that start_delaunay() returns True on success, and that it returns False when it is unsuccessful, for example when the points it uses are on the same y- or x-axis.

	- that the create_room_connections() function creates connections between rooms correctly.

	- some basic functions, but not much else since most functions in the dungeon generation are functions that are already tested elsewhere.




#### Flood fill

I tested:

	- that the fill affects the cells of the map correctly.




#### Prim's algorithm:

I tested:

	- that the distance function it uses works correctly.

	- that every vertex that is in the input of the algorithm, is also in the output.

	- that the algorithm gives a correct result in two different graphs by calculating by hand.




#### Room generation

I tested:

	- that rooms can not be placed on top of each other.

	- that the room generation knows when there is room for a room. I tested this by giving it a map with room and a map without room as inputs.

	- that the room generation does not affect the outer rims of the map, even when the generator wants to put the room there.

	- other various functions in the room_generation.py.




#### Rooms

I tested:
	- that the various functions the file uses work



#### Triangle

I tested:

	- that the distance function it uses works.




#### Execution speed

I tested how long the code takes to execute with different room sizes, while using the minimum spanning tree option spanning = True. For this I used Python's built-in profilers. Here is the execution speed test data.

![Time chart](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/time_chart.png)

Here the equals is just multiplication of the width and lenght shown on the cells line.

![Time graph](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/time_graph.png)


Here we can see that the time greatly depends on the shape of the dungeon. When the dungeon was just a thin line, doubleing the width sometimes only doubled the time required for executing the code. This would be a time complexity of O(n), where the n is the count of all the cells. However, with larger dungeons the time required was multiplying with different rates as the the cell count doubled.


When the dungeon was a large square, generating the dungeon took over four times longer for the same amount of cells. This is because there were more rooms on the y-axis since the lenght of the dungeon was larger too. This makes the Prim's algorithm take longer, since before it could pretty much just add lines horizontally, since most of the rooms were on a line, since there was not much room to be on top or under other rooms.


## How to replicate tests


To get the coverage report use the command
```bash
invoke coverage-report
```
The command also executes all the tests required. The report will be generated to the directory htmlcov where you can copy the path to the index.html and paste it to
your browser.


To only execute the tests use
```bash
invoke test
```


To time the code execution, first set the room size with
```bash
invoke config --length wanted_length_in_int --width wanted_width_in_int --spanning boolean
```
Note: the application does not work well with lenght and width of 16 or less for each. Please make sure that length and width are at least 20.


Then use
```bash
python -m cProfile src/index.py
```

or

```bash
python3 -m cProfile src/index.py
```