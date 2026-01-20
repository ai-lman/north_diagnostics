"""
Extract all data from the DDAQ and CRIO files and plot it. Both .tdms file must be saved in the data folder, but there is a possibility to change the path file 
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
def current_fit(U, I_isat, k_BT_e, U_f, e):
  """Function fitted by scipy"""
  return I_isat*(1-np.exp(e*(U-U_f)/k_BT_e))
  
def read_machine_data(shot, path_to_data):
  """
  Read the channels:  1 (Light sensor)
                      2 (Coil currents)
                      3 (Pressure sensor)
                      6 (LFS power)
                      7 (HFS power)
  to control machine parameters. Plotted in the main program and saved in a .txt files in the Data folder.
  """
  
  #Read data file
  file = nptdms.TdmsFile.read(f"{path_to_data}/CRIO{shot}.tdms")

  #Define the time interval of the study (the mask variable)
  t_start = 0
  t_end = machine_file['Data']['Time'][-1]
  mask = (machine_file['Data']['Time'][:] >= t_start) & (machine_file['Data']['Time'][:] <= t_end)

  #Extracting all machine parameters
  data[:,0] = t
  data = np.zeros((len(t), 6))
  head = 'Time; Light sensor; Coil current; Pressure sensor; LFS power; HFS power'
  data[:,0] = t*1E-3 # in s
  data[:,1] = machine_file['Data']['Light'][mask] # in ??; whatever, not for a quantitative analysis
  data[:,2] = machine_file['Data']['I_TF'][mask] # in A
  data[:,3] = machine_file['Data']['Pressure'][mask]*1E2 # in Pa
  data[:,4] = machine_file['Data']['LFSset'][mask]*450/3000 # in W
  data[:,5] = machine_file['Data']['HFSset'][mask]*450/3000 # in W
  return data

def read_probe_data(shot, path_to_data):
  """
  Read all the probes channels which are n_channel=n_probe+14. 
  Plotted in the main program and saved in a .txt files in the Data folder.
  """
  #Useful variables
  probe = {}
  data = np.zeros((len(t), 51))

  #Read data file
  for i in range(Probe.TOTAL_PROBES):
    probe[i] = Probe(path = path_to_data, shot = shot, number = i+1, caching = True)
    t = probe[i].time
    U = probe[i].bias_voltage
    I = probe[i].current
    if i==0:
      data = np.zeros((len(t), 51))
      data[:,0] = t
    if bias_type == 'density':
      data[:,i+1] = I/(0.61*e*np.sqrt(k_B*T_e_estim/m_i)*A)
    elif bias_type == 'temperature': 
      data[:,i+1] = T_e_estim
    else:
      print('WARNING: the bias type is not recognized')
  return data

#Main program: plot all machine and some probe data to verify that the shot "looks fine"
if __name__=="__main__":
  #Input parameters
  shot = 9974
  Z_gas = 4 #Helium
  bias_type = 'temperature' # Probes can be biased to measure 'density' or 'temperature' (the same bias is applied on every probe)
  path_to_data = './north_diagnostics/Data/'

  #Physical constants
  e = 1.602E-19 # in C
  k_B = 1.38E-23 # in J/K
  m_i = Z_gas*1.67E-27 # in kg

  #Experiment parameters
  A = 1E-6 # in m^2
  T_e_estim = 1.5*e/k_B # in K (the numerical value is in eV)

  #Generate the data
  machine_data = read_machine_data(shot, path_to_data)
  probe_data = read_probe_data(shot, path_to_data)
  
  #Saving all data in the Data folder
  head = 'Time; Light sensor; Coil current; Pressure sensor; LFS power; HFS power'
  np.savetxt(f"{path_to_data}/machine_data{shot}.txt", machine_data, delimiter='; ', header=head)
  head = 'Time; probes in the numerical order'
  np.savetxt(f"{path_to_data}/probe_data{shot}.txt", probe_data, delimiter='; ', header=head)
  
  #Plot and save figures
  path_to_figure = './north_diagnostics/Figure/'

