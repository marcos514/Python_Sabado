from abc import ABCMeta,abstractmethod

class AbstractPersistencia(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def guardar(*args,**kwargs):
        pass

    @abstractmethod
    def abrir(modo):
       pass

    @abstractmethod
    def buscar(*args,**kwargs):
        pass

    @abstractmethod
    def eliminar(*args,**kwargs):
        pass

    @abstractmethod
    def cerrar(*args,**kwargs):
        pass
