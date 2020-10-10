import re
from Automaton import Automaton
# This module contains the functions for reading the text file
# and retrieving the Automaton info in a functional approach.

def addEntry(table, state, symbol, result):
    """state is a string indicates state's row in table
        symbol is a char indicates key of nested dict
        result is a string indicates the resulting state after processing char
        """
    table[state][symbol] = result

def empty_table(states, alphabet):
    """initializes a dictionary of the type: {state: {character: newState} }
        represents the transition table"""
    table = {}
    for s in states:
        table[s] = {}
        for char in alphabet:
            table[s][char] = 'null'

    return table

def readFile(filename):
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
    table = empty_table(states, alphabet)

    #parse the transitions and populate the table
    for i in range(4, file_length):
        line = data[i].rstrip()
        args = re.split(',|=>|\n', line) # q2, a=>q3
        addEntry(table, args[0], args[1], args[2])

    print(table)

    f.close()

    return Automaton(states, alphabet, table, initial, final) # return an Automaton