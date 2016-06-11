import numpy as np
from constants import *
from horseshoemaths import *


class Trajectory :
    def __init__(self,dimension=2, ls='--',color='k') :
        self.tab = np.empty((1,dimension))
        self.dim = dimension
        self.ls  = ls
        self.color = color

    def append(self, arg, init=False) :
        self.tab = np.vstack([self.tab,arg])
        if init :
            self.tab = np.delete(self.tab,(0),axis=0)


    def plotto(self, ax, times, mode = 'inertial', center = 'origin', refradius = 1.) :

        if center == 'origin' :
            centerpos = np.zeros(2)
        else : 
            centerpos = center.pos

        if mode in ["centering","corotating"] :
            copy =  Trajectory(dimension=self.dim, ls= self.ls, color=self.color)
            #centering
            for row,t in zip(self.tab,times) : 
                rowc = get_centered(row, centerpos)
        
                if mode == 'corotating' :
                    #... rotating
                    angleH = np.sqrt(GCST*center.mass/refradius**3)*t
                    rowt = get_rotated(rowc,angleH)
                else :
                    rowt = rowc

                
                copy.append(rowt, (t==0))

            x,y = copy.tab[:,0],copy.tab[:,1]
    
        else :
            x, y = self.tab[:,0],self.tab[:,1]

        ax.plot(x,y,  ls=self.ls,color=self.color)
