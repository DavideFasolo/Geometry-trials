import math as ma
import itertools


def parse_float(val):
    return float(eval(str(val)))

def controllo_float(val):
    try:
        parse_float(val)
        return parse_float(val)
    except ValueError:
        print("errore di input coordinata punto")
        return "errore"
    except SyntaxError:
        print("errore di sintassi coordinata punto")
        return "sintassi non valida"
    except NameError:
        print("errore di sintassi coordinata punto")
        return "sintassi non valida (nome variabile?)"
    except OverflowError:
        print("errore di overflow coordinata punto")
        return "risultato oltre i limiti calcolabili"

def isfloat(val):
    return str(controllo_float(val)).isnumeric()

def verifica_float(val):
    return controllo_float(val)


class Punto:
    def __init__(self,x,y,z):
        self.x=isfloat(x) and parse_float(x)
        self.y=isfloat(y) and parse_float(y)
        self.z=isfloat(z) and parse_float(z)
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
