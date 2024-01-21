import threading
import time

from apolo_11.menu_system import commander_center_menu, leader_center_menu, main_menu
from apolo_11.src.helpers.utils.os_system import OsSystem
from apolo_11.src.helpers.utils.read_config import ReadConfig
from apolo_11.src.models.mission_files import MissionFiles

EXECUTION_PERIODICITY = ReadConfig.cycle_frequency_time()


def request_reports_missions():
    while True:
        time.sleep(EXECUTION_PERIODICITY)
        print(
            "\nPrograma de Simulacion APOLO_11 Solicitando reportes del estado de los vehiculos a cada una de las Misiones... (Periodicidad de la Ejecución: {} Segundos)".format(
                EXECUTION_PERIODICITY
            )
        )
        carpeta_a_limpiar = "apolo_11/src/routes/devices"
        carpeta_origen = "apolo_11/src/routes/devices"
        carpeta_destino = "apolo_11/src/routes/backup"

        MissionFiles.eliminar_archivos_carpeta(carpeta_a_limpiar)
        MissionFiles.generar_archivos_misiones()
        MissionFiles.generar_backup_carpeta(carpeta_origen, carpeta_destino)


def main():
    report_request_thread = threading.Thread(target=request_reports_missions)
    report_request_thread.daemon = True
    report_request_thread.start()

    current_menu = main_menu

    while True:
        OsSystem.clear_console()

        current_menu()
        choice = input("\nIngrese su Eleccion (1, 2, o 3): \n")

        if current_menu == main_menu:
            if choice == "1":
                current_menu = commander_center_menu
            elif choice == "2":
                current_menu = leader_center_menu
            elif choice == "3":
                break
            else:
                print(
                    "Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 3."
                )
        else:
            if choice == "0":
                current_menu = main_menu
            else:
                print("Eleccion Invalida. Por favor ingrese un 0.")


if __name__ == "__main__":
    main()
