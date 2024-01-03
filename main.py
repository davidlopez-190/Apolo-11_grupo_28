import threading
import time

from configparser import ConfigParser
from apolo_11.menu_system import main_menu, commander_center_menu, leader_center_menu
from  apolo_11.src.helpers.utils.osystem import clear_console


config = ConfigParser()
config.read('./config.ini')
EXECUTION_PERIODICITY = int(config.get('apolo_11', 'cycle_frequency_time'))



def request_reports_missions():
    while True:
        time.sleep(EXECUTION_PERIODICITY)
        print("\nPrograma de Simulacion APOLO_11 Solicitando reportes del estado de los vehiculos a cada una de las Misiones... (Periodicidad de la Ejecución: {} Segundos)".format(EXECUTION_PERIODICITY)) 

def main():
    report_request_thread = threading.Thread(target=request_reports_missions)
    report_request_thread.daemon = True
    report_request_thread.start()

    current_menu = main_menu

    while True:
        clear_console()

        current_menu()
        choice = input("\nIngrese su Eleccion (1, 2, o 3): \n")

        if current_menu == main_menu:
            if choice == '1':
                current_menu = commander_center_menu
            elif choice == '2':
                current_menu = leader_center_menu
            elif choice == '3':
                break
            else:
                print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 3.")
        else:
            if choice == '0':
                current_menu = main_menu
            else:
                print("Eleccion Invalida. Por favor ingrese un 0.")

if __name__ == "__main__":
    main()
