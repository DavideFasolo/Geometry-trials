import math as ma

def verifica_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

class Punto:
    def __init__(self,x,y,z):
        def errore_trigger():
            return not(
                    verifica_float(x)
                and verifica_float(y)
                and verifica_float(z)
            ) or False

        def errore_stringa():
            return (
                  (( verifica_float(x) and (" ")) or ("errX "))
                + (( verifica_float(y) and (" ")) or ("errY "))
                + (( verifica_float(z) and (" ")) or ("errZ "))
                )

        self.x=errore_trigger() and errore_stringa() or float(x)
        self.y=errore_trigger() and errore_stringa() or float(y)
        self.z=errore_trigger() and errore_stringa() or float(z)
        self.p='{},{},{}'.format(   self.x,
                                    self.y,
                                    self.z)
        self.pF='{},{},{}'.format(  errore_trigger() and errore_stringa() or round(self.x,3),
                                    errore_trigger() and errore_stringa() or round(self.y,3),
                                    errore_trigger() and errore_stringa() or round(self.z,3)
                                    )
        

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

        (   (   tipo=="deg" or tipo=="rad" )
            and verifica_float(angolo)
            and imposta_proprietà()
        )

pippo=Punto(1/3,0.25,"1a")
print(pippo.p)
