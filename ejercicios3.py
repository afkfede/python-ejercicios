#Ejercicio 1
class Persona():
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_edad(self, edad):
        self.edad = edad
        
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def print_persona(self):
        print(f"Nombre: {self.get_nombre()}. Edad: {self.get_edad()}")
        
persona = Persona()
persona.set_nombre("Marcos")
persona.set_edad(15)

persona2 = Persona()
persona2.set_nombre("Juan")
persona2.set_edad(20)

persona.print_persona()
persona2.print_persona()

#Ejercicio 2
class Persona():
    
    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def print_persona(self):
        print(f"Nombre: {self.nombre}. Edad: {self.edad}")
        
persona = Persona()
persona.constructor("Maria", 28)
persona.print_persona()
persona2 = Persona()
persona2.constructor("Laura", 19)
persona2.print_persona()

#Ejercicio 3
class Persona():
    
    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def print_persona(self):
        print(f"Nombre: {self.nombre}. Edad: {self.edad}")
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
persona = Persona()
persona.constructor("Maria", 28)
persona.print_persona()
print(f"¿{persona.nombre} es mayor de edad? {persona.es_mayor_de_edad()}")
persona2 = Persona()
persona2.constructor("Laura", 17)
persona2.print_persona()
print(f"¿{persona2.nombre} es mayor de edad? {persona2.es_mayor_de_edad()}")

#Ejercicio 4
class Persona():
    
    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def print_persona(self):
        print(f"Nombre: {self.nombre}. Edad: {self.edad}")
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.edad
    
persona = Persona()
persona.constructor("Maria", 28)
persona.print_persona()
print(f"¿{persona.nombre} es mayor de edad? {persona.es_mayor_de_edad()}")
persona2 = Persona()
persona2.constructor("Laura", 17)
persona2.print_persona()
print(f"¿{persona2.nombre} es mayor de edad? {persona2.es_mayor_de_edad()}\n")

if persona.es_mayor_que(persona2):
    print(f"{persona.nombre} es mayor que {persona2.nombre}")
else:
    print(f"{persona.nombre} no es mayor que {persona2.nombre}")
    
#Ejercicio 5
class Persona():
    
    def constructor(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def print_persona(self):
        print(f"Nombre: {self.nombre}. Edad: {self.edad}")
        
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def get_mayor(persona, persona2):
        return persona if persona.edad > persona2.edad else persona2
    
persona = Persona()
persona.constructor("Carlos", 14)
persona.print_persona()
print(f"¿{persona.nombre} es mayor de edad? {persona.es_mayor_de_edad()}")
persona2 = Persona()
persona2.constructor("Luciano", 17)
persona2.print_persona()
print(f"¿{persona2.nombre} es mayor de edad? {persona2.es_mayor_de_edad()}\n")

mayor = Persona.get_mayor(persona, persona2)
print(f"{mayor.nombre} es el mayor con {mayor.edad} años")

#Ejercicio 6
class Alumno():
    
    def constructor(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def print_alumno(self):
        print(f"Alumno: {self.nombre}. Nota: {self.nota}")
        
    def aprobado(self):
        return "Aprobado" if self.nota >= 4 else "Desaprobado"
        
alumno = Alumno()
alumno.constructor("Roberto Alonso", 8)
alumno.print_alumno()
print(f"Con nota {alumno.nota}, su estado es: {alumno.aprobado()}\n")

alumno2 = Alumno()
alumno2.constructor("Dario Juarez", 3)
alumno2.print_alumno()
print(f"Con nota {alumno2.nota}, su estado es: {alumno2.aprobado()}")

#Ejercicio 7
class Triangulo():
    
    def constructor(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)
    
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"
        
lado1 = int(input("Ingrese lado 1: "))
lado2 = int(input("Ingrese lado 2: "))
lado3 = int(input("Ingrese lado 3: "))

triangulo = Triangulo()
triangulo.constructor(lado1, lado2, lado3)
print(f"Valor del lado mayor: {triangulo.lado_mayor()}")
print(f"Tipo de triangulo: {triangulo.tipo()}")

#Ejercicio 8
class Calculadora():
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def suma(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        return self.numero1 / self.numero2
    
calculo = Calculadora(4, 5)
print(f"Numeros {calculo.numero1} y {calculo.numero2}")
print(f"Suma: {calculo.suma()}")
print(f"Resta: {calculo.resta()}")
print(f"Multiplicación: {calculo.multiplicacion()}")
print(f"Division: {calculo.division()}")

#Ejercicio 9
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("\n***//////////***")
        print("Contacto añadido.")
        print("***//////////***")

    def listar_contactos(self):
        if not self.contactos:
            print("\n***//////////***")
            print("No hay contactos en la agenda.")
            print("***//////////***")
            return
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(contacto)
                return
        print("Contacto no encontrado.")

    def editar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_nombre = input("Nuevo nombre (no ingresar nada para dejar como está): ")
                nuevo_telefono = input("Nuevo teléfono (no ingresar nada para dejar como está): ")
                nuevo_email = input("Nuevo email (no ingresar nada para dejar como está): ")

                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nuevo_email:
                    contacto.email = nuevo_email
                
                print("\n***//////////***")
                print("Contacto actualizado.")
                print("***//////////***")
                return
        print("\n***//////////***")
        print("Contacto no encontrado.")
        print("***//////////***")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.añadir_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                nombre = input("Nombre del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Nombre del contacto a editar: ")
                self.editar_contacto(nombre)
            elif opcion == '5':
                print("\n***//////////***")
                print("Cerrando agenda.")
                print("***//////////***")
                break
            else:
                print("Opción invalida, ingrese una opción correcta.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
    
#Ejercicio 10
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        if monto > 0:
            self.cantidad += monto
            print(f"{self.nombre} ha depositado ${monto}. Nuevo saldo: ${self.cantidad}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def extraer(self, monto):
        if 0 < monto <= self.cantidad:
            self.cantidad -= monto
            print(f"{self.nombre} ha extraído ${monto}. Nuevo saldo: ${self.cantidad}.")
        else:
            print("Monto no válido para la extracción.")

    def mostrar_total(self):
        print(f"Saldo de {self.nombre}: ${self.cantidad}")


class Banco:
    def __init__(self):
        self.clientes = []
        self.total_depositado = 0

    def agregar_cliente(self, nombre):
        nuevo_cliente = Cliente(nombre)
        self.clientes.append(nuevo_cliente)

    def operar(self):
        while True:
            nombre_cliente = input("Ingrese el nombre del cliente para realizar una operación en la cuenta (o 'salir' para terminar): ")
            if nombre_cliente.lower() == 'salir':
                break
            cliente = next((c for c in self.clientes if c.nombre.lower() == nombre_cliente.lower()), None)
            if cliente:
                operacion = input("¿Desea depositar o extraer? (d/e): ")
                if operacion.lower() == 'd':
                    monto = float(input("Ingrese el monto a depositar: "))
                    cliente.depositar(monto)
                    self.total_depositado += monto
                elif operacion.lower() == 'e':
                    monto = float(input("Ingrese el monto a extraer: "))
                    cliente.extraer(monto)
                else:
                    print("Operación no válida.")
            else:
                print("Cliente no encontrado.")

    def deposito_total(self):
        print(f"Total de dinero depositado hoy: ${self.total_depositado}")

if __name__ == "__main__":
    banco = Banco()
    
    for i in range(3):
        nombre_cliente = input(f"Ingrese el nombre del cliente {i + 1}: ")
        banco.agregar_cliente(nombre_cliente)

    banco.operar()
    banco.deposito_total()