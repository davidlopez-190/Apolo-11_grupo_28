import json
import os
from typing import Any, Dict

from apolo_11.src.helpers.utils.read_config import FullPaths

devicespath = FullPaths.devices_path()
reportspath = FullPaths.reports_path()


class UnknownStatusReport:
    def __init__(self):
        self.carpeta_json = devicespath
        self.carpeta_resultados = reportspath
        self.contador_por_mision_y_dispositivo: Dict[str, Any] = {}

    def analizar_archivos(self):
        for nombre_archivo in os.listdir(self.carpeta_json):
            if nombre_archivo.endswith(".json"):
                ruta_archivo = os.path.join(self.carpeta_json, nombre_archivo)
                self._analizar_archivo(ruta_archivo)

    def _analizar_archivo(self, ruta_archivo: str):
        with open(ruta_archivo) as json_file:
            data = json.load(json_file)

        for dispositivo in data["dispositivos_espaciales"]:
            if dispositivo["device_status"].lower() == "desconocido":
                nombre_dispositivo = dispositivo["device_name"]
                nombre_mision = data["nombre_mision"]

                clave = (nombre_mision, nombre_dispositivo)
                self.contador_por_mision_y_dispositivo[clave] = (
                    self.contador_por_mision_y_dispositivo.get(clave, 0) + 1
                )

    def imprimir_resultados(self):
        print(
            "Cantidad de veces que cada dispositivo tiene el estado 'Desconocido' por misión:"
        )
        for (
            nombre_mision,
            nombre_dispositivo,
        ), cantidad in self.contador_por_mision_y_dispositivo.items():
            print(
                f"Misión: {nombre_mision}, Dispositivo: {nombre_dispositivo}, Cantidad: {cantidad} veces"
            )

    def guardar_resultados_en_json(self):
        resultados_json = {
            "resultados": [
                {"mision": mision, "dispositivo": dispositivo, "cantidad": cantidad}
                for (
                    mision,
                    dispositivo,
                ), cantidad in self.contador_por_mision_y_dispositivo.items()
            ]
        }

        ruta_resultados = os.path.join(
            self.carpeta_resultados, "APLSTATS-UNKNOWN_STATUS.json"
        )
        with open(ruta_resultados, "w") as json_resultados:
            json.dump(resultados_json, json_resultados, indent=2)
