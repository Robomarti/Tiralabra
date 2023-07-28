import sys
import logic.automata
n=0
 
for argument in sys.argv:
	n+=1
	print(argument, n)
	
cg = logic.automata.CaveGenerator()
cg.generate_map()
cg.print_map()