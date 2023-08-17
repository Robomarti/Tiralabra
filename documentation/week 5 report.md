
added variation to room count and thus also added more variance to room sizes

this application is not meant to be used with values less than 10 anyway, so might as well block it

I did not understand the delaunay algorithm from the old articles I found online, so I pretty much copied the stackoverflow code from the stackoverflow source . But even after I fixed the bug in that post, this implementation still did not work correctly, so I deleted everything and implemented it myself using the pseudocode that I found in the wikipedia article that the publisher of the post used as a source. With the pseudocode I finally understood how to implement the Delaunay triangulation, and now it is working correctly.



This week's progress took 11 hours.

sources:

https://github.com/jmespadero/pyDelaunay2D

https://stackoverflow.com/questions/58116412/a-bowyer-watson-delaunay-triangulation-i-implemented-doesnt-remove-the-triangle

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm
