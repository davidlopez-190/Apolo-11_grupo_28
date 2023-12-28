import threading
from multiprocessing import Value
import time

from  apolo_11.src.usecase.MainMenu import showMenu

cycle_time_lock = threading.Lock()



def request_reports_background_task(cycle_time_event, cycle_time_var):
    while not cycle_time_event.is_set():
        with cycle_time_lock:
            local_cycle_time = cycle_time_var.value

        time.sleep(local_cycle_time)
        print("\nPrograma de Simulacion APOLO_11 Solicitando reportes del estado de los vehiculos a cada una de las Misiones... (Periodicidad de la Ejecución: {} Segundos)".format(local_cycle_time))



def set_execution_frequency(cycle_time_var):
    try:
        new_cycle_time = int(input("Ingrese la nueva frecuencia de ejecucion en segundos: "))
        if new_cycle_time > 0:
            with cycle_time_lock:
                cycle_time_var.value = new_cycle_time
        else:
            print("Ingreso de Frecuencia Invalida. Por favor digite un numero entero valido.")
    except ValueError:
        print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 9.")


def main():
    
    cycle_time_event = threading.Event()
    cycle_time_var = Value('i', 10)

    background_thread = threading.Thread(target=request_reports_background_task, args=(cycle_time_event, cycle_time_var), daemon=True)
    background_thread.start()

    while True:
        showMenu()
        choice = input("\nIngrese su Eleccion (1, 2, 3... o 9): \n")

        if choice == '1':
            print("You selected Option 1.")
        elif choice == '2':
            print("You selected Option 2.")
        elif choice == '7':
            try:
                new_cycle_time = int(input("Ingrese la nueva frecuencia de ejecucion en segundos: "))
                if new_cycle_time > 0:
                    with cycle_time_lock:
                        cycle_time_var.value = new_cycle_time
                else:
                    print("Ingreso Invalido. La frecuencia ingresada debe ser un numero entero positivo.")
            except ValueError:
                print("Ingreso de Frecuencia Invalida. Por favor digite un numero entero valido.")
        elif choice == '9':
            cycle_time_event.set()
            break
        else:
            print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 9 ")
