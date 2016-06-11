#!/usr/bin/python
#-*-coding:utf-8-*-

from pybox import *
from Planet import *
from SolarSystem import *
import pylab as pl
import time


args = get_script_args()
svgdirectory = args[0]


print "---------------------------------------"
print "Initializing..."
sun     = Planet('The Mighty Sun', mass=1.,   coords=[0.,0],    color='yellow')
jup     = Planet('Jupiter',        mass=9e-4, coords=[1.,0.],   color='orange')
vulcain = Planet('Vulcain',        mass=1e-6, coords=[0.,0.95], color='blue',isTest=True) 

sys     = SolarSystem ([sun, jup, vulcain],rep=svgdirectory)
sys.setKeplerianMotion()
print "System is set in Keplerian motion !\n"



#         main loop
#===========================

for i in range(NMAX) :
    if i %4e2 == 0 :
        sys.write()
        for b in sys.bodies :
            b.traj.append([b.pos[0],b.pos[1]], (i==0))

    sys.walkOneStep(STEP)
    clearLastLine()
    print "computing... {} %".format(str(round(float(i+1)/NMAX*100.,2))) 
