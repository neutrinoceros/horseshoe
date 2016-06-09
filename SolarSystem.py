from Planet import *


def gravity(b1,b2) :
    d         = b1.getDistanceTo(b2)
    intensity = GCST*b1.mass*b2.mass/d**2
    force     = intensity * b1.getDirectionTo(b2)
    return force


class SolarSystem :
    
    def __init__(self, planets) :
        if type(planets) == Planet :
            self.sun    = planets
        elif type(planets) == list :
            self.sun    = planets[0]
            self.bodies = planets
        self.physicalTime = 0.


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


    def plotto(self, ax, mode = 'inertial', center = 'origin', refradius = 1.) :
        xxx = []
        yyy = []
        ccc = []
        sss = []


        if center == 'origin' :
            cx = 0.
            cy = 0.
        else : 
            cx = center.pos[0]
            cy = center.pos[1]
        if mode == 'corotating' :
            angleH = np.sqrt(GCST*center.mass/refradius**3)*self.physicalTime

        for b in self.bodies :
    
            #centering
            x1 = b.pos[0] - cx
            y1 = b.pos[1] - cy
            if mode == 'corotating' :
                #... rotating
                x2 = x1 * np.cos(-angleH) - y1 * np.sin(-angleH)
                y2 = x1 * np.sin(-angleH) + y1 * np.cos(-angleH)
                xxx.append(x2)
                yyy.append(y2)
            else :
                xxx.append(x1)
                yyy.append(y1)
                    
            ccc.append(b.color      )
            sss.append(b.visual_radius)
        ax.scatter(xxx,yyy,s=sss,c=ccc)
