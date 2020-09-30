# This file contains the classes for reading the text file and generating a DFA
# Hasta ahora considero tres clases.
# 1. Automata o DFA, procesa basado en su tabla de transición
# 2. Minimizador. Recibe un Automata y devuelve otro automata minimizado.
# 3. File reader. Lee el .txt y extrae los datos para un autómata.

import re
# para parseo de los archivos de texto

class Automata(object):
    # this class is not finished yet.
    def __init__(self, states, symbols, initial, final, table):
        """states is an array, set of states of M
            symbols is an array, the alphabet of M
            initial is an int, the number id of initial state of M
            final is an array, the number id's of final states of M"""
        self.states = states
        self.initial = initial
        self.final = final
        self.table = table

    def minimize(self):
        """minimizes the transition table, if possible"""

    def process(self, string):
        """processes a given string.
        returns true if the string is accepted, false otherwise"""


class FileReader(object):
    """The FileReader class is used to read text files and extract the Automata's elements from it
        It's main function is to parse the states, """

    def addEntry(self, table, state, symbol, result):
        """state is a string indicates state's row in table
            symbol is a char indicates key of nested dict
            result is a string indicates the resulting state after processing char
            """
        table[state][symbol] = result

    def empty_table(self, states, alphabet):
        """initializes a dictionary of the type: {state: {character: newState} }
            represents the transition table"""
        table = {}
        for s in states:
            table[s] = {}
            for char in alphabet:
                table[s][char] = 'null'
        return table

    def readFile(self, filename):
        """generates the transition table from the given file"""
        f = open(filename, "r", encoding="UTF-8")

        data = f.readlines()
        file_length = len(data)

        # parse characteristics of automata
        states = data[0].rstrip().split(',')
        alphabet = data[1].rstrip().split(',')
        initial = data[2].rstrip()
        final = data[3].rstrip().split(',')

        # initialize an empty table
        print(states)
        table = self.empty_table(states, alphabet)

        #parse the transitions and populate the table
        for i in range(4, file_length):
            line = data[i].rstrip()
            args = re.split(',|=>|\n', line)
            print(args)
            self.addEntry(table, args[0], args[1], args[2])

        print(table)

        f.close()

        return (states, alphabet, table, initial, final)

protoDFA = FileReader.readFile("test1.txt")