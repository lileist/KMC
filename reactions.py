"""
Initially contributed by Lei Li, UT Austin
"""

class Reaction(object):
    """
    Define a reaction
    """

    def __init__(self, reactant, product, forward_rate, backward_rate):
        self.reactant = reactant
        self.product = product
        self.forward_rate = forward_rate
        self.backward_rate = backward_rate

#class Reactions(object):
#    """
#    Group reactions based on species:
#      find out all reactions that are relavent to species (key of the library)
#      i.e., {"CO2": [reaction1, reaction2],    #only reactant that different from CO2 is recorded
#             "CH3OH": [reaction1, reaction2]}
#    """
#    def __init__(self,reactions_lib = {}):

        
