from Persistencia import Persistencia

class Agenda(object):
    __dato={}
    __persistencia=Persistencia("marcos.json")
    def abrir(self):
        self.__dato=self.__persistencia.preparar()
        if(self.__dato=="Error al leer el archivo"):
            return False
        return True

    def guardar(self,nombre,tel,email):
        self.__dato[nombre]={email:tel}
        print self.__dato
        self.__persistencia.grabar(self.__dato)
        return self.__dato

    def buscar(self,nombre):
        return self.__dato.get(nombre,"error nombre no ingresado")

    def eliminar(self,nombre):
        try:
            self.__dato.pop(nombre)
        except ValueError:
            return False
        self.__persistencia.grabar(self.__dato)
        return True




agenda=Agenda()
print agenda.abrir()
print agenda.guardar("Marcos",1234,"marcos@gmail.com")
print agenda.buscar("Marcos")
print agenda.eliminar("Marcos")



