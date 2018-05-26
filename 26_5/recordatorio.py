class Persona(object):
    __nombre = ""
    __apellido = ""
    __edad = 0

    def __init__(self,nombre,apellido,edad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__edad=edad
    
    def __str__(self):
        return '{"nombre":'+self.nombre+',"apellido":'+self.apellido+',"edad":'+ str(self.edad)+'}'



    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor
        
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,valor):
        self.__edad=valor
        
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,valor):
        self.__apellido=valor

personita=Persona("Marcos","Rey",44)
print personita


personita.apellido="Ruhl"
personita.nombre="Ivan"
personita.edad=18
print personita

