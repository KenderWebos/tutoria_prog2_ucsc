print("iniciando...")

class Vehiculo:
    # Constructor de la clase, mediante esto se inicializan los atributos de la clase
    def __init__(self, nombre, ruedas, cap=1 , pas=0, color=""):
        self.ruedas = ruedas
        self.cap = cap
        self.pas = pas
        self.color = color
        print("vehiculo creado")

    def makeSound(self):
        print("DI DI!")    

class VehiculoTerrestre(Vehiculo):
    def __init__(self,nombre,ruedas,cap,pas,color,motor):
        super()._init_(nombre,ruedas,cap,pas,color)
        self.motor=motor
    def andando(self):
        print("El vehiculo esta andando")

vehiculoGenerico = Vehiculo("Generico", 4, 5, 0, "Rojo")

vehiculoGenerico.makeSound()

#Bus = VehiculoTerrestre("bus",4,31,0,"amarillo","v8 mamalon")

# class VehiculoAereo(Vehiculo):
#     def _init_(self,turbina):
#         self.turbina=turbina

# class VehiculoAcuatico(Vehiculo):
#     def _init_(self, nombre, ruedas, cap, pas, color,remos):
#         super()._init_(self,nombre,ruedas,cap,pas,color)
#         self.remos=remos
#     def remar(self):
#         print("Estoy remando")

# class VehiculoAnfibio(VehiculoTerrestre,VehiculoAcuatico):
#     def _init_(self,nombre,ruedas,cap,pas,color,motor,remos):
#         super()._init_(nombre,ruedas,cap,pas,color,motor)
#         self.remos=remos
#         self.motor=motor
    

# pato = VehiculoAnfibio("pato",4,1,0,"amarillo","v8 mamalon",True)
# pato.datos()
# pato.remar()
# pato.andando()

# input()