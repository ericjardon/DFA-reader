from FileReader import readFile
from Minimizer import Minimizer

### READ AUTOMATON (The test files must be in the root folder)###
DFA2 = readFile("test2.txt")
DFA = readFile("test1.txt")
# print(DFA)
# DFA.show_table()



### MINIMIZE AUTOMATON ###
minimizer = Minimizer()
DFA = minimizer.minimize(DFA)
print(DFA)
DFA.show_table()

## Testing string acceptance in test1.txt ##

inputString=input("Introduce a string to verify if is accepted: ")
DFA.process(inputString)

print ("-----------------------------------------------------------------------------------")

DFA2 = minimizer.minimize(DFA2)
print(DFA2)
DFA2.show_table()

## Testing string acceptance in test2.txt ##

inputString2=input("Introduce a string to verify if is accepted: ")
DFA2.process(inputString2)

