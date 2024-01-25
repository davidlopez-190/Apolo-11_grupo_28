import os
import random
import shutil
from datetime import datetime

from ..helpers.utils.read_config import FullPaths, ReadConfig
from .mission import Mision

backuppath = FullPaths.backup_path()
missions_path = FullPaths.missions_path()
prefix = ReadConfig.prefix_mision_file_name()
prefix_components = ReadConfig.prefix_components()
json_extension = ReadConfig.json_extension()
file_number_range = ReadConfig.file_number_range()
mission_prefix = ReadConfig.mission_dict()
mission_type_list = ReadConfig.mission_type_list()


class MissionFiles:
    @staticmethod
    def generar_archivos_misiones():
        cantidad_archivos = random.randint(1, file_number_range)
        for p in mission_prefix:
            for i in range(1, cantidad_archivos + 1):
                mnemonic_value = mission_prefix[p]
                mission_type_choice = random.choice(mission_type_list)
                nombre_archivo = f"{prefix}{mnemonic_value}{i}{json_extension}"
                ruta_json_personalizada = os.path.join(
                    missions_path, f"{p}{prefix_components}{json_extension}"
                )
                mision = Mision(
                    path_mission_components=ruta_json_personalizada,
                    mission_name=p,
                    mission_type=mission_type_choice,
                    mission_goal="test",
                )
                mision.guardar_datos_en_archivo(nombre_archivo, p)

    @staticmethod
    def generar_backup_carpeta(carpeta_origen: str, carpeta_destino: str):
        if not os.path.exists(carpeta_origen):
            print(f"La carpeta de origen '{carpeta_origen}' no existe.")
            return

        fecha_actual = datetime.now().strftime("%Y%m%d%H%M%S")

        for archivo_nombre in os.listdir(carpeta_origen):
            archivo_origen = os.path.join(carpeta_origen, archivo_nombre)

            if os.path.isfile(archivo_origen):
                nombre_base, extension = os.path.splitext(archivo_nombre)
                nombre_backup = f"{nombre_base}_backup_{fecha_actual}{extension}"
                ruta_backup = os.path.join(carpeta_destino, nombre_backup)

                try:
                    shutil.copy(archivo_origen, ruta_backup)
                    print(
                        f"Se ha generado un respaldo de '{archivo_origen}' en '{ruta_backup}'."
                    )
                except Exception as e:
                    print(f"Error al generar el respaldo para '{archivo_origen}': {e}")

    @staticmethod
    def eliminar_archivos_carpeta(carpeta: str):
        if not os.path.exists(carpeta):
            print(f"La carpeta '{carpeta}' no existe.")
            return

        for archivo_nombre in os.listdir(carpeta):
            archivo_ruta = os.path.join(carpeta, archivo_nombre)

            if os.path.isfile(archivo_ruta):
                try:
                    os.remove(archivo_ruta)
                    print(f"Se ha eliminado el archivo: {archivo_ruta}")
                except Exception as e:
                    print(f"Error al eliminar el archivo '{archivo_ruta}': {e}")
