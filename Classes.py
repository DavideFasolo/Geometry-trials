import math as ma

class Punto:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)
    self.punto='{},{},{}'.format(self.x,
                                self.y,
                                self.z)
    self.puntoF='{},{},{}'.format(round(self.x,3),
                                  round(self.y,3),
                                  round(self.z),3)


pippo=Punto(1/3,1,0.5)
print(pippo.puntoF)
