import math as ma
import itertools

def verifica_float(var):
    try:
        float(eval(str(var)))
        return True
    except ValueError:
        return False
    except SyntaxError:
        return False
#print(eval(str("1a")))
class Punto:
    def __init__(self,x,y,z):
        def errore_trigger():
            return  not(
                    verifica_float(x)
                and verifica_float(y)
                and verifica_float(z)
                )   and (
                   ( "Classe Punto, input non valido: {{ {},{},{} }}\n".format(x,y,z) )
                + (( verifica_float(x) and (" ")) or ("(errX: " + '{} NaN)\n'.format(x)))
                + (( verifica_float(y) and (" ")) or ("(errY: " + '{} NaN)\n'.format(y)))
                + (( verifica_float(z) and (" ")) or ("(errZ: " + '{} NaN)\n'.format(z)))
            ) or False
        self.x=errore_trigger() or float(eval(str(x)))
        self.y=errore_trigger() or float(eval(str(y)))
        self.z=errore_trigger() or float(eval(str(z)))
        self.p='{},{},{}'.format(   self.x,
                                    self.y,
                                    self.z)
        self.pF='{},{},{}'.format(  errore_trigger() or round(self.x,3),
                                    errore_trigger() or round(self.y,3),
                                    errore_trigger() or round(self.z,3)
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

pippo=Punto("1/3",0.25,"1+6")
print(pippo.x)
print(pippo.y)
print(pippo.z)
print(pippo.p)
print(pippo.pF)