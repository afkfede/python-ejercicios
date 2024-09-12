#Ejercicio 1
def mayorUnico(a, b, c):

    a_mayor = (a > b) * (a > c)
    b_mayor = (b > a) * (b > c)
    c_mayor = (c > a) * (c > b)

    mayor = a * a_mayor + b * b_mayor + c * c_mayor
    return mayor if mayor != 0 else -1


a = int(input("Ingrese el primer número positivo: "))
b = int(input("Ingrese el segundo número positivo: "))
c = int(input("Ingrese el tercer número positivo: "))

resultado = mayorUnico(a, b, c)
    
if resultado != -1:
    print(f"El mayor único es: {resultado}")
else:
    print("No existe un mayor único.")

#Ejercicio 2
from datetime import datetime
def fecha_valida(dia, mes, ano):
    try:
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False
    
print("Ingrese una fecha (primero DIA, segundo MES, tercero AÑO): ")
dia = int(input(""))
mes = int(input(""))
anio = int(input(""))

if fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
else:
    print("La fecha no es válida.")

#Ejercicio 4
def patron_ascendente(n):
    for i in range(1, n + 1):
        print('*' * i)

def patron_especifico(cantidad):
    print(" ")
    for _ in range(cantidad):
        print('*' * cantidad)

num = int(input("Ingresar un numero: "))
patron_ascendente(num)

patron_especifico(num)

#Ejercicio 5
cuadrado = lambda x: x ** 2

numero = int(input("Ingrese un numero: "))
print(f"El cuadrado de {numero} es:", cuadrado(numero))

#Ejercicio 6
numero_par = lambda x: x % 2 == 0

numero_impar = lambda x: x % 2 != 0

numero = int(input("Ingresar un numero: "))
print(f"El número {numero} es par:", numero_par(numero))
print(f"El número {numero} es impar:", numero_impar(numero))

#Ejercicio 7
def calcularCuadrados(n):
    return [i**2 for i in range(1, n+1)]

def calcularUltimos10(cuadrados):
    return cuadrados[-10:]

n = int(input("Ingrese un numero entero positivo: "))

cuadradros = calcularCuadrados(n)
print(f"Lista completa de cuadrados: {cuadradros}")
ultimos10 = calcularUltimos10(cuadradros)
print(f"Últimos 10 valores de la lista: {ultimos10}")

#Ejercicio 8
def eliminar_elementos(lista_original, lista_a_eliminar):
    lista_resultante = []
    for palabra in lista_original:
        if palabra not in lista_a_eliminar:
            lista_resultante.append(palabra)
    return lista_resultante

lista_original = ['river', 'boca', 'racing', 'independiente', 'atletico']
lista_a_eliminar = ['boca', 'racing']

print(f"Lista Original: {lista_original}")
print(f"Lista a Eliminar: {lista_a_eliminar}")
lista_final = eliminar_elementos(lista_original, lista_a_eliminar)
print(f"Lista Resultante: {lista_final}")

#Ejercicio 9
def ordenada_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    
    return True

num = input("Ingresa los elementos de la lista separados por espacios: ")
lista = list(map(int, num.split()))

if ordenada_ascendente(lista):
    print("La lista está ordenada en forma ascendente.")
else:
    print("La lista NO está ordenada en forma ascendente.")

#Ejercicio 10
def es_capicua(palabra):
    izquierda = 0
    derecha = len(palabra) - 1
    
    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return False
        izquierda += 1
        derecha -= 1
        
    return True

palabra = "radar"
print(es_capicua(palabra))

palabra = "hola"
print(es_capicua(palabra))

#Ejercicio 11
def centrarCadena(cadena, ancho_pantalla):
    return cadena.center(ancho_pantalla)

def cadenaCentrada(cadena, ancho_pantalla):
    cadena_centrada = centrarCadena(cadena, ancho_pantalla)
    print(cadena_centrada)
    
cadena = input("Introduce una cadena de caracteres: ")
ancho_pantalla = 80

cadenaCentrada(cadena, ancho_pantalla)

#Ejercicio 12
def fecha_extendida(dia, mes, anio):
    
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    anio = 2000 + anio
    
    nombre_mes = meses[mes - 1]
    
    print(f"{dia} de {nombre_mes} de {anio}")

print("Ingrese una fecha (primero DIA, segundo MES, tercero AÑO (ultimos dos digitos)): ")
dia = int(input(""))
mes = int(input(""))
anio = int(input(""))
fecha_extendida(dia, mes, anio)

#Ejercicio 13
def obtenerPalabras(frase):
    palabras = frase.split()
    conjunto_palabras = set(palabras)
    return list(conjunto_palabras)

def ordenarPorLongitud(lista_palabras):
    lista_palabras.sort(key=len)
    return lista_palabras

def palabrasOrdenadas(lista_palabras):
    print("Palabras ordenadas por su longitud:")
    for palabra in lista_palabras:
        print(palabra)

frase = input("Introduce una frase: ")
lista_palabras = obtenerPalabras(frase)
lista_palabras = ordenarPorLongitud(lista_palabras)
palabrasOrdenadas(lista_palabras)

#Ejercicio 14
def eliminar_claves(diccionario, lista_claves):

    claves_existentes = [clave for clave in lista_claves if clave in diccionario]

    for clave in claves_existentes:
        del diccionario[clave]

    return diccionario, True

diccionario = {'dni': 40352832, 'nombre': "Juan", 'edad': 20, 'telefono': 15534234}
lista_claves = ['nombre', 'telefono']
print(f"Diccionario orignial: {diccionario}")
diccionario_modificado, existe = eliminar_claves(diccionario, lista_claves)

print(f"Diccionario modificado: {diccionario_modificado}")
print(f"Operación exitosa: {existe}")

#Ejercicio 15
def eliminar_subcadena(cadena, posicion, cantidad):
    
    cantidad = min(cantidad, len(cadena) - posicion)
    return cadena[:posicion] + cadena[posicion + cantidad:]

cadena_inicial = "Tecnicatura Superior en Desarrollo de Software"
posicion = 11
cantidad = 12
    
print(f"Cadena original: {cadena_inicial}")
print(f"Posicion desde donde eliminar: {posicion}")
print(f"Cantidad de caracteres a eliminar: {cantidad}")
    
cadena_resultante = eliminar_subcadena(cadena_inicial, posicion, cantidad)
print(f"Cadena resultante: {cadena_resultante}")