class Automaton(object):
    def __init__(self, states, symbols, table, initial, final):
        """states is an array, set of states of M
            symbols is an array, the alphabet of M
            initial is an int, the number id of initial state of M
            final is an array, the number id's of final states of M"""
        self.states = states
        self.initial = initial
        self.final = final
        self.table = table
        self.isMinimized = False


    def process(self, string):
        """processes a given string."""

        res = self.ext_d(self.initial, string)
        accepted = "" if (res in self.final)  else "NOT"

        print("M: d*(%s, %s) = %s" % (self.initial, string, res))
        print("The string is %s accepted" % accepted)

        return res in self.final


    def d(self, qi, symbol):
        """Simple transition function"""
        if (qi == 'null'):
            # checking for sink state
            return 'null'
        else:
            return self.table[qi][symbol]

    def ext_d(self, qi, string):
        """Extended transition function. Recursive implementation"""
        # BASE CASES
        if len(string) == 0:
            # empty string
            return qi
        if len(string) == 1:
            # a single character
            return self.d(qi, string)
        # STEP
        else:
            # *d(qi, ua) = d(d*(qi, u), a)
            return self.d(self.ext_d(qi, string[:-1]), string[-1])


    def __str__(self):
        info = "Automaton M: \n" \
              "\tstates = " + str(self.states) + "\n" \
              "\tinitial = " + str(self.initial) + "\n" \
              "\tfinal = " + str(self.final) + "\n" \
                                        "\tminimized: " + str(self.isMinimized)
        return info