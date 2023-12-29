import threading
from multiprocessing import Value
import time

from  apolo_11.src.usecase.ControlPanelMenu import ControlPanelMenu


cycle_time_lock = threading.Lock()

menu_app = ControlPanelMenu()




def request_reports_background_task(change_cycle_time, defined_cycle_frequency):
    while not change_cycle_time.is_set():
        with cycle_time_lock:
            local_cycle_time = defined_cycle_frequency.value

        time.sleep(local_cycle_time)
        print("\nPrograma de Simulacion APOLO_11 Solicitando reportes del estado de los vehiculos a cada una de las Misiones... (Periodicidad de la Ejecución: {} Segundos)".format(local_cycle_time)) 


def set_execution_frequency(defined_cycle_frequency):
    try:
        new_cycle_frequency_time = int(input("Ingrese la nueva frecuencia de ejecucion en segundos: "))
        if new_cycle_frequency_time > 0:
            with cycle_time_lock:
                defined_cycle_frequency.value = new_cycle_frequency_time
        else:
            print("Ingreso de Frecuencia Invalida. Por favor digite un numero entero valido.")
    except ValueError:
        print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 9.")


def main():

    while True:
        menu_app.showMenu()
        choice = input("\nIngrese su Eleccion (1, 2, 3... o 9): \n")

        if choice == '1':
            print("You selected Option 1.")
        elif choice == '2':
            print("You selected Option 2.")
        elif choice == '8':
            try:
                new_cycle_frequency_time = int(input("Ingrese la nueva frecuencia de ejecucion en segundos: "))
                if new_cycle_frequency_time > 0:
                    with cycle_time_lock:
                        defined_cycle_frequency.value = new_cycle_frequency_time
                else:
                    print("Ingreso Invalido. La frecuencia ingresada debe ser un numero entero positivo.")
            except ValueError:
                print("Ingreso de Frecuencia Invalida. Por favor digite un numero entero valido.")
        elif choice == '7':
            menu_app.run()
        elif choice == '9':
            change_cycle_time.set()
            break
        else:
            print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 9 ")
    
change_cycle_time = threading.Event()
defined_cycle_frequency = Value('i', 5)

background_thread = threading.Thread(target=request_reports_background_task, args=(change_cycle_time, defined_cycle_frequency), daemon=True)
background_thread.start()