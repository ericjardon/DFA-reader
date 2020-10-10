# DFA-reader
**Integrative Practice Part 1** 

Bryan Alexis Monroy Álvarez A01026848  
Eric Andrés Jardón Chao A01376748

 ***   
 _Description_: A program that reads a transition table 
 from a text file and generates the corresponding Deterministic Finite Automaton.  
 Then it can also determine whether a given string is accepted or not by the DFA.   
 
###_Modules_:  
- FileReader: A functional-based module that contains functions for reading a text file given its name, 
and returns an instance of an Automaton given the information provided in the file's lines.
- Automaton: A class-based module that represents a Deterministic Finite Automaton.
Has as class attributes a list of states, a list of symbols, a string for the initial state and 
a list final states, and a transition
table represented as a nested dictionary. Has methods for processing a string and a print method.  
- Minimizer: A class-based module that contains methods for minimizing an Automaton. 
A Minimizer has an Automaton and its main method, _minimize()_, directly modifies the given Automaton's transition table,
 initial and final states in order to minimize it iteratively and returns it. It also has basic get and set methods for the Automaton. 