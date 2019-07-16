 ####string o cadena de texto
 "esto es string"
### tipo de dato integer o entero
105
###Listas
[] ###listas vacias
["felix", 20, "estudiante"] #lista de elementos
#### VARIABLES no puede tener comas ni puede empezar con numeros
nombre = "felix"
edad = 20
variable_lista = ["Hola", nombre, 20]
### Acceder a un elemento de lista
print(variable_lista[0], edad, variable_lista[2])
#### Acciones operaciones sobre listas
variable_lista.append ("rugby") ##agregar elemento a lista
variable_lista.pop() ## eliminar ultimo elemento
variable_lista[2] = 50  ### modificar un elemento en la lista
#### BUCLES, LOOP, CICLOS
for loquesea in variable_lista :
    print(loquesea)

##### imprimir los numeros del 1 al 10
for cualquiercosa in range (11):
    print(cualquiercosa)

###### solucion paso por paso
otra_lista = [5,"hola que tal", "chau",4] ### lista general
otra_lista.append("aaaaa")
#### solucion para hallar el ultimo elemento de una lista
dim_lista = len(otra_lista) ### agrege la dimension de la lista a una variable
print("la dimension de la lista es", dim_lista)
indice_del_ultimo = dim_lista - 1  #### el ultimo elemento de una lista en variable
print("el indice del ultimo elemento es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])
################
for numero in range(1,11):
    print(numero)
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", numero)
####### imprimir el numero de resultado de la suma de los numeros del 1 al 10
sumatoria = 0   ### variable iniciada en cero
for valor in range (1,11):   #se crea elementos del 1 al 10
    sumatoria= sumatoria + valor    ### crear operacion para ir sumando cada elemento
print(sumatoria)

####### FUNCIONES ######### def
def suma(num1,num2):
    resultado = num1 + num2
    return resultado
### equivalente a la de arriba
def suma2(num1,num2):
    return num1 + num2
print(suma(5,10))
resul = suma(5,8)
print(resul)
#### ejercicio crear una funcion resta, que reciba como parametro dos numeros
### y retorne la resta de esos numeros luego llamar a la funcion e imprimir el res
def resta(num1,num2):
    resultado= num1 - num2
    return resultado
print(resta(8,4))
resul= resta(8,4)
print(resul)

#####ejerc 2 crear una funcion saludo2 que reciba como parametro nombre y edad e 
### imprimir Hola soy... y tengo.... años llamar varias veces a la funcioncon 
### distintos valores 
def saludo (nombre, edad):
    print("hola soy",nombre, "y tengo", edad, "años")

saludo("felix",2{0)
saludo("marce",33)

def datos (nombre,edad,CI,profesion):
    print("mi nombre es",nombre,"tengo", edad, "años", "mi ci es", CI, "y soy",profesion)
datos("Felix",20,6220661,"estudiante")
datos("carmen",32,324676,"arquitecta")
datos("Raul",56,769893,"doctor")
##### EJERCICIO, crear una funcion suma_lista que reciba como argumento una lista
#de numeros y retorne la suma de sus elementos
#pista usar acumulador
listita = [1,2,3,4,5]   #1+2+3+4+5=15
listota = [100,5,5]    ### el valor de retorno 110
def suma_lista (una_listita):
    suma = 0
    for x in una_listita:
        suma = suma + x
    return suma
suma_lista(listita)
#### Ej2 lista al cuadrado, crear un funcion que reciba una lista de numero como 
####parametro y retrne una lista con los numeros al cuadrado 
### lista_cuadrado(listita)     [1,4,9,16,24]
listajeyma = [1,4,9,16,24]

def lista_cuadrado(listajeyma):
    a=[]  ### se crea lista vacia
    for jeyma in listajeyma:
        a.append(jeyma * jeyma)   #####en la lista vacia se agrega jeyma por jeyma
    return a  #### pido retorno
lista_cuadrado(listajeyma)

#### Eliminar todos los elementos de una lista utilizando for
grupo5 = ["N","F1", "F2", "A"]
for j in range(len(grupo5)):
    grupo5.pop()
print()

### Crear una funcion suma_cuadrado que reciba una lista de numeros y retorne el 
###valor de la suma de cada numero al cuadrado [1,2,3]  1+4+9....14
lista = [1,2,3,4]
def suma_cuadrado(lista):
    
