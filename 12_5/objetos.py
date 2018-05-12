class Persona(object):
    def __init__(self,edad,nombre,apellido,dni):
        self.__edad=int(edad)
        self.__apellido=apellido
        self.__nombre=nombre
        self.__dni=dni

    def mostrarNombre(self):
        print "Nombre:",self.__nombre
    
    def Mayor(self):
        if(self.__edad>=18):
            return "Mayor"
        else:
            return "Menor"
    def cumplir_anios(self):
        self.__edad+=1

    def toString(self):
        return "Nombre: "+self.__nombre+" - "+self.__apellido+" Edad: "+str(self.__edad)+" Dni: "+str(self.__dni)  
    
    @property
    def Nombre(self):
        return self.__nombre



class Alumno(Persona):
    def __init__(self,edad,nombre,apellido,dni,legajo):
        Persona.__init__(self,edad,nombre,apellido,dni)
        self.__legajo=int(legajo)

    

    def toString(self):
        mostrar=Persona.toString(self)+" Legajo: "+str(self.__legajo)
        return "".join(mostrar)

class Profesor(Persona):
    def __init__(self,edad,nombre,apellido,dni,legajo):
        Persona.__init__(self,edad,nombre,apellido,dni)
        self.__legajo=int(legajo)

    def toString(self):
        mostrar=Persona.toString(self)+" Legajo: "+str(self.__legajo)
        return "".join(mostrar)
    
class Clase:
    def __init__(self,alumno,nombre,cantidadMaxima,precio,profesor):
        self.__nombre=nombre
        self.__cantidadMaxima=cantidadMaxima
        self.__precio=precio
        self.__alumnos=[]
        self.__profesor=profesor
        for alumnoAgregar in alumno:
            if(len(self.__alumnos)+1<=self.__cantidadMaxima):
                self.__alumnos.append(alumnoAgregar)
            else:
                break
     

    def toString(self):
        texto="Nombre: "+self.__nombre+"\nProfesor a cargo: "+self.__profesor.Nombre+"\nPrecio: "+str(self.__precio)+"\nCantidad de Alumnos: "+str(len(self.__alumnos))

        for alumno in self.__alumnos:
            texto=texto+"\n"+alumno.toString()
        texto+="\n\nRecaudacion: "+str(self.Recaudar())
        return texto
    def Recaudar(self):
        return len(self.__alumnos)*self.__precio




a=Alumno(18,"Marcos","Rey",41435394,1)
b=Profesor(22,"Diego","M",5555,15)

clase=Clase([a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],"Python",50,1400,b)
print clase.toString()

