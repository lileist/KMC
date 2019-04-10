from site import Site

def readsites(filename):
    """
    Read in sites defined in format:
    Ce    O     Ce    O
    O     Ce    O     Ce
    Ce    O     Ce    O
    O     Ce    O     Ce
    """
    sites=[]
    sites_infor = np.loadtxt(filename)
    (row, column) = sites_infor.shape
    for i in range(row):
      for j in range(column):
         sites.append(site(coords=np.array([i, j]), site_type= sites_infor[i][j], neighborlist=[], diffusionlist=[])
    return sites

def readreactions():
    """
    Example inputs:
    CO2           + site(O)        => CO2-O_site(O);      forwardbarrier, backwardbarrier
    CO2-O_site(O) + CH3OH_site(Ce) => CH3O-COO_site(O);   forwardbarrier, backwardbarrier 
    """

    return reactions

