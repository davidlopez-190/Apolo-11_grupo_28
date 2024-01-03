import threading
import time
from apolo_11.menu_system import main_menu, commander_center_menu, leader_center_menu
from  apolo_11.src.helpers.utils.osystem import clear_console


def background_task():
    while True:
        time.sleep(20)
        print("\nPrograma de Simulacion APOLO_11 Solicitando reportes del estado de los vehiculos a cada una de las Misiones... (Periodicidad de la Ejecución: 20 Segundos)") 

def main():
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True
    background_thread.start()

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
