import numpy as np

import SourceTerm
import Parameters as par
import Variables as var
import Grid


def Thermal():
  DT_z = (var.T[1:]-var.T[:-1])/Grid.dz
  DT_z = np.append(DT_z, DT_z[-1])
  L = np.abs(var.T/DT_z)

  Chi = var.kappa/(var.rho*par.cv)
  DiffusionTime = (5./2. + 1.)*L*L/Chi

  return DiffusionTime, L


def Radiative():
  Lr = SourceTerm.computeRadiativeLosses()
  
  RadiationTime = var.P/(Lr*(par.gamma-1.))
  
  return RadiationTime


def Dynamic():
  c_s = np.sqrt(par.gamma*var.P/var.rho)
  SoundTime = Grid.dz/c_s
  
  return SoundTime

