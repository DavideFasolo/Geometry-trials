import math as ma

def verifica_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False

class Punto:
    def __init__(self,x,y,z):
        self.x=(verifica_float(x) and float(x)) or ("errore input X")
        self.y=(verifica_float(y) and float(y)) or ("errore input Y")
        self.z=(verifica_float(z) and float(z)) or ("errore input Z")
        def imposta_errore():
            a=verifica_float(x) or "errore input X "
            b=verifica_float(y) or "errore input Y "
            c=verifica_float(z) or "errore input Z "
            return a+b+c
        def imposta_proprietà(switch):
            self.p='{},{},{}'.format(   self.x,
                                        self.y,
                                        self.z)
            self.pF='{},{},{}'.format(  ((verifica_float(x) and round(self.x,3)) or self.x),
                                        ((verifica_float(y) and round(self.y,3)) or self.y),
                                        ((verifica_float(z) and round(self.z,3)) or self.z)
                                        )

        (   
                imposta_proprietà(True)
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


pippo=Punto("1a",0.25,"1")
print(pippo.p)
