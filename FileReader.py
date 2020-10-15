import re
from Automaton import Automaton
""" This module contains the functions for reading the text file 
and producing an instance of Automaton in a functional approach. """

def addEntry(table, state, symbol, result):
    """ This function inserts an entry (result) to the transition table given the row (state) and the column (symbol).
        state is a string, indicating the starting state in transition table
        symbol is a string, indicating the symbol processed,
        result is a string, indicating the state after having processed the symbol."""
    table[state][symbol] = result


def empty_table(states, alphabet):
    """Given a list of states and an alphabet,
        this function creates and returns an empty dictionary of the type: {state: {character: newState}}
        Such dictionary represents the transition table"""
    table = {}
    for s in states:
        table[s] = {}
        for char in alphabet:
            table[s][char] = 'null'     # initialize with null values

    return table


def readFile(filename):
    """Takes the name of the .txt file,
        reads it and extracts the states, initial, final, the alphabet,
        and generates the transition table.
        Returns the corresponding Automaton object."""
    f = open(filename, "r", encoding="UTF-8")
    data = f.readlines()
    file_length = len(data)

    # parse basic characteristics of automata
    states = data[0].rstrip().split(',')
    alphabet = data[1].rstrip().split(',')
    initial = data[2].rstrip()
    final = data[3].rstrip().split(',')

    # initialize an empty transition table
    table = empty_table(states, alphabet)

    #parse the transitions and populate the table
    for i in range(4, file_length):
        line = data[i].rstrip()
        args = re.split(',|=>|\n', line) # q2, a=>q3
        addEntry(table, args[0], args[1], args[2])

    f.close()

    return Automaton(states, alphabet, table, initial, final)