## Coverage report:
![Coverage-report](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/coverage.png)


## What has been tested, and how

I have tested cellular automata, in case I might need it sometime since I already implemented it accidentally.

I tested its wall_count() function by giving it a small matrix as a game map, where some tiles were walls and some were floors.

Then I also tested the whole cellular automata by giving it another small matrix as a game map and making sure that it only changed the tile it was working on if the
conditions were met.


I also tested the dungeon generation algorithm by testing its different functions. For example, I made up some custom maths to decide
how many rooms each dungeon should have, so I tested that it works.

Then I tested that the room generation does not affect the outer rims of the map, even when the generator wants to put the room there.

I have also tested that the function that tells whether there is room for a room works by giving it a map with room and a map without room as inputs.




I tested how long the code takes to execute with different room sizes. For this I used Python's built-in profilers. Here is the execution speed test data.

![Time chart](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/time_chart.png)
![Time graph](https://github.com/Robomarti/Tiralabra/blob/main/documentation/images/time_graph.png)

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
invoke config --length wanted_length_in_int --width wanted_width_in_int
```
Note: the application does not work well with lenght and width of 16 or less for each. Please make sure that length and width are at least 17.


Then use
```bash
python -m cProfile src/index.py
```