#Ejercicio 1
print("Bienvenido a Python")

#Ejercicio 2
num1 = 22
num2 = 7
resultado = num1 - num2
print(f"La diferencia entre {num1} y {num2} es: {resultado}")

#Ejercicio 3
edad = int(input("Ingrese su edad: "))
print(f"Tienes {edad} años")

#Ejercicio 4
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
producto = num1*num2
print(f"El producto de {num1} y {num2} es: {producto}")


#Ejercicio 5
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
    
print(f"El numero menor es: {menor}")

#Ejercicio 6
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4
    
print(f"De los cuatro numeros el menor es: {menor}")

#Ejercicio 7
num = int(input("Ingrese un numero: "))
if num % 2 != 0:
    print(f"El numero {num} es IMPAR")
else:
    print(f"El numero {num} NO es IMPAR")
    
#Ejercicio 8
num = int(input("Ingrese un numero: "))
if num % 4 == 0:
    print("Es divisible por 4")
elif num % 6 == 0:
    print("Es divisible por 6")
elif num % 8 == 0:
    print("Es divisible por 8")
elif num % 10 == 0:
    print("Es divisible por 10")
else:
    print("No es divisible por 4, 6, 8 o 10")
    
#Ejercicio 9
num = int(input("Ingrese un numero: "))
if num % 4 == 0:
    print("Es divisible por 4")
if num % 6 == 0:
    print("Es divisible por 6")
if num % 8 == 0:
    print("Es divisible por 8")
if num % 10 == 0:
    print("Es divisible por 10")

#Ejercicio 10
numero = int(input("Introduce un número: "))
print(f"Múltiplos de 3 menores que {numero}:")
for i in range(3, numero, 3):
    print(i)

#Ejercicio 11
num = int(input("Ingrese un numero: "))
i = 2
suma = 0
while i <= num:
    if num % i == 0:
        suma += num//i
    i += 1
    
if suma == num:
    print("El numero es perfecto")
else:
    print("El numero NO es perfecto")
    
#Ejercicio 12
nota = int(input("Ingrese la nota (0-10): "))
if 0 <= nota <= 2:
    print("Muy malo")
elif 3 <= nota <= 4:
    print("Malo")
elif 5 <= nota <= 6:
    print("Regular")
elif 7 <= nota <= 8:
    print("Muy bueno")
elif 9 <= nota <= 10:
    print("Excelente")
else:
    print("La nota no se encuentra entre el rango de 0 y 10")
    
#Ejercicio 13
num = int(input("Introduce la altura de la pirámide: "))

for i in range(1, num + 1):
    asteriscos = '*' * (2 * i - 1)
    print(asteriscos)

#Ejercicio 14
altura = int(input("Introduce la altura de la pirámide invertida: "))

for i in range(altura, 0, -1):
    asteriscos = '*' * (2 * i - 1)
    print(asteriscos)

#Ejercicio 15
contador_lineas = 0

for numero in range(1, 300 + 1):
    if numero % 5 == 0 and numero % 7 == 0:
        tipo_multiplo = "Múltiplo de 5 y 7"
    elif numero % 5 == 0:
        tipo_multiplo = "Múltiplo de 5"
    elif numero % 7 == 0:
        tipo_multiplo = "Múltiplo de 7"
    else:
        tipo_multiplo = ""
    
    if tipo_multiplo:
        print(f"{numero}: {tipo_multiplo}")
    else:
        print(numero)
    
    contador_lineas += 1
    
    if contador_lineas % 6 == 0:
        print("-" * 20)
