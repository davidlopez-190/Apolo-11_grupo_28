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
