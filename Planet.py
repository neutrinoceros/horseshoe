
import numpy as np
from Trajectory import *
from constants import *


class Planet :
    
    def __init__(self, name, mass=1., coords=[0.,0.], vel=[0.,0.], isTest=False, color='red') :
        self.mass          = mass
        self.pos           = np.array(coords)
        self.vel           = np.array(vel)
        self.force         = np.zeros(2)
        self.isTest        = isTest 
        self.visual_radius = 2000*mass**(1./3) #wip
        self.color         = color
        self.name          = name
        self.traj          = Trajectory(dimension=2, color = self.color)


    def getDistanceTo(self, otherBody) :
        direction = otherBody.pos - self.pos
        distance  = np.sqrt(np.sum(direction**2))
        return distance


    def getDirectionTo(self, otherBody) :
        direction   = otherBody.pos - self.pos
        norm        = np.sqrt(np.sum(direction**2))
        direction  /= norm
        return direction


    def setKeplerianMotion(self,attractor) :
        #attractor is of type Planet and supposedly inert
    
        d          = self.getDistanceTo(attractor)
        direction  = self.getDirectionTo(attractor)
        omK        = np.sqrt(GCST*attractor.mass/d**3)
        self.vel   = np.array([direction[1]*d*omK,-direction[0]*d*omK]) #imparfait

    
    def dumpforce(self) :
        self.force = np.zeros(2)


    def walk(self,dt) :
        self.pos  += self.vel             * dt 
        self.vel  += self.force/self.mass * dt
        self.dumpforce()
