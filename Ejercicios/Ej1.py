class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.empleados = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

class Edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

empresa = Empresa("YooHoo!")
edificio_a = Edificio("A", "Nueva York")
edificio_b = Edificio("B", "Nueva York")
edificio_c = Edificio("C", "Los Ángeles")
ciudad_nueva_york = Ciudad("Nueva York")
ciudad_los_angeles = Ciudad("Los Ángeles")
empleado_martin = Empleado("Sr. Martin")
empleado_salim = Empleado("Sr. Salim")
empleado_xing = Empleado("Sra. Xing")

empresa.agregar_edificio(edificio_a)
empresa.agregar_edificio(edificio_b)
empresa.agregar_edificio(edificio_c)
empresa.agregar_empleado(empleado_martin)
empresa.agregar_empleado(empleado_salim)
empresa.agregar_empleado(empleado_xing)
ciudad_nueva_york.agregar_edificio(edificio_a)
ciudad_nueva_york.agregar_edificio(edificio_b)
ciudad_los_angeles.agregar_edificio(edificio_c)

empresa.edificios.remove(edificio_a)
empresa.edificios.remove(edificio_b)
empresa.empleados.remove(empleado_martin)
empresa.empleados.remove(empleado_salim)
empresa.empleados.remove(empleado_xing)
ciudad_nueva_york.edificios.remove(edificio_a)
ciudad_nueva_york.edificios.remove(edificio_b)

print("Edificios de la empresa YooHoo!:", [edificio.nombre for edificio in empresa.edificios])
print("Empleados de la empresa YooHoo!:", [empleado.nombre for empleado in empresa.empleados])
print("Edificios en Nueva York:", [edificio.nombre for edificio in ciudad_nueva_york.edificios])
print("Edificios en Los Ángeles:", [edificio.nombre for edificio in ciudad_los_angeles.edificios])