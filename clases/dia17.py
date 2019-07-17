
class Dino:
    ojos = 2

    def __init__(self, un_nombre, un_color, canti_patas=4, un_genero=None ):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("Naci")
    
    def saludar(self):
        print("Hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", self.genero)
    
    def cortar_patas(self, cantidad_de_patas_a_cortar=1):
        self.patas= self.patas - cantidad_de_patas_a_cortar

    def decir_genero(self):
        print("Hola soy", self.nombre, "y me identifico como", self.genero)

    

rex = Dino("Rex","Verde",5,"macho")
print(rex)

print(rex.nombre)
print(rex.color)
print(rex.patas)
print(rex.genero)

rex.saludar()
rex.cortar_patas()
rex.saludar()
rex.decir_genero()

##### HERENCIA ####

class TRex(Dino):
    def __init__(self, nombre, patas=4, color=None):
        self.nombre = nombre
        self.patas = patas
        self.color= color
        print("Hola soy un trex y me llamo", self.nombre)

robert = TRex("Roberto el TRex")
print(robert.ojos)

robert.saludar()
robert.decir_genero()

robert.esta_vivo()

robert.saludar()