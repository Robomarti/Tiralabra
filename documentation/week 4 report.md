
added more testing, patched mocks to random values so I could test functions that used random
revamped the room generation, made sure that rooms do not spawn next to border
made sure that the application can not get stuck in infinite loop when it tries to fit a room that can not fit anywhere. Instead it discards it and tries again up to 10 times and gives up after that.

added some sort of delaunay triangulation

room sizes are pretty constant across map sizes, they are always about 3 or 4 wide and long. This is because the room size depends on the room count. I should change the values a
bit so that there is more variation

hours: 20