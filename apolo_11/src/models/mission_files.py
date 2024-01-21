import os
import random
import shutil
from datetime import datetime

from .mission import Mision


class MissionFiles:
    @staticmethod
    def generar_archivos_misiones():
        cantidad_archivos = random.randint(1, 5)
        for i in range(1, cantidad_archivos + 1):
            nombre_archivo = f"APLORBONE_{i}.json"
            ruta_json_personalizada = (
                "apolo_11/src/routes/missions/ColonyMoon_Components.json"
            )
            mision = Mision(path_mission_components=ruta_json_personalizada)
            mision.guardar_datos_en_archivo(nombre_archivo)

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


# Ejemplo de uso:
carpeta_a_limpiar = "apolo_11/src/routes/devices"
carpeta_origen = "apolo_11/src/routes/devices"
carpeta_destino = "apolo_11/src/routes/backup"

# MissionFiles.generar_archivos_misiones()
# MissionFiles.generar_backup_carpeta(carpeta_origen, carpeta_destino)
# MissionFiles.eliminar_archivos_carpeta(carpeta_a_limpiar)
