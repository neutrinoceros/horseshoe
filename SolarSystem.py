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


    def plotto(self, ax) :
        xxx = []
        yyy = []
        ccc = []
        sss = []
        for b in self.bodies :
            xxx.append(b.pos[0]     )
            yyy.append(b.pos[1]     )
            ccc.append(b.color      )
            sss.append(b.visual_radius)
        ax.scatter(xxx,yyy,s=sss,c=ccc)

    def plotCenteredto(self, ax, center) :
        xxx = []
        yyy = []
        ccc = []
        sss = []
        for b in self.bodies :
            xxx.append(b.pos[0]-center.pos[0])
            yyy.append(b.pos[1]-center.pos[1])
            ccc.append(b.color      )
            sss.append(b.visual_radius)
        ax.scatter(xxx,yyy,s=sss,c=ccc)

    def plotRotatingto(self, ax, center, refradius=1.) :
        #not done
        xxx = []
        yyy = []
        ccc = []
        sss = []
        angleH = np.sqrt(GCST*center.mass/refradius**3)*self.physicalTime

        for b in self.bodies :
            #centering
            x1 = b.pos[0] - center.pos[0]
            y1 = b.pos[1] - center.pos[1]
            #... rotating
            x2 = x1 * np.cos(-angleH) - y1 * np.sin(-angleH)
            y2 = x1 * np.sin(-angleH) + y1 * np.cos(-angleH)
            xxx.append(x2)
            yyy.append(y2)
            ccc.append(b.color)
            sss.append(b.visual_radius)
        ax.scatter(xxx,yyy,s=sss,c=ccc)
