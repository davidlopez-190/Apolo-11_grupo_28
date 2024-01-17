import random
import uuid
from datetime import datetime, timedelta
import json
import os

class Mision:
    def __init__(self, nombre_mision=None):
        self.tipos_dispositivo = self.cargar_tipos_dispositivo()
        self.estados_dispositivo = self.cargar_estados_dispositivo()
        self.misiones = self.cargar_misiones()
        self.mision_actual = self.seleccionar_mision(nombre_mision)
        self.nombre_mision = self.mision_actual["nombre"]
        self.tipo_mision = self.mision_actual["tipo"]
        self.objetivos_mision = self.mision_actual["objetivos"]
        self.fecha_lanzamiento = self.generar_fecha_lanzamiento()
        self.dispositivos_espaciales = self.generar_dispositivos_espaciales()

    def cargar_tipos_dispositivo(self):
        with open('apolo_11\src\constants\configuracion.json', 'r') as file:
            config = json.load(file)
            return config.get('tipos_dispositivo', [])

    def cargar_estados_dispositivo(self):
        with open('apolo_11\src\constants\configuracion.json', 'r') as file:
            config = json.load(file)
            return config.get('estados_dispositivo', [])

    def cargar_misiones(self):
        with open('apolo_11\src\constants\configuracion.json', 'r') as file:
            config = json.load(file)
            return config.get('misiones', [])

    def seleccionar_mision(self, nombre_mision=None):
        if nombre_mision:
            for mision in self.misiones:
                if mision["nombre"] == nombre_mision:
                    return mision

        return random.choice(self.misiones)

    def generar_fecha_lanzamiento(self):
        return datetime.now().strftime("%Y-%m-%d")

    def generar_dispositivos_espaciales(self):
        num_dispositivos = random.randint(1, 5)
        dispositivos = []
        for _ in range(num_dispositivos):
            dispositivo = {
                "id_dispositivo": str(uuid.uuid4()),
                "tipo_dispositivo": random.choice(self.tipos_dispositivo),
                "estado_dispositivo": random.choice(self.estados_dispositivo)
            }
            dispositivos.append(dispositivo)
        return dispositivos

    def to_dict(self):
        return {
            "nombre_mision": self.nombre_mision,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "tipo_mision": self.tipo_mision,
            "objetivos_mision": self.objetivos_mision,
            "dispositivos_espaciales": self.dispositivos_espaciales
        }
    def guardar_datos_en_archivo(self, nombre_archivo):
        ruta_directorio = "apolo_11/src/routes/devices/"
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)
        
        try:
            if not os.path.exists(ruta_directorio):
                os.makedirs(ruta_directorio)

            with open(ruta_completa, 'w') as file:
                json.dump(self.to_dict(), file, indent=2)
            print(f"Los datos de la misión '{self.nombre_mision}' se han guardado en el archivo: {ruta_completa}")
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")
# Ejemplo de uso:
mision = Mision(nombre_mision="Misión OrbitOne")
datos_mision = mision.to_dict()
datos_mision_consola = json.dumps(datos_mision, indent=4)
print(datos_mision)
mision.guardar_datos_en_archivo("APLORBONE_0001.json")
