
class Persona :    #### Definimos la clase, una receta para crear un objeto, es una plantilla
    edad = 5       ### atributo o propiedad del objetos que creamos

    def __init__(self, un_nombre):    ###metodo constructor : funcion dentro de la clase que opera dentro del objeto
        self.mi_nombre = un_nombre     ### usamos self para referirnos al objeto mismo
        print("Hola naci, me llamo", self.mi_nombre)    

    def cumple(self):                 ##### cumple es un metodo de la clase persona
        self.edad = self.edad + 1      ### que aumenta la propiedad en uno
    
    def restaedad(self):
        self.edad = self.edad - 1
    
    def origen(self, un_pais):
        self.nacionalidad = un_pais
    
    def presentacion(self):
        print("Hola soy",self.mi_nombre, "y mi nacionalidad es", self.nacionalidad)
    
    

pepe = Persona("Pepito")   #### pepe es un objetp de la clase o tipo persona
pepa = Persona("Pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)

pepe.restaedad()
print(pepe.edad)

###Ejercicio Agregar un metodo a la case que asigne una nacionalidad y otro metodo que imprima hola soy... y mi
### nacionalidad es... 

pepe.origen("Argentino")

pepe.presentacion()



