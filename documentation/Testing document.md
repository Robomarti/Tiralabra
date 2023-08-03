## Coverage report:
![Coverage-report](/images/coverage.png)


## What has been tested, and how

I have tested cellular automata, in case I might need it sometime since I already implemented it accidentally.

I tested its wall_count() function by giving it a small matrix as a game map, where some tiles were walls and some were floors.

Then I also tested the whole cellular automata by giving it another small matrix as a game map and making sure that it only changed the tile it was working on if the
conditions were met.


I also tested the dungeon generation algorithm by testing its different functions. For example, I made up some custom maths to decide
how many rooms each dungeon should have, so I tested that it works.

Then I tested that the room generation does not affect the outer rims of the map, even when the generator wants to put the room there.

I have also tested that the function that tells whether there is room for a room works by giving it a map with room and a map without room as inputs.


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
