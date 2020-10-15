from FileReader import readFile
from Minimizer import Minimizer

### READ AUTOMATON ###
DFA = readFile("test2.txt")
# print(DFA)
# DFA.show_table()

### MINIMIZE AUTOMATON ###
minimizer = Minimizer()
DFA = minimizer.minimize(DFA)
print(DFA)
DFA.show_table()

### TEST STRING ACCEPTANCE  ###

#DFA.process('')