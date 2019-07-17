
###Hacer una clase que se llame vehiculo y que tenga tres atributos y uno de ellos sea cantidad_ruedas y un metodo
## que sea definir_tipo_vehiculo que me diga si es bicicleta, triciclo, auto de acuerdo a la cantidade de ruedas

class Persona :
    cantidad_ruedas = 4
    tamaño_ruedas = "grande"
    color_ruedas = "negras"
    
    def __init__ (self, un_tipo) :
        self.mi_vehiculo = un_tipo  
        print("vehiculo creado", self.mi_vehiculo)

    def definir_tipo_vehiculo (self):
        cantidad_ruedas = 40
        if cantidad_ruedas == 2:
            print("bicicleta")
        if cantidad_ruedas == 3:
            print("triciclo")
        if cantidad_ruedas == 4:
            print ("auto")
        




vehiculo = Persona("automovil")
print(vehiculo.cantidad_ruedas)

vehiculo.definir_tipo_vehiculo()