# -*- coding: utf-8 -*-

#Tipos de datos numéricos

#Imprime la suma de dos números

a = int (input ("ingrese un numero:"))
b = int (input ("ingrese otro numero:"))
suma = a + b
print ("El resultado de la suma es", suma)

#Crea dos variables como (alto y ancho) de un triángulo e imprime su área

alto = 16
base = 12
area = base * alto / 2
print("el area del triangulo es:", area)

#Imprime el número más grande entre 15 y 20, utiliza una función de Python

def numero_mayor():
    a = 15
    b = 20
    if a > b:
     print(a)
    else:
        print(b)
numero_mayor()


#Tipos de datos de cadena

#Asigna tu nombre a una variable:

nombre = "Sharon"
print("Mi nombre es", "", nombre)
    
#Imprime el número de caracteres de tu nombre. Ejemplo: (Mi nombre tiene ‘numero de caracteres’ número de caracteres)

print(len(nombre))

#Imprime tu nombre en mayúsculas

print(nombre.upper())


#Listas

#Escribe una lista de tu platos favoritos: Imprime el tercer plato de la lista

platos_favoritos = ["sancocho", "arepa", "pabellon criollo", "pasticho", "empanada de cazon"]
print(platos_favoritos[2])

#Imprime el número de ítems de la lista. Ejemplo: (Tengo ‘numero de items’ platos favoritos)

print("Tengo", len(platos_favoritos), "platos de comida venezolana favoritos")

#Imprime la lista en orden alfabético

platos_favoritos.sort()
print(platos_favoritos)


#Diccionarios

#Escribe un diccionario con tu nombre, edad y ciudad de nacimiento:

mis_datos = {
    'nombre': "Sharon",
    'edad': 28,
    'ciudad_nacimiento': "Los Teques"
}

#De entre tu lista, imprime tu nombre

print(mis_datos["nombre"])

#De entre tu lista, modifica el valor de ‘edad’

mis_datos["edad"] = 22
print(mis_datos["edad"])

#De entre tu lista, elimina la clave ‘ciudad’ y su valor

mis_datos.pop('ciudad_nacimiento')
print(mis_datos)


#Tuplas

#Escribe una lista de tus hobbies:

mis_hobbies = ("caminar por la playa", "leer", "ver series")

#Imprime tu hobby más reciente
print(mis_hobbies[0])

#Añade una nuevo hobby
"""No se puede añadir un nuevo elemento a la tupla por no ser mutables, una forma de añadir un nuevo elemento es creando una nueva variable con el nuevo elemento que queremos agregar
y una nueva variable donde vamos a concatenar mi tupla original + el nuevo elemento."""

nuevo_hobbie = "treking",
nueva_tupla = mis_hobbies + nuevo_hobbie
print(nueva_tupla)


#Condicionales
#Define en una variable la edad de un usuario.

#Escribe (El usuario es mayor de edad) si tiene igual o mas de 18 años - Escribe (El usuario es menor de edad) si tiene menos de 18 años

edad = int (input("Ingresa tu edad"))

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario no es mayor de edad")

#Escribe ‘el numero ‘’numero” existe’ si un número existe en una lista

lista_numeros = [1,2,3,4,5,6]
numero = int (input("Ingresa un número:"))

if numero in lista_numeros:
    print("El número", numero, "existe")
else:
    print("El número no existe")


#Bucles

#Define en una variable una lista con números no ordenados del 1 al 10. Utiliza un bucle para:
#Imprime los números de 1 al 10, en orden ascendente. Ejemplo: ()

numeros_desordenados = [7,5,1,3,9,4,8,2,6,10]
i = 1
while i in numeros_desordenados:
    print(i)
    i += 1    
    
#imprime los números del 1 al 10, en orden descendente.

i = 10
while i >= 1 in numeros_desordenados:
    print(i)
    i -= 1  
    
#Escribe letra a letra la cadena de texto: “Hello Clouders”

cadena = "Hello Clouders"
for letra in cadena:
    print(letra)

#Funciones

#Define e imprime el resultado de llamar a la función 'saludar()’, que salude a alguien.

def saludar():
    print("Hola María")
saludar()

def saludar():
    ingresar_nombre = input("Ingrese su nombre:")
    print("Hola", ingresar_nombre)
saludar()

#Imprime el valor devuelto por una función que sume dos números 'suma(a, b)’

def sumar(a,b):
    print(a + b)
sumar(7,5)

#Imprime el valor devuelto de una función que al pasarle como parámetro una lista de números devuelva la suma de todos los números pares.

def sumar_pares(lista_numeros):
    suma = 0
    for i in lista_numeros:
        if i % 2 == 0:
            suma += i
    return suma

numeros = [1,2,3,4,5]
resultado = sumar_pares(numeros)
print(resultado)
