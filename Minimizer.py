from collections import defaultdict
from pprint import pprint
# The transition table of an Automaton is a dictionary of state-keys, each row represented by a subdictionary of symbol:result pairs.
# The Automaton table is a states-to-row mapping.
# # To find equivalent states we need to find states that are of the same type (final or non final) and share the same row value.
# We need to flip the dictionary into a row-to-states mapping.

class Minimizer():
    def __init__(self, Automaton):
        self.ch = 'A'
        self.Automaton = Automaton

    def set_Automaton(self, Automaton):
        self.Automaton = Automaton

    def restart_counter(self):
        self.ch = 'A'

    def minimize(self):
        """Receives an automaton.
            Does the full minimization of Automaton, modifying its table, initial and final states"""
        while True:
            flipped, repeated = self.flip(self.Automaton.table)
            pprint(flipped)
            if len(repeated) == 0:
                print("No rows are repeated. finish")
                pprint(self.Automaton.table)
                break
            else:
                redundant = False
                for key in list(flipped):
                # go through all keys of flipped, checking if there is >1 state with that row value (same transitions).
                    if len(flipped[key]) > 1:
                        print("Row " + key + " of table has redundant states: " + str(flipped[key]))
                        # separate the redundant states into final and non-final states
                        final = []
                        nonfinal = []
                        for state in flipped[key]:
                            if state in self.Automaton.final:
                                final.append(state)
                            else:
                                nonfinal.append(state)
                        # Collapse equivalent states that are final
                        if len(final)>1:
                            self.collapse_rows(final, True)
                            redundant = True
                        # Collapse equivalent states that are non-final
                        if len(nonfinal)>1:
                            self.collapse_rows(nonfinal, False)
                            redundant = True
            if not redundant:
                print("No equivalent states left. Finish")
                break


    def flip(self, table):
        # flipped is a dictionary: {'qaqb': ['q0','q1',...'qn']} that shows the states with the same transition row
        # the keys of flipped are the concatenated state names in the original transition table row
        repeatedRows = []
        flipped = defaultdict(dict)
        for key, subdict in table.items():
            # notice there are as many values as there are keys in the subdict.
            # we don't need the keys of the subdict to compare rows, only the values (the states)
            # construct a string with the concatenated values of the row (e.g. 'q1q2')
            rowKey = ''
            for s in subdict.values():
                # subdict.values() returns in order of the keys
                rowKey += s
            if rowKey not in flipped:
                flipped[rowKey] = [key]
            else:
                # the row is repeated in more than one state
                flipped[rowKey].append(key)
                repeatedRows.append(rowKey)

        return dict(flipped), repeatedRows

    def collapse_rows(self, states, areFinal):
        """Receives an array of redundant states,
            replaces all their rows with a single row,
            renames their occurrences in the automaton's table"""
        rowValues = self.Automaton.table[states[0]]
        rename = 'q_' + self.ch
        self.ch = chr(ord(self.ch) + 1)
        for rs in states:
            # delete all redundant key:value pairs
            del self.Automaton.table[rs]

        # leave a single renamed row
        self.Automaton.table[rename] = rowValues

        # Rename all occurrences of redundant states in the remaining table rows
        for key, subdict in self.Automaton.table.items():
            for symbol, result in subdict.items():
                if result in states:
                    subdict[symbol] = rename

        # Update initial state if necessary
        if self.Automaton.initial in states:
            self.Automaton.initial = rename

        # Update final states if necessary
        if (areFinal):
            for f in self.Automaton.final:
                if f in states:
                    self.Automaton.final.remove(f)
            self.Automaton.final.append(rename)