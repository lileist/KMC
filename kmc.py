from io import readreactions, readsites
from state import State, Transition, search_possible_events
#define grids, two ways to define: 
#(1) generate grids first, then alternatively assign site_type
#(2) read from a input as in readgrids() 
sites = readsites()

#random initialize state with given concentration of reactants and products
state = sites.initialize()

 """
 readin reations and sorted to library in format:
 {"CO2":   [reaction1, reaction2, reaction3], # a list of reaction that involve CO2
  "CH3OH": [reaction1, reaction2, reaction3], # a list of reaction that involve CH3OH
 }
 """

reactions = readreactions()

for step in range(maxSteps):
  #Initialize state with given reactions
  state.initialize(reactions)

  #search for possible transition events
  #Information needed: states, reactions
  events = search_possible_events(state, reactions)   # a list of transition

  #build rate table and normalize it:
  rates = [event.rate for event in events]
  total_rate = sum(rates)
  rate_table = [rate/total_rate for rate in rates]
  #take KMC step and update state
  kmc.step()
  


