import math as ma

def verifica_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

class Punto:
    def __init__(self,x,y,z):
        def imposta_proprietà():
            self.x=float(x)
            self.y=float(y)
            self.z=float(z)
            self.p='{},{},{}'.format(   self.x,
                                        self.y,
                                        self.z)
            self.pF='{},{},{}'.format(  round(self.x,3),
                                        round(self.y,3),
                                        round(self.z,3))
            return True

        self.valido=(       verifica_float(x)
                        and verifica_float(y)
                        and verifica_float(z)
                        and imposta_proprietà())

class Angolo:
    def __init__(self,angolo,tipo):
        def imposta_proprietà():
            self.rad =  (
                            verifica_float(angolo)
                        ) and (
                            (tipo=="rad" and float(angolo) )
                            or 
                            (tipo=="deg" and float(angolo)*ma.pi/180 )
                        )

            self.deg =  (
                            verifica_float(angolo)
                        ) and (
                            (tipo=="deg" and float(angolo) )
                            or 
                            (tipo=="rad" and float(angolo)/ma.pi*180 )
                        )
            return True

        self.valido = ( (  tipo=="deg" or tipo=="rad" )
                        and verifica_float(angolo)
                        and imposta_proprietà()
                      )

pippo=Punto(1/3,0.25,"1")
print(pippo.p)
