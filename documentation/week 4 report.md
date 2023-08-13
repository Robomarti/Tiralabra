This week I  added more unittesting and patchedrandom values to mock values so I could test functions that used features from the random library.
I then revamped the room generation, and made sure that rooms do not spawn next to or inside of the border.
I also made sure that the application can not get stuck in infinite loop when it tries to fit a room that can not fit anywhere. Instead it discards it and tries again up to 10 times and gives up completely after that.


I also researched the web about Delaunay triangulation, which was surprisingly hard since everyone only seemed to reference some research papers published in the 1900s. They were too complex for me so I tried to undestand the basics of it and implement it in my own way. The result is not a perfect Delaunay triangulation, but with smaller maps between 20-40 units of lenght and width it looks really good. With larger maps it currently still leaves a few unconnected clusters of rooms but I will try to fix that next week.

I then researched Bresenham's line algorithm for creating pathways between rooms that should be connected. After a bit I realised that it does not look as good as just two straight line along the x- and y-axis, so I don't think I will use it in this project.


I added testing data about the time it requires to execute the code with different room sizes. After that I realized that room sizes are pretty constant across map sizes, as they are always about three or four cells wide and long. This is because the room size depends on the room count, which means that I should change the values a
bit so that there is more variation. But if I were to implement this application to a game where each cell would be 1 meter squared, I think smaller rooms look better for dungeon style map.


Finally I made more docstring documentation.

next week I will finalize the room connection part and find the two most distant rooms and make sure that they are connected. Then I will mark them in a different color

hours: 25