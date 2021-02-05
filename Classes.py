import math as ma
import itertools


def parse_float(val):
    return float(eval(str(val)))

def controllo_float(val):
    try:
        parse_float(val)
        return parse_float(val)
    except ValueError:
        return "errore"
    except SyntaxError:
        return "sintassi non valida"
    except NameError:
        return "sintassi non valida (nome variabile?)"
    except OverflowError:
        return "risultato oltre i limiti calcolabili"

def verifica_float(val):
    return controllo_float(val)

print (verifica_float("5**5+t"))

class Punto:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.p='{},{},{}'.format(   self.x,
                                    self.y,
                                    self.z)
        self.pF='{},{},{}'.format(  round(self.x,3),
                                    round(self.y,3),
                                    round(self.z,3)
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

pippo=Punto(1/3,0.25,1+6)
print(pippo.x)
print(pippo.y)
print(pippo.z)
print(pippo.p)
print(pippo.pF)