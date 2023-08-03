This week I realized that I had been sidetracking by trying to generate caves when I originally wanted to create dungeons so I wasted a lot of time doing that.


While trying to advance the cave generation I implemented Perlin noise, but because I am creating the cave with same coordinates every time, it does not result in different looking caves even after I tried to add randomness into the algorithm. Perlin noise could be useful if I wanted to create a cave in chunks so that I create a new cave that looks connected to the old one. During the implementation of Perlin noise I learned a lot about bitwise operators in python (mainly that they even exist) while trying to implement the algorithm in python. The example on Wikipedia was written in C, which somehow uses bitwise operators differently so I had to do workarounds for that.


Then I tried random room placement for the cave generation, and found out that square and rectangle rooms are pretty immune to cellular automata smoothing, which isn't surprising after I thought how to algorithm worked more. But when the rooms are close to each other they would merge nicely so maybe it could have some use in the future if I decide to look into cave generation again.

In the end my original "normal randomness cave generation with cellular automata" resulted in the best looking caves, so random room placement was not worth the hassle.


After all this I remembered that I was supposed to be generating dungeons, so I used a method I found online. It is basically random room placement, but whenever it fails to find room
for a room, it tries to place the new room further.

I omitted perlin noise and cave generation from unittests, coverage-reports and pylint, since I don't use them in my application but I wanted to show them regardless in case anyone is curious about my progress.

Next week I will try to implement the room system and Delaunay triangulation to create potential pathways between the rooms.


I spent around 16 hours this week on this project


Here are some sources I used this week:

https://en.wikipedia.org/wiki/Perlin_noise 

Random room placement: https://slsdo.github.io/procedural-dungeon/

The overall dungeon generation process: https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm 

https://en.wikipedia.org/wiki/Delaunay_triangulation 