from Automaton import Automaton
from FileReader import readFile
from Minimizer import Minimizer

# Se consideran tres clases.
# 1. Automata o DFA, procesa basado en su tabla de transición
# 2. Minimizador. Recibe un Automata y lo modifica directamente que estpe minimizado
# 3. File reader. Lee el .txt y extrae los datos para un autómata.


DFA = Automaton(*readFile("test1.txt"))        # the * operator separates the list into separate arguments
minimizer = Minimizer()

minimizer.set_Automaton(DFA)
minimizer.minimize()
DFA = minimizer.get_Automaton()
print(DFA)