import random

class Mision:
    def __init__(self, nombre, descripcion, fecha_lanzamiento, fecha_fin):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_lanzamiento = fecha_lanzamiento
        self.fecha_fin = fecha_fin
        self.dispositivo_espacial = None
        self.objetivos = []  # Lista de objetivos de la misión

    def asignar_dispositivo_espacial(self, dispositivo_espacial):
        self.dispositivo_espacial = dispositivo_espacial

    def agregar_objetivo(self, objetivo):
        self.objetivos.append(objetivo)

    def listar_objetivos(self):
        print(f"Objetivos de la misión '{self.nombre}':")
        for objetivo in self.objetivos:
            print(f"- {objetivo}")

    def obtener_estado_mision(self):
        if self.dispositivo_espacial:
            return f"La misión '{self.nombre}' está actualmente en curso con {self.dispositivo_espacial.tipo} '{self.dispositivo_espacial.nombre}'."
        else:
            return f"La misión '{self.nombre}' aún no ha sido asignada a ningún dispositivo espacial."

    def finalizar_mision(self):
        if self.dispositivo_espacial:
            print(f"La misión '{self.nombre}' ha sido completada. {self.dispositivo_espacial.tipo} '{self.dispositivo_espacial.nombre}' regresa a la Tierra.")
        else:
            print(f"No se puede finalizar la misión '{self.nombre}' ya que no hay ningún dispositivo espacial asignado.")

    def generar_datos_aleatorios(self):
        # Generar fechas aleatorias para la misión
        self.fecha_lanzamiento = f"{random.randint(2025, 2030)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        self.fecha_fin = f"{random.randint(2031, 2035)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

        # Generar un número aleatorio de objetivos para la misión (entre 1 y 5)
        num_objetivos = random.randint(1, 5)
        for _ in range(num_objetivos):
            objetivo = f"Objetivo {random.randint(1, 100)}"
            self.objetivos.append(objetivo)

        # Generar un mensaje aleatorio para la descripción de la misión
        mensajes_descripcion = [
            "Misión de exploración",
            "Misión de investigación científica",
            "Misión de búsqueda de vida extraterrestre",
            "Misión de recolección de muestras"
        ]
        self.descripcion = random.choice(mensajes_descripcion)




report = ['Hello! This is the OrbitOne Report!']