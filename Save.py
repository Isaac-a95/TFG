#--------------------------------------------
#		Save.py
# This module saves the current state as a plot,
# or a ASCII file (TODO). It can add different
# plots, that can be set at Parameters.py (eg.
# an analytic solution)
#
#--------------------------------------------

import shutil
import os
import numpy as np
import time

import Grid
import Parameters as par
import Variables as var

# ------------------ PLOT ----------------------

#fig = plt.figure()
#ax = fig.add_subplot(111)
#line1, = ax.plot(z, rho)
print 'Loading Save..'

# Create results folders
if not os.path.exists(par.FolderName):
   os.makedirs(par.FolderName)
   os.makedirs(par.FolderName + '/RESULTS')
   os.makedirs(par.FolderName + '/RESULTS_DAT')
  

ThereIsSettings = os.path.exists(par.FolderName+'/Settings.py')
ThereIsParameters = os.path.exists(par.FolderName+'/Parameters.py')

if ThereIsSettings or ThereIsParameters:
   print '###### WARNING ######'
   print 'There is already a previous simulation stored at ' + par.FolderName
   des = raw_input('Do you want to overwrite it? ([y]/n)')
   fh = open(par.FolderName + '/log.txt', 'w')
   fh.write('#Starting simulation\n')
   fh.close()
   if des ==  'n':
      exit()

shutil.copy2('Settings.py', par.FolderName)
shutil.copy2('Parameters.py', par.FolderName)

ZeroTime = time.clock()
"""
plotCounter = 0

f, axs = plt.subplots(4+par.PlotCharacteristics,1, sharex=True)
f.set_size_inches(18.5, 10.5)
axs[0].set_title(r"$\rho$")
rho_line, = axs[0].plot(Grid.z, var.rho)
axs[1].set_title("v")
v_line, = axs[1].plot(Grid.z, var.v)
axs[2].set_title("P")
P_line, = axs[2].plot(Grid.z, var.P)
axs[3].set_title("T")
T_line, = axs[3].plot(Grid.z, var.T)


itTextStr = 'IT: 0'
tTextStr = 't: 0 s'

itText = f.text(0.8, 0.9, '', fontsize=14)
tText = f.text(0.15, 0.9, '', fontsize= 14)

itText.set_text(itTextStr)
tText.set_text(tTextStr)

if par.PlotCharacteristics:
   axs[4].set_title('Characteristic lenght')
   if par.ThermalDiffusion:
      Thermal_tau, = axs[4].plot([],[], 'k')
      Thermal_tau.set_xdata(Grid.z)
   if par.RadiativeLoss:
      Losses_tau, = axs[4].plot([],[], 'g')
      Losses_tau.set_xdata(Grid.z)
   Dynamic_tau, = axs[4].plot([],[], 'b')
   Dynamic_tau.set_xdata(Grid.z)
   axs[4].semilogy()
   axs[4].set_xlabel(par.xlabel)
   axs[4].set_ylabel(r'$s$')
else:
   axs[3].set_xlabel(par.xlabel)


FreeFall_line, = axs[1].plot([],[], "r--")

SoundSpeed_line, = axs[1].plot([],[], "r--")
MaxAmp_line, = axs[1].plot([],[], "k--")

rhoAna_line, = axs[0].plot([],[], "k--")
vAna_line, = axs[1].plot([],[], "k--")
PAna_line, = axs[2].plot([],[], "k--")
TAna_line, = axs[3].plot([],[], "k--")

axs[0].set_ylabel(par.ylabels[0])
axs[1].set_ylabel(par.ylabels[1])
axs[2].set_ylabel(par.ylabels[2])
axs[3].set_ylabel(par.ylabels[3])

#scientific notation for v axis
axs[1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))

SoundSpeedProf_line, = axs[1].plot([],[], 'g--')

if par.FreeFallLine:
   FreeFall_line.set_xdata([Grid.z[0], Grid.z[-1]])

if par.SoundSpeedLine:
   SoundSpeed_line.set_ydata([0.,2.])
   MaxAmp_line.set_xdata([0.,1.])

if par.SoundSpeedProfile:
   SoundSpeedProf_line.set_xdata(Grid.z)
   
if par.SoundSpeedAnalytic or par.IsothermalAnalytic or par.ThermalAnalytic:
   rhoAna_line.set_xdata(Grid.z)
   vAna_line.set_xdata(Grid.z)
   PAna_line.set_xdata(Grid.z)
   TAna_line.set_xdata(Grid.z)


if par.rhoAxis != []:
   axs[0].set_ylim(par.rhoAxis)
if par.vAxis != []:
   axs[1].set_ylim(par.vAxis)
if par.PAxis != []:
   axs[2].set_ylim(par.PAxis)
if par.TAxis != []:
   axs[3].set_ylim(par.TAxis)
  
for i in range(4):
   if par.logScale[i]==True:
      axs[i].semilogy()

axs[0].set_xlim(Grid.z[0],Grid.z[-1])


if par.PlotFile:
   z_dat, rho_dat, p_dat, T_dat = np.loadtxt(par.FileToPlot, unpack=True)
   axs[0].plot(z_dat, rho_dat, 'k--')
   axs[2].plot(z_dat, p_dat, 'k--')
   axs[3].plot(z_dat, T_dat, 'k--')
"""

def Plot():
   global plotCounter
   """
   rho_line.set_ydata(var.rho)
   v_line.set_ydata(var.v)
   P_line.set_ydata(var.P)
   T_line.set_ydata(var.T)

   itText.set_text('IT: %d'%par.it)
   tText.set_text('t: %.2f s'%par.tt)

   if par.FreeFallLine:
      vff = par.g*par.tt
      FreeFall_line.set_ydata([vff, vff])

   if par.SoundSpeedLine:
      c_s = np.sqrt(par.gamma)   #rho=p0=1
      x = c_s*par.tt 
      SoundSpeed_line.set_xdata([x, x])
      MaxAmp = np.max(var.v)
      MaxAmp_line.set_ydata([MaxAmp, MaxAmp])
      
   if par.SoundSpeedProfile:
      c_s = np.sqrt(par.gamma*var.P/var.rho)
      SoundSpeedProf_line.set_ydata(c_s)
      
   # This can be further improved...
   if par.SoundSpeedAnalytic:
      rhoAna, vAna, PAna, TAna = Analytic.SoundWaves(sets.argsIC, par.tt)
      rhoAna_line.set_ydata(rhoAna)
      vAna_line.set_ydata(vAna)
      PAna_line.set_ydata(PAna)
      TAna_line.set_ydata(TAna)  
 
   if par.IsothermalAnalytic:
      rhoAna, vAna, PAna, TAna = Analytic.Isothermal(sets.argsIC, par.tt)
      rhoAna_line.set_ydata(rhoAna)
      vAna_line.set_ydata(vAna)
      PAna_line.set_ydata(PAna)
      TAna_line.set_ydata(TAna)     
 
   if par.ThermalAnalytic:
      rhoAna, vAna, PAna, TAna = Analytic.GaussianThermal(sets.argsIC, par.tt)
      rhoAna_line.set_ydata(rhoAna)
      vAna_line.set_ydata(vAna)
      PAna_line.set_ydata(PAna)
      TAna_line.set_ydata(TAna)
      
   if par.PlotCharacteristics:
      if par.ThermalDiffusion:
         tau = Characteristics.Thermal()
         Thermal_tau.set_ydata(tau)
      if par.RadiativeLoss:
         tau = Characteristics.Radiative()
         Losses_tau.set_ydata(tau)
    
      tau = Characteristics.DensityChanges()
      Dynamic_tau.set_ydata(tau) 
      #Re-scale axis
      axs[4].relim()
      axs[4].autoscale_view()  
   
   
   if par.SaveToFile and plotCounter%par.SaveToFileRatio==0 :
      dataToSave = np.array([Grid.z, var.rho, var.v, var.T])
      if par.PlotCharacteristics:  
         if par.ThermalDiffusion:
            tau_T = Characteristics.Thermal()
            dataToSave = np.append(dataToSave, [tau_T], axis=0)
         if par.RadiativeLoss:
            tau_R = Characteristics.Radiative()
            dataToSave = np.append(dataToSave, [tau_R], axis=0)
         print 'Saving to file..'
   """
   
   np.save(par.FolderName + '/RESULTS_DAT/%.20f.dat'%par.tt, np.array([Grid.z, Grid.y, var.rho, var.vZ, var.vY, var.T]) ) 
      
   fh = open(par.FolderName + '/log.txt','a')
   fh.write(str(par.it) + ' ' + str(par.dt) + ' ' + str(par.tt) + ' ' + str(time.clock() - ZeroTime) + '\n')     
   fh.close()
      
   #plt.savefig(par.FolderName + '/RESULTS/%.20f.png'%par.tt, bbox_inches='tight')
   #plotCounter +=1




   
   





