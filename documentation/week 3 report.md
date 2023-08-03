I used wikipedia as a source. 
I tried perlin noise, but even though I feel like I copied the example perfectly, it still does not feel random. 
Probably because I am creating the cave with same coordinates every time.

random room placement is pretty immune to cellular automata smoothing, except when the rooms are close to each other.
random room placement not worth it

in the end normal randomness was best

I omitted perlin noise and cave generation from coverage and lint, since I don't use them in my application but I wanted to show them regardless in case anyone is curious about my progress.

Then I remembered that I was supposed to be generating dungeons, so I used a method I found online. It is basically random room placement, but whenever it fails to find room
for a room, it tries to place the new room further.


What I lerned
What was hard

Next week I will try to implement the room system and Delaunay triangulation to create potential pathways between the rooms


I spent around 16 hours this week on this project

sources:
https://en.wikipedia.org/wiki/Perlin_noise 
https://slsdo.github.io/procedural-dungeon/ random room placement
https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm 
https://en.wikipedia.org/wiki/Delaunay_triangulation 