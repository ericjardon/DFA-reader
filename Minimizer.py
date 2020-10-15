from collections import defaultdict
from pprint import pprint
"""This module contains the Minimizer class. The principal method is minimize(), which receives an instance
    of an Automaton and returns a minimized Automaton. 
    When given an Automaton to minimize, a Minimizer stores it for easier management;
    i.e. updating the table, initial, final and states lists."""

class Minimizer():
    def __init__(self):
        self.ch = None      # character counter for renaming
        self.Automaton = None       # automaton to minimize

    def get_Automaton(self):
        return self.Automaton

    def set_Automaton(self, Automaton):
        self.Automaton = Automaton

    def restart_counter(self):
        self.ch = 'A'


    def minimize(self, Automaton):
        """Take in an instance of Automaton,
            Returns an minimized Automaton with an updated transition table, initial and final states.
            Uses helper functions: flip() for inverting the table's dictionary at each iteration
             and collapse_rows() for replacing redundant rows with a single condensed row in the original table."""
        self.set_Automaton(Automaton)
        self.restart_counter()

        while True:
            # At each step, flip the current transition table to determine repeated rows.
            flipped, repeated = self.flip(self.Automaton.table)

            redundant = False
            # boolean to determine if there are equivalent states minimizable. Assume false

            # For each repeated row, find if there are equivalent states and collapse their rows in the original table.
            for key in repeated:
                # print("States " + str(flipped[key]) + " have the same row: " + key)
                final = []
                nonfinal = []
                for state in flipped[key]:
                    # separate the redundant states into final and non-final arrays
                    if state in self.Automaton.final:
                        final.append(state)
                    else:
                        nonfinal.append(state)
                # Check both arrays; if there is more than 1 state, indicate redundancy and collapse their rows
                if len(final)>1:
                    self.collapse_rows(final, True)
                    redundant = True
                if len(nonfinal)>1:
                    self.collapse_rows(nonfinal, False)
                    redundant = True

            if not redundant:
                # Break the cycle when there are no equivalent states left.
                break

        self.updateStates()
        self.Automaton.isMinimized = True
        return self.Automaton


    def flip(self, table):
        """Given a transition table's dictionary, generate the flipped dictionary of the form:
        {'qaqb': ['q0','q1',...'qn']}, that shows which states have the same transition row.
        Since we are using nested dictionaries we create keys as the concatenation of the values
         of the original row (subdictionary).
         Returns the flipped dictionary and a list of the repeated rows"""
        repeatedRows = []
        flipped = defaultdict(dict)

        for key, subdict in table.items():
            # iterate over the rows of the table and create the keys for each unique row
            rowKey = ''
            for s in subdict.values():      # returns the values in same order as keys e.g. a, b
                rowKey += s
            if rowKey not in flipped:
                flipped[rowKey] = [key]
            else:
                # if the key already exists, the row is repeated.
                flipped[rowKey].append(key)     # Add the state to the list of states with that row
                repeatedRows.append(rowKey)     # Add the row key to the repeated rows array
                
        return dict(flipped), repeatedRows


    def collapse_rows(self, r_states, areFinal):
        """A helper function that modifies the transition table;
            receives an array of redundant states names (r_states),
            and a boolean indicating whether to update the list of final states (areFinal);
            erases their rows from the dictionary and
            replaces with a single 'condensed' row, then
            renames all the redundant states' occurrences in the original table.
            Updates the initial state if necessary.
            Does not return anything"""

        rowValues = self.Automaton.table[r_states[0]]       # save the value of the rows to be collapsed
        rename = 'q' + self.ch      # obtain a new name for the condensed row
        self.ch = chr(ord(self.ch) + 1)     # increment the character counter

        # print("Rename " + str(r_states) + " --> " + rename)

        for rs in r_states:
            # delete all redundant states from the transition table
            del self.Automaton.table[rs]

        # insert the new condensed row into the table
        self.Automaton.table[rename] = rowValues

        # print("Udating redundant states " + str(r_states))

        # Rename all occurrences of redundant states in the remaining table rows,
        for key, subdict in self.Automaton.table.items():
            for symbol, result in subdict.items():
                if result in r_states:
                    subdict[symbol] = rename

        # Updating the automaton's initial and final states if necessary
        if self.Automaton.initial in r_states:
            self.Automaton.initial = rename

        if (areFinal):
            for rs in r_states:
                if rs in self.Automaton.final:
                    self.Automaton.final.remove(rs)
            self.Automaton.final.append(rename)


    def updateStates(self):
        """Simple helper function that updates the list of states based on the transition table's keys.
            This function is called only when all minimization has been finished."""
        self.Automaton.states = []
        for key in list(self.Automaton.table):
            self.Automaton.states.append(key)