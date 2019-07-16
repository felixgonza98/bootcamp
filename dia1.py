print(2*2)
print(5-3)
print(35*2) #multiplicacion de numeros
print("hola mundo") #usar comillas para palabras
print("hola" * 10) #multiplicacion de las palabras
print("hola " * 29) #utilizar espacios para separar las palabras
#########estructura de datos VARIABLES
a = 10 #Damos un valor a la letra a
b = 2 #damos un valor a la letra b
print(a*b) #multiplicamos las variables
a = 10-b #damos nuevo valor a la a
print(a*b) #imprimimos una multiplicacion con las nuevas variables
print (a,b) #separamos elementos con la coma.
print ("variables de a y b son ",a,b) #combinacion de textos con las variables.
print ("ocho",a,"dos",b) #prueba de combinacion de texto y variables.
#### EJERCICIO NOMBRE Y EDAD CON VARIABLES Y TEXTOS
nombre = "Felix" #textos si o si con comillas
edad = 20 #los numeros o variables sin comas
print("Hola me llamo", nombre, "y tengo", edad, "años")
##### EJERCICIO 2 Variable con hobby
hobby = "leer y escuchar musica "
print("hola me llamo", nombre, "y mis hobbies son",hobby)
#### LISTAS 
lista_vacia = []
listax = [1,2,6,8]
print(lista_vacia)
print(listax)
datos = ["marce"]
print(datos)
alumnos = ["jose", "ramon", nombre,"maria"]
print(alumnos)
#####Ejercicios de lista
datos = ["FELIX", 20, "escuchar musica y leer"]
print("Hola me llamo", datos[0], "y tengo", datos[1], "años", "y me gusta", datos[2])
datos[2]= "salir"
print("a el le gusta", datos[2])
datos.append("estudiante") #agregar informacion a la lista datos
print(datos[3])
####EJERCICIO
datos = ["FELIX",20]
datos.append("estudiante") #agregar informaciones a dato
print(datos) #cambie mi lista 
datos.append("escuchar musica")  
print("soy", datos[2], "y me gusta", datos[3])  
datos.pop()
print(datos)
### funcion len() = lenght
print(datos)
print(len(datos))
### Ejercicios de len 
print(datos)
print(len(datos))
dimension_de_datos = len(datos)
print("la lista datos tiene",dimension_de_datos, "elementos" )
###### Ej imprimir el ultimo elemento de una lista sin saber cuantos elementos
#tiene
datos = [1,2,3,4,5,6,7,8,9,3,4,5,2,6,7,9,3,2,3,4,6,5,8,9,5,6,7,3]
print(datos)
print(len(datos)) #cantidad de elementos
dimension_de_datos = len(datos) ### cantidad de elementos
print(datos[1])   ### prueba de como listar
print(datos[dimension_de_datos-1]) ### cantidad de elementos - los numeros
###### Bucles, Loops, ciclos, iteraciones
lista_temas = ["variables", "listas", "tipos de datos"]
for concepto in lista_temas:
    print("hoy aprendi", concepto)
    print("que gusto")
print ("esto es lo que aprendi hoy")
##### recorrer una lista con fro e imprimir en cada ciclo el valor del elemento 
###con 3 signos de admiracion al final fuera del bucle fin ej variables
datos = ["FELIX", "20", "estudiante",]
for concepto in datos:
    print("datos personales", concepto )
print("FIN!!!")

##### for in range para repetir
for x in range(10):
    print("HOLA", x)
####EJERCICIO Imprimir los numeros del 1 al 100 usando for y range
for x in range(101):
    print(x)
##### EJERCICIO imprimir el resultado de la suma de los numeros del 1 al 10
for x in range(1+2+3+4+5+6+7+8+9+10):
    print(x+1)