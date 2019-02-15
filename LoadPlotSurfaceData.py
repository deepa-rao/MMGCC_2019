#!/usr/bin/env python
import sys
from pylab import *

mon = sys.argv[1]

lon = loadtxt('longitudegrid.txt')
lat = loadtxt('latitudegrid.txt')

#surface data:
T      = ma.masked_greater(loadtxt('SurfTair_' + mon + '.txt'), 1e36)
precip = ma.masked_greater(loadtxt('Precip_' + mon + '.txt'), 1e36)
sw     = ma.masked_greater(loadtxt('SurfSW_' + mon + '.txt'), 1e36)

#plot DIC:
figure()
pcolormesh(lon, lat, T)
colorbar()
xlabel('Longitude', fontsize=14)
ylabel('Latitude', fontsize=14)
title('Surface air temperature month ' + mon, fontsize=16)
show()
