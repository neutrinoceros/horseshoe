#!/usr/bin/python
#-*-coding:utf-8-*-

from Planet import *
from SolarSystem import *
import pylab as pl
import time

framelim = 2.


print "---------------------------------------"
print "Initializing..."
sun     = Planet('The Mighty Sun', mass=1.,   coords=[0.,0],    color='yellow')
jup     = Planet('Jupiter',        mass=9e-4, coords=[1.,0.],   color='orange')
vulcain = Planet('Vulcain',        mass=1e-6, coords=[0.,0.95], color='blue',isTest=True) 

sys     = SolarSystem ([sun, jup, vulcain])
sys.setKeplerianMotion()
print "System is set in Keplerian motion !"



#=======================================================
#                Running/plotting loop
#=======================================================
fig,(ax0,ax1,ax2) = pl.subplots(ncols=3, figsize = (18,5))
titles = ["Inertial frame","Jupiter-centered frame","Jupiter co-rotating frame"]

for ax in fig.axes :
    ax.set_aspect('equal')

pl.ion()
pl.show()

for i in range(int(1e5)) :
    sys.walkOneStep(STEP*1e6)
    if i %4e2 == 0 :
        for ax,tit in zip(fig.axes,titles) :
            ax.cla()
            ax.set_title(tit)
            ax.set_xlim([-framelim, + framelim])
            ax.set_ylim([-framelim, + framelim])


        sys.plotto (ax0)
        sys.plotto (ax1, mode='centering' , center=jup)
        sys.plotto (ax2, mode='corotating', center=sun)
        
        for b in sys.bodies :
            b.traj.append([b.pos[0],b.pos[1]])
            if i == 0 : 
                b.traj.tab = np.delete(b.traj.tab,(0),axis=0)
            b.traj.plotto(ax0)

        pl.draw()
        #time.sleep(0.1)
        

pl.ioff()
raw_input('press anykey to quit     ')
