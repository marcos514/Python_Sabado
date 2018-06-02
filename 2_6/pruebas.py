from abs import ABCMeta,abstractmethod,abstractproperty

class Personaje(object):
    _vida=0
    _posicion=0
    _velocidad=0
    def __init__(self,vida,posicion,velocidad):
        self._vida=vida
        self._posicion=posicion
        self._velocidad=velocidad
    
    def dibujar(self):
        raise NotImplementedError("Error bobo")

    def recibir_ataque(self, danio):
        self._vida-=danio
        if(self._vida<=0):
            raise Exception("murio wey")
    
    def mover(self,direccion):
        if(direccion=="arriba"):
            self._posicion[1]+=self._velocidad
        elif direccion=="abajo":
            self._posicion[1]-=self._velocidad
        elif direccion=="derecha":
            self._posicion[0]+=self._velocidad
        elif direccion=="izquierda":
            self._posicion[0]-=self._velocidad
 
class Soldado(Personaje):
    _ataque=0
    def __init__(self,vida,posicion,velocidad,ataque):
        super(Soldado,self).__init__(vida,posicion,velocidad)
        self._ataque=ataque
    
    def atacar(self,personaje):
        personaje.recibir_ataque(self._ataque)

class Campesino(Personaje):
    _cosecha=0
    def __init__(self,vida,posicion,velocidad,cosecha):
        super(Campesino,self).__init__(vida,posicion,velocidad)
        self._cosecha=cosecha

    def cosechar(self):
        return self._cosecha
   

soldadito=Soldado(100,[1,1],10,100)
campesinito=Campesino(200,[2,3],5,15)
print soldadito.__dict__
print campesinito.__dict__
soldadito.atacar(campesinito)
soldadito.mover("arriba")
campesinito.mover("derecha")
print soldadito.__dict__
print campesinito.__dict__