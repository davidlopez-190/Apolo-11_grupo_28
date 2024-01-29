import hashlib
import json
import os
import random
from datetime import datetime
from typing import Any, Dict, List

from ..helpers.utils.read_config import FullPaths, ReadConfig

component_state_list = ReadConfig.component_state_list()
missions_path = FullPaths.missions_path()
prefix_components = ReadConfig.prefix_components()
json_extension = ReadConfig.json_extension()


class MissionComponents:
    def __init__(self):
        self.componentes_espaciales: List[Dict[str, Any]] = []

    def cargar_componentes_desde_archivo(self, mission: str) -> None:
        file_component = os.path.join(
            missions_path, f"{mission}{prefix_components}{json_extension}"
        )
        try:
            with open(file_component, "r") as file:
                data = json.load(file)
                self.componentes_espaciales = data
                print(f"Componentes cargados desde {file_component}")
        except FileNotFoundError:
            print(f"El archivo {file_component} no existe.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON {file_component}")

    def calcular_hash(self, *args: str) -> str:
        cadena_concatenada = "".join(map(str, args))
        hash_obj = hashlib.sha256(cadena_concatenada.encode())
        return hash_obj.hexdigest()

    def agregar_componente(
        self, mission: str, device_type: str, device_name: str
    ) -> None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        device_status = random.choice(component_state_list)
        hash_componente = self.calcular_hash(
            date, mission, device_type, device_name, device_status
        )

        componente: Dict[str, Any] = {
            "date": date,
            "mission": mission,
            "device_type": device_type,
            "device_name": device_name,
            "device_status": device_status,
            "hash": hash_componente,
        }

        self.componentes_espaciales.append(componente)
        print(f"Componente añadido:\n{componente}")

    def quitar_componente(self, device_name: str) -> None:
        for componente in self.componentes_espaciales:
            if componente["device_name"] == device_name:
                print(f"Componente eliminado:\n{componente}")
                self.componentes_espaciales.remove(componente)
                print(f"Componente eliminado:\n{componente}")
                return

        print(f"No se encontró un componente con el nombre {device_name}")

    def guardar_componentes_en_archivo(self, mission: str) -> None:
        file_component = os.path.join(
            missions_path, f"{mission}{prefix_components}{json_extension}"
        )
        with open(file_component, "w") as file:
            json.dump(self.componentes_espaciales, file, indent=2)
            print(f"Componentes guardados en {file_component}")

    def mostrar_componentes(self):
        print("Componentes Espaciales:")
        # for componente in self.componentes_espaciales:
        print(self.componentes_espaciales)
