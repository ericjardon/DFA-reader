from FileReader import readFile
from Minimizer import Minimizer


DFA =readFile("test2.txt")
print(DFA)
minimizer = Minimizer()

minimizer.minimize(DFA)
DFA = minimizer.get_Automaton()
print(DFA)