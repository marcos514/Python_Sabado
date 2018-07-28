class Contacto(object):
    __nombre=""
    __telefono=""
    __email=""

    def __init__(self,nombre,tel,mail):
        self.__email=mail
        self.__nombre=nombre
        self.__telefono=tel

