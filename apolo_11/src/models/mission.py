import json
import os
from configparser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read("./config.ini")


class Mision:
    def __init__(self, path_mission_components: str):
        self.mission_components = self.load_components(path_mission_components)
        self.fecha_lanzamiento = self.generar_fecha_lanzamiento()

    def load_components(self, path_mission_components: str):
        with open(path_mission_components, "r") as components:
            components_data = json.load(components)
        return components_data

    def generar_fecha_lanzamiento(self):
        return datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "nombre_mision": "OrbitOne",
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "tipo_mision": "test",
            "objetivos_mision": "test",
            "dispositivos_espaciales": self.mission_components,
        }

    def guardar_datos_en_archivo(self, nombre_archivo: str) -> None:
        ruta_directorio = "apolo_11/src/routes/devices/"  # mejorar los / \ dependiendo del OS, agregar metodo en el objeto Apolo-11_grupo_28\apolo_11\src\helpers\utils\os_system.py
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

        try:
            if not os.path.exists(ruta_directorio):
                os.makedirs(ruta_directorio)

            with open(ruta_completa, "w") as file:
                json.dump(self.to_dict(), file, indent=2)
            print(
                f"Los datos de la misión 'Nombre mision' se han guardado en el archivo: {ruta_completa}"
            )
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")


# Prueba:
ruta_json_personalizada = "apolo_11/src/routes/missions/ColonyMoon_Components.json"
mision = Mision(path_mission_components=ruta_json_personalizada)
datos_mision = mision.to_dict()
mision.guardar_datos_en_archivo("APLORBONE_0001.json")
