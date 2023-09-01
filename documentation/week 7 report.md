This week I improved testing and the pylint score. There is still some warnings from pylint, but they are not worth fixing in my opinion.


I also added commands to tasks.py to switch between using only Delaunay triangulation and using a minimum spanning tree too. The minimum spanning tree uses Deulanay triangulation, so it might not result in a "true" minimum spanning tree, but I think this is better since it ensures that the amount of paths going through rooms is minimal. Then I made sure that even when users tamper with configs, be it using commands or altering the config.txt file, the system uses hardcoded default values.


Lastly I added more docstrings to my files and improved documentation.


This week's progress took 11 hours.