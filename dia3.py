##### def
ing_pan = ["harina","levadura","sal","azucar","agua"]  ###crear list
def imprimir_lista(ingredientes,nombre_producto):   #### creamos una funcion 
    print("lista de compras de", nombre_producto)   ####
    print("............")
    for producto in ingredientes:
        print(producto)

imprimir_lista(ing_pan,"pan")   #####FUNCION CREADA
###########
ing_salsa = ["tomate","azucar","sal","cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza") ##utilizamos la funcion a otra lista


###################Ejercicio crear una funcin suma_cuadrado que reciba
#### una lista de numeros y retorne el valor de la suma de cada numero al
### cuadrado [1,2,3,4]     [1+2+9+16] 30
list_numeros = [1,2,3,4]
def suma_cuadrado(lista_n):
    suma = 0
    for p in lista_n:
        suma = suma + (p*p)
    return suma

print (suma_cuadrado(list_numeros))


######## CONDICIONALES #############
### == igual
# > mazor que
#### < menor que 
## > mazor o igual 
### < menor o igual
a = 3
##pregunta 1
if a > 3 :
    print ("si, a es mayor a 3")
    print ("chau1")
else :
    print ("No, a es mayor a 3")
## pregunta 2
if a == 3:
    print("a es igual a 3")

nota = 60
## pregunta 3
if nota >= 60 :
    print ("pasaste")
else :
    print ("hule ya")

### EJ Crear una funcion que reciba como parametro una nota de 1 al 100 e imprimir si pasaste o 
### te aplazaste (se prueba con 61 )

calificacion = 61
def nota (numeros):
    if numeros >= 61:
         print("aprobado")
    else:
        print ("reprobado")

nota(calificacion)

###### otro ejemplo
a = 6
if a > 5 and a < 10 :
    print("a es mayor a  y menor que 10")
else :
    print ("a no esta en el rango, alguna de las 2 condiciones no se cumplio") 
a=6
if a > 5 or a < 10 :
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")

############
edad = 7
if edad > 18 :      ####Si coincide con una de las opciones, automaticamente imprime es y saltea los restantes
    print ("deberia de estar en la universidad")
elif edad > 13 :
    print("deberia de estar en la secundaria")
elif edad > 6:
    print("deberia de estar en su casa primaria")
else :
    print("deberia de estar en su casa bbdlx")

###### Ej, crear una funcion puntaje que reciba como parametro una nota del 1 al 100 e imprimir
###  que nota sacaste 
### nota < 60 ------> 1
### nota entre 60 y 70 -----> 2
### nota entre 71 y 75 ------> 3
### nota entre 76 y 85 ------> 4
### nota mayor que 85 -------> 5

nota = 90
def exa (numeross):
    if numeross > 85 :
        print(5)
    elif numeross > 75:
        print(4)
    elif numeross > 70:
        print(3)
    elif numeross > 59 :
        print(2)
    else:
        print(1)
exa(nota)  ### funcion creada para una escala

######## Ejercicio. Pedir al usuario que ingrese tres numeros y multiplicarlos entre si, imprimir el 
#### el resultado
nombre = input ("ingrese el primer numero")   ###input para imprimir en pantalla 
nonmbre_2 = input ("ingrese el segurndo numero")
nombre_3 = input("ingrese el tercer numero")
print(int(nombre) * int(nonmbre_2)* int(nombre_3))

#####Ej2. Pedir al usuario un numero del 1 al 100 y llamar a la funcion que retornaba la nota que creamos
### hace un rato utilizando el valir ingreado por el usuario
Datos =int(input("Ingrese un numero del 1 al 100"))   ###int para pasar de stream a numeros
exa(Datos)

##### Bucle while == Mientras ####

x = 74
while x != 5 :
    print ("esto es un bucle while, se va a ejecutar mientras x sea distinta de 5") 
    x = int(input("ingresa un numero:"))
    print("el valor de x ahora es ", x)
print("Terminoo")

### contador inverso
contador = 10
while contador > 0 :
    print("sigo en el bucle while")
    contador = contador - 1
    print ("te quedan",contador,"oportunidades")
print("termino")

## contador
contador = 0
while contador < 10 :
    print ("sigo en el bucle while")
    contador = contador + 1
    print("se repite",contador,"veces")

#### Ejer. usando while pedir al usuario 5 ingredientes para hacer una pizza y agregar a una lista 
### al final imprimir una lista 

contador = 0
ing_lista = []
while contador < 5:
    print(input"Hola"))
    ingre = input("ingrese un ingeniero: ")
    ing_lista.append(ingre)
    contador = contador + 1
print ("los ingredientes de la pizza son : ", ing_lista)
###
numero_secreto = 7
adivino = False
while adivino == False :
    apuesta = input("Adivina el numero secreto del 1 al 10")

    if int(apuesta) == numero_secreto :
        print("Ganaste")
        adivino = True
    else :
        print("segui participando nde arruinado")
    
#### Ej crear un juego de adivinar el numero como elde arriba y darle pistas al usuario
### si el numero que ingreso es mayor o menor al numero a adivinar.. pista usar elif

numero_secreto = 3
adivino = False
while adivino == False :
    apuesta = input("Adivina el numero secreto del 1 al 10")
    if int(apuesta) == numero_secreto :
        print("Ganaste")
        adivino = True
    if int(apuesta) < numero_secreto:
        print("es mayor")
    if int(apuesta) > numero_secreto:
        print ("es menor")

#### Ej 2 buscar como generar un numero aleatorio para numero_secreto 
 
 from random import randint ##### funcion predeterminada
 numero_secreto = randint(0,10)