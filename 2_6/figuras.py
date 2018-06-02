from abc import ABCMeta,abstractmethod,abstractproperty

class abstractFigura(object):
    __metaclass__=ABCMeta
    _lado=0
    _cant_lados=0

    def __init__(self, lado,cant):
        self._lado=lado
        self._cant_lados=cant
    @property
    def perimetro(self):
        return self._lado*self._cant_lados
    @abstractproperty
    def area(self):
        pass
    @abstractmethod
    def dibujar(self):
        pass


class Cuadrado(abstractFigura):
    def __init__(self,lado):
        super(Cuadrado,self).__init__(lado,4)
    
    @property
    def area(self):
        return self._lado**2

    def dibujar(self):
        dibujo=""
        i=0
        while i<self._lado:
            j=0
            while j<self._lado:
                dibujo+="*"
                j+=1
            dibujo+="\n"
            i+=1

            
        return dibujo

cuadradito=Cuadrado(4)
print cuadradito.dibujar()