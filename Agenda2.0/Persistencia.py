import json
from AbstractPersistencia import  AbstractPersistencia


class PersistenciaEnArchivo(AbstractPersistencia):
    __ubicacion = ""
    __archivo = None
    __datos=None

    def __init__(self,ubicacion):
        self.__ubicacion=ubicacion

    def abrir(self):
        try:
            self.__archivo=  open(self.__ubicacion, "a+")
        except :
            raise Exception("No se pudo abrir la persistencia")
#
 #       retorno = ""
  #      retorno = self.__archivo.read()
   #     if (retorno == ""):
   #         return False

    #    self.__archivo.close()
     #   try:
      #      retorno = json.loads(retorno)
       #     return retorno
       #     except Exception:
        #    return False

    def guardar(self, dato):
        try:
            self.__archivo = open(self.__ubicacion, "w+")
            self.__archivo.writelines(json.dumps(dato))
            return True
        except ValueError:
            return False
        finally:
            self.__archivo.close()

    def __cargar_datos(self):
        retorno = ""
        try:
            self.__archivo = self.abrir("r")

            retorno = self.__archivo.read()
            if (retorno == ""):
                return "{}"
            retorno = json.loads(retorno)
            return retorno
        except :
            raise Exception("Error al buscar contacto")
        finally:
            self.__archivo.close()
        return retorno




    def buscar(self,nombre):
        datos=self.__abrir_para_busqueda()
        return datos.get(nombre,None)



    def eliminar(nombre):
        pass

    def cerrar(aaa):
        pass

