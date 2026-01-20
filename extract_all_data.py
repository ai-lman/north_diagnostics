"""
Extract all data from the ddaq files and plot it.
Usefull for further data treatment 
"""

#Import all usefull libraries
import north_diagnostics
from north_diagnostics.diagnostics import Diagnostic, Probe
import matplotlib.pyplot as plt
import numpy as np

# Define all usefull functions

#Main programme: plot all machine and some probe data to verify that the shot looks fine
if __name__=="__main__":
  shot=9974
  
