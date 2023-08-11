
added more testing, patched mocks to random values so I could test functions that used random
revamped the room generation, made sure that rooms do not spawn next to border
made sure that the application can not get stuck in infinite loop when it tries to fit a room that can not fit anywhere. Instead it discards it 10 times and gives up after that.

hours: 7