import numpy as np

class Trajectory :
    def __init__(self,dimension=2, ls='--',color='k') :
        self.tab = np.empty((1,dimension))
        self.dim = dimension
        self.ls  = ls
        self.color = color

    def append(self, arg) :
        self.tab = np.vstack([self.tab,arg])
#        print self.tab

    def plotto(self,ax) :

        x, y = self.tab[:,0],self.tab[:,1]
        if self.dim == 2 :
            ax.plot(x,y,  ls=self.ls,color=self.color)
        elif self.dim == 3 :
            z = self.tab[:,2]
            ax.plot(x,y,lz,s=self.ls,color=self.color)
