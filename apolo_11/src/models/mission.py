import json
import os
from datetime import datetime

from ..helpers.utils.read_config import FullPaths

devicespath = FullPaths.devices_path()


class Mision:
    def __init__(
        self,
        path_mission_components: str,
        mission_name: str,
        mission_type: str,
        mission_goal: str,
    ) -> None:
        self.mission_components = self.load_components(path_mission_components)
        self.fecha_lanzamiento = self.generar_fecha_lanzamiento()
        self.dict_file = self.to_dict(mission_name, mission_type, mission_goal)

    def load_components(self, path_mission_components: str):
        with open(path_mission_components, "r") as components:
            components_data = json.load(components)
        return components_data

    def generar_fecha_lanzamiento(self):
        return datetime.now().strftime("%Y-%m-%d")

    def to_dict(self, mission_name: str, mission_type: str, mission_goal: str):
        return {
            "nombre_mision": mission_name,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "tipo_mision": mission_type,
            "objetivos_mision": mission_goal,
            "dispositivos_espaciales": self.mission_components,
        }

    def guardar_datos_en_archivo(self, nombre_archivo: str, mission_name2: str) -> None:
        ruta_directorio = devicespath
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

        try:
            if not os.path.exists(ruta_directorio):
                os.makedirs(ruta_directorio)

            with open(ruta_completa, "w") as file:
                json.dump(self.dict_file, file, indent=2)
            print(
                f"Los datos de la misión {mission_name2} se han guardado en el archivo: {ruta_completa}"
            )
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")


# Prueba:
# ruta_json_personalizada = "apolo_11/src/routes/missions/ColonyMoon_Components.json"
# mision = Mision(path_mission_components=ruta_json_personalizada)
# datos_mision = mision.to_dict()
# mision.guardar_datos_en_archivo("APLORBONE_0001.json")
