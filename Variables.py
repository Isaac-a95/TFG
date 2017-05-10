#--------------------------------------------
#		Variables.py
# This module allocate and store the different
# arrays of conservative and primite variables,
# as well as other auxiliary arrays that depend
# on the mesh shape
#
#--------------------------------------------
import numpy as np

import Grid

# Conservative variables
rho = np.ones(Grid.z.shape)
momentum = np.zeros(Grid.z.shape)
energy = np.ones(Grid.z.shape)

# Conservative variables at last time step
lastrho = np.ones(Grid.z.shape)
lastmomentum = np.ones(Grid.z.shape)
lastenergy = np.ones(Grid.z.shape)

# Source arrays
momentumSource = np.zeros(Grid.z.shape)
energySource = np.zeros(Grid.z.shape)

# Primitive variables
T = np.ones(Grid.z.shape)
P = np.ones(Grid.z.shape)
v = np.ones(Grid.z.shape)

