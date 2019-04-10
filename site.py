
"""
Initially contributed by Lei Li, UT Austin
"""

class Site(object):
    """
    This class is to define 'Site' object.
    Properties included: 
     coords: coordinates of the site, used to calculate distance between sites thus update neighborlists
     site_type: i.e., 'Ce' or 'O'
     species: current species that occupies this site
     neighborlist: store first-nearest and the second-nearest neighbors
     reactinglist: store possible neighboring sites that can react with the current site. It should be updated when the spicies changed
    """

    def __init__(self, coords=np.array([]), site_type = None, species, neighborlist=[], reactinglist=[]):
        self.coords = coords
        self.site_type = site_type
        self.species = species
        self.neighborlist = neighborlist
  
    def set_neighborlist(self, neighborlist):  
        self.neighborlist = neighborlist  

    def set_species(self, species):
        self.species = species
