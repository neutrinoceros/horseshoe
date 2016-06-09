from Planet import *
from SolarSystem import *
import pylab as pl
import time

framelim = 1.5

sun     = Planet('The Mighty Sun', mass=1., coords=[0.,0],                   color='yellow')
jup     = Planet('Jupiter',        mass=9e-4, coords=[1.,0.], color='orange'
#                 , isTest=True
             )

vulcain = Planet('Vulcain',        mass=1e-6, coords=[0.,0.99], color='blue' 
                 ,isTest=True
             ) 

sys     = SolarSystem ([sun, jup, vulcain])
sys.setKeplerianMotion()


#raw_input()
#print jup.vx, jup.vy



print "all went well !"

fig,(ax0,ax1,ax2) = pl.subplots(ncols=3, figsize = (18,5))

pl.ion()
pl.show()
for i in range(int(1e7)) :
    sys.walkOneStep(STEP*1e5)
    if i %4e2 ==0 :
        for ax in fig.axes :
            ax.cla()
            ax.set_xlim([-framelim, + framelim])
            ax.set_ylim([-framelim, + framelim])

        sys.plotto         (ax0)
        sys.plotCenteredto (ax1, center=jup)
        sys.plotRotatingto (ax2, center=sun)
        pl.draw()
        #time.sleep(0.1)
pl.ioff()
raw_input()
