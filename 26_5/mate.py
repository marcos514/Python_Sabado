import json
class Mate(object):
    __cebadas_Restantes=0
    __lleno=False
    def __init__(self,n):
        self.__cebadas_Restantes=n

    def __str__(self):
        valor=self.__dict__
        valor=str(valor)
        valor=valor.replace("_Mate__","")

        return  json.dumps(valor) 

    
    def cebar(self):
        if self.__lleno:
            raise Exception("Cuidado!! Te quemaste")
        
        self.__lleno=True
        
    def beber(self):
        if not self.__lleno:
            raise Exception("Mate esta vacio!")

        self.__lleno=False

        if self.__cebadas_Restantes > 0:
            
            self.__cebadas_Restantes-=1
        else:
            print "Advertencia! Mate lavado"
            


matecito=Mate(50)

archivo=open("archivo.txt","w")
i=50
archivo.write("[\n")
while(i>0):
    matecito.cebar()
    matecito.beber()
    linea=str(matecito)
    archivo.writelines(linea+"\n")
    if(i!=1):
        archivo.writelines(",")
    i-=1
archivo.write("]")
archivo.close()


archivo=open("archivo.txt","r")
for linea in archivo.readlines():
    print linea
archivo.close()










        