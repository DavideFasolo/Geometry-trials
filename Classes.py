import math as ma

def verificatipo(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

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
                                      round(self.z,3))

class Angolo:
    def __init__(self,angolo,tipo):

        self.valido =   (
                        (  tipo=="deg" or tipo=="rad" )
                        and
                        verificatipo(angolo)
                        and True
                        )

        self.rad =  (
                        verificatipo(angolo) and self.valido
                    ) and (
                        (tipo=="rad" and float(angolo) )
                        or 
                        (tipo=="deg" and float(angolo)*ma.pi/180 )
                    )

        self.deg =  (
                        verificatipo(angolo) and self.valido
                    ) and (
                        (tipo=="deg" and float(angolo) )
                        or 
                        (tipo=="rad" and float(angolo)/ma.pi*180 )
                    )

pippo=Angolo("1.0471975511965976","rad")
print(pippo.deg)
