import json
class Persistencia(object):
    __ubicacion=""
    __archivo=""
    def __init__(self,ubicacion):
        self.__ubicacion=ubicacion

    def preparar(self):

        try:
            self.__archivo = open(self.__ubicacion, "r")
        except ValueError:
            return "Error al leer el archivo"

        retorno=""
        retorno=self.__archivo.read()
        if(retorno==""):
            return "Error al leer el archivo"

        self.__archivo.close()
        retorno=json.loads(retorno)

        return retorno



    def grabar(self,dato):
        try:
            self.__archivo = open(self.__ubicacion, "w")
            self.__archivo.writelines(json.dumps(dato))
            return True
        except ValueError:
            return False
        finally:
            self.__archivo.close()
