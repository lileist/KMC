"""
Initially contributed by Lei Li, UT Austin
"""
class State(object):
    """
    Define 'State' object.
    It should including all 'Site' information at current stage: occupation situation of all sites
    statenumber: used to distinguish states, define a function to idetify states
    sites: a list of site object
    """

    def __init__(self, statenumber, sites):
        self.statenumber = statenumber
        self.sites = sites
        self.sites_number = len(sites)
        self.transition_events = [] # A list of transition event

    def group_sites(self, species):
        return [site for site in self.sites if site.species == species]

    #TODO: Avoid get_neighborlist for each new state              
    def get_neighborlist(self):
        """
        A neighborlist with the following format will be returned
        [{'O':[{index, site1}, {index,site2}], 'Ce': [{index, site1}, {index, site2}]},
         {'O':[{index, site1}, {index,site2}], 'Ce': [{index, site1}, {index, site2}]},]
        """
        self.neighborlist = []
        for i in range(self.sites_number):
            center_site = self.sites[i]
            center_species = center_site.species
            self.neighborlist.append([{center_species: []}])
            self.others.append([])
            for j in range(self.sites_number):
                site_b = self.sites[j]
                if center_site == site_b:
                   continue
                if np.linalg.norm(center_site.coords - site_b.coords) <= 1.0 and center_species == site_b.species:
                   self.neighborlist[i][center_species].append({j:site_b})
                   continue
                if np.linalg.norm(center_site.coords - site_b.coords) <= 2.0 and center_species == site_b.species:
                   #Note: site at diagnal will be counted
                   self.neighborlist[i][site_b.species].append({j:site_b})
                   continue
        return self.neighborlist
 
    def set_state(self):
        #set_state with given infor

class Transition(object):
    """
    Define transition from one state to another state
    """
    def __init__(self, inital_state, final_state, rate):
        self.inital_state = initial_state
        self.final_state = final_state
        self.rate = rate
               
        
def search_possible_events(state, reactions):
    #iterate over each sites
    #A list of transition event
    transition_events = [] 
    neighborlist = state.get_neighborlist()
    sites = state.sites
    #TODO: need a global varialbe to record state number
    #TODO: Avoid dupicated states
    stateNumber = state.statenumber  

    #TODO: Refine algorithm
    for i in range(sites):
       curr_species = sites[i].species
       #Fetch all possible reactions when seeing one species.
       #TODO: It should only contain reactant, product and forward_rate
       reactionlist = reactions[curr_species]

       #Iterate over all neighborsites
       for key, neighborsites in neighborlist[i]:
           for index, neighborsite in neighborsites:
               for reaction in reactionlist:
                   if all([curr_species, neighborsite.species] in reaction.reactant):
                      #that means this reaction is possible to happen
                      #A transition event found, then constructuct new state and build the event
                      #TODO: Rule to construct the new state: reaction.product[0] takes the current site
                      #                                       reaction.product[1] takes the neighbor site
                      stateNumber += 1
                      new_sites = copy.deepcopy(sites)
                      #TODO: Add set_species function in 'Site' class
                      new_sites[i].set_species(reaction.product[0])
                      new_sites[index].set_species(reaction.product[1])
                      new_state = State(stateNumber, sites)
                      transition_events.append(Transition(state, new_state, reaction.forward_rate)) 
                      break
    return transition_events

