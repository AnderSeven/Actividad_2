#cambios
clientes_lista = []
citas_medicas = []
class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []

class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}, Edad: {self.edad}")

class Perro(Mascota):
    def __init__(self, nombre, raza, edad):
        super().__init__(nombre, "Perro", raza, edad)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}")

class Gato(Mascota):
    def __init__(self, nombre, raza, edad):
        super().__init__(nombre, "Gato", raza, edad)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}")


class CitaMedica:
    def __init__(self, fecha, motivo, diagnostico):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico

def registrar_cliente():
    print("---Registro de clientes---")
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    correo = input("Ingrese el correo: ")
    cliente = Cliente(nombre, telefono, correo)
    clientes_lista.append(cliente)
    print("Clientre registrado")

def registrar_mascota():
    print("---Registro de mascotas---")
    nombre_cliente = input("Ingrese el nombre del propietario: ")
    cliente_encontrado = None
    for i in clientes_lista:
        if i.nombre == nombre_cliente:
            cliente_encontrado = i
    if cliente_encontrado == None:
        print("Cliente no encontrado")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    raza = input("Ingrese la raza: ")
    edad = input("Ingrese la edad: ")
    mascota = Mascota(nombre_mascota, especie, raza, edad)
    cliente_encontrado.mascotas.append(mascota)

def agendar_cita():
    print("---Agendar cita---")
    nombre_cliente = input("Ingrese el nombre del propietario: ")
    cliente_encontrado = None
    for i in clientes_lista:
        if i.nombre == nombre_cliente:
            cliente_encontrado = i
    if cliente_encontrado == None:
        print("Cliente no enocntrado")
        return
    if len(cliente_encontrado.mascotas) == 0:
        print("Este cliente no tiene mascotas registradas")
        return
    print("Mascotas del cliente:")
    for i in cliente_encontrado.mascotas:
        print(f"- Nombre: {i.nombre}, Especie: {i.especie}")
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    mascota_encontrada = None
    for i in cliente_encontrado.mascotas:
        if i.nombre == nombre_mascota:
            mascota_encontrada = i
    if mascota_encontrada == None:
        print("Mascota no encontrada")
        return
    fecha = input("Ingrese la fecha de la cita: ")
    motivo = input("Ingrese el motivo de la cita: ")
    diagnostico = input("ingrese el diagnotico: ")
    cita = CitaMedica(fecha, motivo, diagnostico)
    citas_medicas.append((cliente_encontrado, mascota_encontrada, cita))
    print("Cita medica agendada correctamente")

def historial_citas():
    if len(citas_medicas) == 0:
        print("No hay citas medicas registradas")
        return
    for cliente, mascota, cita in citas_medicas:
        print(f"Cliente: {cliente.nombre}")
        mascota.mostrar_info()
        print(f"Fecha: {cita.fecha}, Motivo: {cita.motivo}, Diagnostico: {cita.diagnostico}")
        print("-------------------------")

def mostrar_clientes_mascotas():
    if len(clientes_lista) == 0:
        print("No hay clientes registrados")
        return
    for cliente in clientes_lista:
        print(f"Cliente: {cliente.nombre}, Telefono: {cliente.telefono}, Correo: {cliente.correo}")
        if len(cliente.mascotas) == 0:
            print("No tiene mascotas registradas")
        else:
            for mascota in cliente.mascotas:
                mascota.mostrar_info()
        print("---------------------------")

a = False
while a == False:
    print("---Bienvenido a la clinita veterinaria---")
    print("1. Registrar nuevo cliente")
    print("2. Registrar nueva mascota")
    print("3. Agendar cita medica")
    print("4. Ver historial de citas")
    print("5. Ver clientes y mascotas")
    print("0. Salir")
    opciones = int(input("Ingrese una opcion: "))
    match opciones:
        case 0:
            print("Gracias por usar el sistema...")
            a = True
        case 1:
            registrar_cliente()
        case 2:
            registrar_mascota()
        case 3:
            agendar_cita()
        case 4:
            historial_citas()
        case 5:
            mostrar_clientes_mascotas()
        case _:
            print("Opcion invalida")