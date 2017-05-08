#--------------------------------------------
#		Analytic.py
# This module defines some analytic functions
# to compare them to numerical solutions. They
# take as arguments the same as the initial
# condition plus the time
#
#--------------------------------------------

import numpy as np

import Grid
import Parameters as par
import Settings as sets

def SoundWaves(args, t):
  rho0 = args[0]
  A = args[1]
  p0 = args[2]
  Nwav = args[3]

  #K = Nwav*2*np.pi/(Grid.zf-Grid.z0)
  c_s = np.sqrt(par.gamma*p0/rho0)
  phas = Nwav * 2. * np.pi *(Grid.z-par.z0)/(par.zf-par.z0)
  
  # v = w/k -> w = v*k
  w = c_s*Nwav*2.*np.pi/(par.zf-par.z0)
  
  rhoAna = rho0*(1. + A*np.cos(phas - w*t) )
  vAna =  c_s*A*np.cos(phas - w*t)
  PAna = p0*(1. + par.gamma*A*np.cos(phas - w*t) )

  return rhoAna, vAna, PAna