from collections import defaultdict
from pprint import pprint
# The transition table of an Automaton is a dictionary of state-keys, each row represented by a subdictionary of symbol:result pairs.
# The Automaton table is a state-to-row mapping.
# # To find equivalent states we need to find states that are of the same type (final or non final) and who share the same row transitions.
# Solution is to flip our dictionary into a row-to-states mapping

class Minimizer():
    def __init__(self):
        self.ch = None
        self.Automaton = None

    def get_Automaton(self):
        return self.Automaton

    def set_Automaton(self, Automaton):
        self.Automaton = Automaton

    def restart_counter(self):
        self.ch = 'A'

    def minimize(self, Automaton):
        self.set_Automaton(Automaton)
        self.restart_counter()
        """Does the full minimization of the stored Automaton, directly modifying its table, initial and final states"""
        while self.Automaton.isMinimized == False:
            flipped, repeated = self.flip(self.Automaton.table)
            if len(repeated) == 0:
                print("No rows are repeated. finish")
                pprint(self.Automaton.table)
                self.Automaton.isMinimized = True
                # break
            else:
                redundant = False
                for key in repeated:
                # iterate over the repeated rows, checking if there is >1 state with that row value (same transitions).
                    print("States " + str(flipped[key]) + " have the same row: " + key)
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
                self.Automaton.isMinimized = True
                # break

        return self.Automaton


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

    def collapse_rows(self, r_states, areFinal):
        """Receives an array of redundant states,
            replaces all their rows with a single row,
            renames their occurrences in the automaton's table"""
        rowValues = self.Automaton.table[r_states[0]]
        rename = 'q' + self.ch
        print("Rename " + str(r_states) + " --> " + rename)
        self.ch = chr(ord(self.ch) + 1)
        for rs in r_states:
            # delete all redundant key:value pairs
            del self.Automaton.table[rs]

        # leave a single renamed row
        self.Automaton.table[rename] = rowValues

        # Rename all occurrences of redundant states in the remaining table rows
        for key, subdict in self.Automaton.table.items():
            for symbol, result in subdict.items():
                if result in r_states:
                    subdict[symbol] = rename

        print("Udating redundant states " + str(r_states))
        # Rename initial state if necessary
        if self.Automaton.initial in r_states:
            self.Automaton.initial = rename

        # Update final states if necessary
        if (areFinal):
            for rs in r_states:
                if rs in self.Automaton.final:
                    self.Automaton.final.remove(rs)
            self.Automaton.final.append(rename)

        self.updateStates()

    def updateStates(self):
        self.Automaton.states = []
        for key in list(self.Automaton.table):
            self.Automaton.states.append(key)