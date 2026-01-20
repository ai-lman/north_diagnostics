"""
Extract all data from the ddaq files and plot it. Both .tdms file must be saved in the data folder, but there is a possibility to change the path file 
at the beginning of the main program.
Usefull for further data treatment and save all usefull data in a .txt file.
Define shot number just after the main programm begins.
"""

#Import all usefull libraries
import nptdms
import scipy.optimize import curve_fit
from north_diagnostics.diagnostics import Probe
import matplotlib.pyplot as plt
import numpy as np

# Define all usefull functions
def read_machine_data():
  """
  Read the channels:  1 (Light sensor)
                      2 (Coil currents)
                      3 (Pressure sensor)
                      6 (LFS power)
                      7 (HFS power)
  to control machine parameters. Plotted in the main program and saved in a .txt files.
  """

def read_probe_data():
  """
  Read all the probes channels which are n_channel=n_probe+14. 
  Plotted in the main program and saved in a .txt files.
  """
  return

#Main programme: plot all machine and some probe data to verify that the shot looks fine
if __name__=="__main__":
  shot=9974
  path_to_file=
  file=
  

