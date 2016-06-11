from Planet import *
from horseshoemaths import *

from os import system
def gravity(b1,b2) :
    d         = b1.getDistanceTo(b2)
    intensity = GCST*b1.mass*b2.mass/d**2
    force     = intensity * b1.getDirectionTo(b2)
    return force


class SolarSystem :
    
    def __init__(self, planets,rep="") :
        if type(planets) == Planet :
            self.sun    = planets
        elif type(planets) == list :
            self.sun    = planets[0]
            self.bodies = planets
        self.physicalTime = 0.

        if rep!="" :
            system("mkdir {}".format(rep))
            with open(rep+"/masses.dat",'w') as fi :
                line = ""
                for b in self.bodies :
                    line += str(b.mass) + "    "
                fi.write(line)


    def setKeplerianMotion(self) :
        for body in self.bodies :
            if body != self.sun :
                body.setKeplerianMotion(self.sun)


    def walkOneStep(self,step) :
        
        index = 0
        for b1 in self.bodies :
            index += 1
            for b2 in self.bodies[index:] :
                force = gravity(b1,b2)
                if not b2.isTest :
                    b1.force +=  force
                if not b1.isTest :
                    b2.force -=  force
                    
            b1.walk(step)
        self.physicalTime += step


    def writeTo(self,filepos,filevel) :
        with open(filepos,'a') as fi :
            line = ""
            for b in self.bodies :
                line += str(b.pos[0]) + "    " +str(b.pos[1]) + "    "
            line += "\n"
            fi.write(line)

        with open(filevel,'a') as fi :
            line = ""
            for b in self.bodies :
                line += str(b.vel[0]) + "    " +str(b.vel[1]) + "    "
            line += "\n"
            fi.write(line)


    def plotto(self, ax, mode = 'inertial', center = 'origin', refradius = 1.) :
        xxx = []
        yyy = []
        ccc = []
        sss = []

        if center == 'origin' :
            centerpos = np.zeros(2)
        else : 
            centerpos = center.pos

        if mode == 'corotating' :
            angleH = np.sqrt(GCST*center.mass/refradius**3)*self.physicalTime

        for b in self.bodies :

            #centering
            x1,y1 = get_centered(b.pos, centerpos)

            if mode == 'corotating' :
                #... rotating
                x2,y2 = get_rotated(np.array([x1,y1]),angleH)
                xxx.append(x2)
                yyy.append(y2)

            else :
                xxx.append(x1)
                yyy.append(y1)

            ccc.append(b.color)
            sss.append(b.visual_radius)
        ax.scatter(xxx,yyy,s=sss,c=ccc)
