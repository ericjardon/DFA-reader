from pprint import pprint
"""This module contains the Automaton class and its methods to process a given string.
    To view the information of the Automaton in console, use the show_table and __str__ methods"""

class Automaton(object):
    def __init__(self, states, symbols, table, initial, final):
        """states is an array, the set of states of M
            symbols is an array, the alphabet of M
            initial is a string, the name of initial state of M
            final is an array, the set of final states of M"""
        self.states = states
        self.initial = initial
        self.final = final
        self.table = table
        self.isMinimized = False
        # by default an Automaton will not be considered minimized upon initialization.


    def process(self, string):
        """Takes in a string, uses the extended transition function to process it.
            May print out the result to console. Lines are commented out for cleaning purposes.
            Returns a boolean indicating whether the given string is accepted by the DFA or not."""
        res = self.ext_d(self.initial, string)

        accepted = "" if (res in self.final)  else "NOT"
        print("M: d*(%s, %s) = %s" % (self.initial, string, res))
        print("The string is %s accepted" % accepted)

        return res in self.final


    def d(self, qi, symbol):
        """Simple Transition Function. Works as a helper to the Extended Transition Function.
            Takes in the starting state, the symbol to process.
            Returns the resulting state according to the transition table."""
        if (qi == 'null'):
            # By design of our transition table, a 'null' value indicates a sink state.
            return 'null'
        else:
            return self.table[qi][symbol]

    def ext_d(self, qi, string):
        """Extended Transition Function based on its recursive definition.
            Takes in a state, the string to process from that state, and recursively decomposes it"""

        # BASE CASES: empty string or single character
        if len(string) == 0:
            return qi
        if len(string) == 1:
            # use the simple transition function
            return self.d(qi, string)

        # RECURSIVE STEP:   *d(qi, ua) = d(d*(qi, u), a)
        return self.d(self.ext_d(qi, string[:-1]), string[-1])


    def show_table(self):
        """Print the transition table to console using the pretty print library"""
        pprint(self.table)

    def __str__(self):
        """Print general information of the automaton to the console"""
        info = "Automaton M: \n" \
              "\tstates = " + str(self.states) + "\n" \
              "\tinitial = " + str(self.initial) + "\n" \
              "\tfinal = " + str(self.final) + "\n" \
                "\tminimized: " + str(self.isMinimized)
        return info