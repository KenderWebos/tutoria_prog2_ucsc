print("iniciando...")

class Vehiculo:
    # Constructor de la clase, mediante esto se inicializan los atributos de la clase
    def __init__(self, nombre, ruedas, cap=1 , pas=0, color=""):
        self.ruedas = ruedas
        self.cap = cap
        self.pas = pas
        self.color = color

    #Definimos un metodo para validar que no se exceda la capacidad del vehiculo
    def validar_pasajeros(self, n):
        if n > self.cap:
            return False
        elif self.pas < 0:
            return False
        else:
            return True
    #Definimos un metodo para subir pasajeros
    def SubirPasajeros(self, n):
        self.pas+=n
        
        check = self.validar_pasajeros
        if check == False:
            print("Se excede la capacidad del vehiculo")
            self.pas-=n
        else:
            print("Se subieron los pasajeros")
    #Definimos un metodo para imprimir los datos del vehiculo
    def BajarPasajeros(self, n):
        self.pas-=n
        check = self.validar_pasajeros
        if check == False:
            print("No se pueden bajar mas pasajeros")
            self.pas=0
        else:
            print("Se bajaron los pasajeros")
    def datos(self):
        print("El vehiculo tiene",self.ruedas,"ruedas")
        print("La capacidad del vehiculo es de",self.cap,"pasajeros")
        print("El vehiculo tiene",self.pas,"pasajeros")
        print("El color del vehiculo es",self.color)

class VehiculoTerrestre(Vehiculo):
    def __init__(self,nombre,ruedas,cap,pas,color,motor):
        super()._init_(nombre,ruedas,cap,pas,color)
        self.motor=motor
    def andando(self):
        print("El vehiculo esta andando")

#Bus = VehiculoTerrestre("bus",4,31,0,"amarillo","v8 mamalon")

# class VehiculoAereo(Vehiculo):
#     def __init__(self,turbina):
#         self.turbina=turbina

class VehiculoAcuatico(Vehiculo):
    def __init__(self, nombre, ruedas, cap, pas, color,remos):
        super().__init__(nombre,ruedas,cap,pas,color)
        self.remos=remos
    def remar(self):
        print("Estoy remando")

pato = VehiculoAcuatico("pato",4,1,0,"amarillo",True)

pato.datos()

# class VehiculoAnfibio(VehiculoTerrestre,VehiculoAcuatico):
#     def __init__(self,nombre,ruedas,cap,pas,color,motor,remos):
#         super().__init__(nombre,ruedas,cap,pas,color,motor)
#         self.remos=remos
#         self.motor=motor
    

# pato = VehiculoAnfibio("pato",4,1,0,"amarillo","v8 mamalon",True)
# pato.datos()
# pato.remar()
# pato.andando()

# input()