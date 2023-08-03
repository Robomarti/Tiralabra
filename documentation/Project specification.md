The topic of the project is dungeon generation. I will use python to generate dungeon layouts with a multi-step process.


I will generate the initial 2d dungeon layouts with random selection of cells. Then I will start reforming the map using cellular automata algorithm procedurally in iterations, see the roguebasin source. I will try to use it so that it only leaves unconnected rooms. During or after that I will mark every unconnected cave / room maybe by simply going over every
pixel. Then I will remove too small caves with the flood fill algorithm. Then I will connect unconnected rooms with the Bresenham's line algorithm.
I might also color the different rooms with different colors with flood fill. I will then use a modified Depth-first search to find the longest path between a starting room
and the furthest room and mark them as the start / end rooms.


The problem I am solving is the need for endless different dungeon layouts. I chose the beforementioned algorithms because they had the most publicity and documentation.


This program probably will only take simple y/n as input as well as the probability that is used to calculate initially whether a pixel should be a wall or a floor. I might add the 
possibility of altering the dungeon size by an input parameter.
A dungeon will be printed with print commands, after which the program asks whether it should generate another dungeon.


Sources: https://www.roguebasin.com/index.php/Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels


I am hoping for a time  complexity of the program to be close to O(n) where n is the count of all cells on the map.


My degree programme is Tietojenkäsittelytieteen kandidaatti


Language used in documentation will be English.