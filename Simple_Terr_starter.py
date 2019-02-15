# Read monthly surface forcing data for simple terrestrial ecosystem model
# Python script
# Mick Follows, Deepa Rao (2019)
# Class exercise, Feb 2019 

# For use in Jupyter Notebook include %matplotlib inline

import os #functions for working with file system
import sys
import glob
from pylab import *

import scipy as sp
import numpy as np
import numpy.ma as ma #masked arrays
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# print the current working directory
os.getcwd()
# change working directory to where input files are
os.chdir('/Users/Deepa/Documents/12.349:12.849/Terrestrial Biosphere/monthly-input-data')
# Backslash on Windows and Forward Slash on OS X and Linux

# read in the lat and lon coordinates of gridded data
lat = pd.read_table('latitudegrid.txt', header=None, skiprows=1)
lon = pd.read_table('longitudegrid.txt', header=None, skiprows=1)

# create meshgrid for plotting of lat and lon
lat, lon = np.meshgrid(lat.T,lon.T) #create meshgrid for plotting 

# import monthly avg climatology data as a numpy array

# use glob.glob to get an unordered list of filenames ('prefix_*.txt')
#print (glob.glob('*.txt')) #print all files in directory
T_files = glob.glob('SurfTair_*.txt')
precip_files = glob.glob('Precip_*.txt') 
sw_files = glob.glob('SurfSW_*.txt') 

# sort unordered list by filename (01, 02, 03 ...)
T_files.sort()
precip_files.sort()
sw_files.sort()

#  check files and array shape
#print(precip_files)
#print(lat.T.shape, lon.T.shape, T_Jan.shape)

# import monthly avg climatology data as a numpy array and mask missing values (1e36)
T = ma.masked_greater([np.loadtxt(f) for f in T_files], 1e36) #surface air temp (C)
precip = ma.masked_greater([np.loadtxt(f) for f in precip_files], 1e36) #precipitation (cm/month)
precip = precip * 12.0 / 100.0 #convert from (cm/month) to (m/yr)
sw = ma.masked_greater([np.loadtxt(f) for f in sw_files], 1e36) #incident short wave radiation - visible light (W m-2)

# test plot -- January temperature
plt.contourf(lon,lat,T[0].T) #note: transpose matrix to set matrix dimensions for plotting
plt.contourf(lon,lat, T[1].T, cmap = cm.coolwarm)
plt.title('Feb mean Surface Air Tempearture (C)')

# plot monthly T 
fig, ax = plt.subplots()
CS = ax.contourf(lon, lat, T[0].T, cmap=cm.coolwarm)
ax.set(xlim=[-180, 180], ylim=[-90,90],
       xlabel='Longitude', ylabel='Latitude',
       title='Monthly Mean Suface Air Temperature (C)')

# create landmask based on surface air T
landmask = np.ma.masked_where(T[0]>1e36, T[0])

# apply landmask on monthly sw data -- to only plot terrestrial data
sw_mask_0 = np.ma.masked_where(np.ma.getmask(landmask), sw[0]) #applies landmask on monthly[n] sw data

# plot monthly SW with landmask
fig, ax = plt.subplots()
J = ax.contourf(lon, lat, sw_mask_0.T, cmap=cm.coolwarm)
ax.set(xlim=[-180, 180], ylim=[-90,90],
       xlabel='Longitude', ylabel='Latitude',
       title='Jan SW (W/m2)')
    