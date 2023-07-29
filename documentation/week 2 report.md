During this week I started the cave generator class, and added the ability to manipulate its inputs. The output is now printed into the command line, which looks pretty clean to me.
I also started making tests for the cave generation process, and added the ability to get coverage reports.
I added docstring documentation to many parts of the code.
I made invoke commands so that running the application, testing it and changing configs are easier to do. Currently the index.py file which is used to do the generation process is looking pretty ugly but I will work on that next week.


Testing is a bit complicated because of the random starting cells of the generation algorithm, but I will find out how to test that next week.


Currently the only way of creating the caves is cellular automata algorithm, but I might add better looking algorithm because there is no way of knowing whether the algorithm will produce many caves inside of the map or just one large one. This might be able to be improved by fine-tuning the config values but it would not completely eliminate the problem. When the algorithm produces many caves / rooms they look nice at least, so I might keep the cellular automata as a clean up algorithm.


I used about 15 hours this week to learn about the testing and task modules as well as improving documentation and of course a part of that time was used to create more code.