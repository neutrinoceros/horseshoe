#!/usr/bin/python
#-*-coding:utf-8-*-



import numpy as np
import pylab as pl

from Planet import *
from SolarSystem import *
from pybox import *


framelim = 2.

args = get_script_args()
svgdir = args[0]

#         loading
#===========================

positions = np.loadtxt(svgdir+"/positions.dat")
masses    = np.loadtxt(svgdir+"/masses.dat"   )
times     = np.loadtxt(svgdir+"/time.dat"     )
names     =    readtxt(svgdir+"/names.dat"    )
colors    =    readtxt(svgdir+"/colors.dat"   )

currentpositions = [positions[-1:][0][2*n:2*n+2] for n in range(len(masses))] 

planets = [Planet(name, mass = m, coords = coo, color = c) for name,m,coo,c in zip(names, masses, currentpositions, colors)]
sys     = SolarSystem(planets)
sys.physicalTime = times[-1]


for i in range(len(positions)) :
    for n in range(len(masses)) :
        xy = positions[i,2*n:2*n+2]
        sys.bodies[n].traj.append(xy, (i==0))

for n in range(len(masses)) :
    print names[n]
    print sys.bodies[n].traj.tab[0,:]
    print currentpositions[n], 'VS', sys.bodies[n].traj.tab[-1,:]
    print "_________________"


#         plotting
#===========================



fig,(ax0,ax1,ax2) = pl.subplots(ncols=3, figsize = (18,5))
titles  = ["Inertial frame","Jupiter-centered frame","Jupiter co-rotating frame"]
modes   = ["inertial","centering","corotating"]
centers = ["origin", sys.bodies[1], sys.bodies[0]]

for ax in fig.axes :
    ax.set_aspect('equal')

pl.ion()
pl.show()

for ax,tit,mode,center in zip(fig.axes,titles,modes,centers) :
    ax.cla()
    ax.set_title(tit)
    ax.set_xlim([-framelim, + framelim])
    ax.set_ylim([-framelim, + framelim])

    sys.plotto (ax, mode=mode, center=center)
    for b in sys.bodies : 
        b.traj.plotto(ax, times, mode =mode, center = center)

            
pl.draw()
pl.ioff()


raw_input('press anykey to quit     ')
