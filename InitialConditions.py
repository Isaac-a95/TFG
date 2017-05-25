#--------------------------------------------
#		InitialConditions.py
# This module defines the Initial Conditions 
# for the simulation. They are selected at
# Settings.py, and a "args" argument is passed,
# which is a list of the neccesary user defined
# parameters.
#
#--------------------------------------------


import numpy as np
import Grid
import Parameters as par
import Variables as var
import glob

# ------------------ INITIAL CONDITIONS --------

print 'Loading InitialConditions..'


def IsothermalEq(args):
  p0 = args[0]
  rho0 = args[1]
  
  P0 = p0*np.exp(-Grid.z/1.)
  var.rho = rho0*np.exp(-Grid.z/1.)
  var.momentum = var.momentum*0.
  var.energy = P0/(par.gamma-1.)


def SoundWaves(args):
  rho0 = args[0]
  A = args[1]
  p0 = args[2]
  Nwav = args[3]

  #K = Nwav*2*np.pi/(Grid.zf-Grid.z0)
  phas = Nwav * 2. * np.pi *(Grid.z-par.z0)/(par.zf-par.z0)
  
  var.rho = rho0*(1. + A*np.cos(phas) )
  
  c_s = np.sqrt(par.gamma*p0/rho0)
  vIn =  c_s*A*np.cos(phas)
  var.momentum = vIn*var.rho

  pIn = p0*(1. + par.gamma*A*np.cos(phas) )
  var.energy = pIn/(par.gamma-1.) + 0.5*var.rho*vIn*vIn


def GaussianTemperature(args):
  T0 = args[0]
  z0 = args[1]
  width = args[2]
  rho0 = args[3]
  
  
  exp = np.exp(-(Grid.z-z0)*(Grid.z-z0)/(4*width))
  var.rho = rho0*np.ones(Grid.z.shape)
  var.momentum = var.momentum*0.
  var.energy = (1.+T0*exp)*var.rho*par.cv
  if par.SpitzerDiffusion:
    var.kappa = par.ct*np.ones(Grid.z.shape)*(1.+T0*exp)**(5./2.)
  else: 
    var.kappa = par.ct*np.ones(Grid.z.shape) #*exp #np.ones(Grid.z.shape)
  
  
def ReadICFromFile(args):
   print "Loading IC from " + args[0]
   FileName = args[0]
   f = open(FileName)
   f.readline()     #Line containing number of elements
   refs = f.readline().split()
   T_ref = float(refs[1])
   rho_ref = float(refs[2])
   mu = float(refs[3])
   g = float(refs[4])
   R = float(refs[5])
   f.close()
   
   par.R = R
   par.mu = mu
   par.g = -g
   par.Computecv()
   #print par.R, par.mu, par.g, par.cv
   
   T_data, rho_data = np.loadtxt(FileName, skiprows=2, usecols=(1,2), unpack=True)

   var.rho = rho_data*rho_ref
   var.energy = var.rho*T_data*T_ref*par.cv
   var.momentum = var.momentum*0.
   var.kappa = par.ct*(T_data*T_ref)**(5./2.)
   
   
def RestartFromFile(args):
   print "Restarting simulation..."
   files = glob.glob(args[0]+'/*.dat')
   files.sort()
   
   last_it = files[-1]

   f = open(last_it)
   refs = f.readline().split()
   mu = float(refs[1])
   g = abs(float(refs[2]))
   R = float(refs[3])
   f.close()   
   print mu, R, g
   par.R = R
   par.mu = mu
   par.g = -g
   par.Computecv()
   
   rho_data, v_data, T_data = np.loadtxt(last_it, skiprows=1, usecols=(1,2,3), unpack=True)
  
   var.rho = rho_data
   var.energy = var.rho*T_data*par.cv + 0.5*var.rho*v_data*v_data
   var.momentum = v_data*var.rho
   var.kappa = par.ct*(T_data)**(5./2.)
