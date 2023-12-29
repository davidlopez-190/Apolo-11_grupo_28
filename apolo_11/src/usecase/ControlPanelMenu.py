import os
import json
import random
from datetime import datetime
import hashlib
import time

from  apolo_11.src.helpers.utils.OsSystem import clear_screen


class ControlPanelMenu:
    
    
    def showMenu(self):  
        time.sleep(3)
        clear_screen()  
        print("======================== Menu ========================") 
        print("1 - Ver Reportes Consolidados de las Misiones")
        print("2 - Analizar Eventos por estado")
        print("3 - Consolidar Misiones")
        print("4 - Gestionar Desconexiones")
        print("5 - Calcular Porcentaje de Datos")
        print("6 - Limpiar Archivos")
        print("7 - Acceder al Tablero de Control")
        print("8 - Establecer nueva frecuencia de ejecucion del programa")
        print("9 - Detener y Salir del programa")

    def showMissionControl(self):  
        time.sleep(3)
        clear_screen()  
        print("======================== Menu ========================") 
        print("1 - Ver todas las Misiones")
        print("2 - Crear un Componente de Mision")
        print("3 - Eliminar un Componente de Mision")
        print("4 - Regresar al Menu Anterior")

    def run(self):
        self.showMissionControl()
        while True:
            choice = input("Ingrese su Eleccion (1-3): ")
            if choice == '1':
                self.show_all_missions()
            elif choice == '2':
                self.createComponent()
            elif choice == '3':
                print("Tu seleccionaste la Opcion 3.")
            elif choice == '4':
                print("Tu seleccionaste la Opcion 1.")
            elif choice == '5':
                print("Saliendo del Programa.")
                break
            else:
                print("Eleccion Invalida. Por favor ingrese un numero comprendido entre el 1 y el 5.")
                

    def show_all_missions(self):
        file_path = os.path.join('apolo_11', 'src', 'routes', 'missions', 'registry_file_missions.json')

        try:
            with open(file_path, 'r') as file:
                missions = file.readlines()

            if missions:
                print("Misiones Disponibles:")
                for mission in missions:
                    print(mission.strip())
            else:
                print("Ninguna mision encontrada.")

        except FileNotFoundError:
            print(f"Archivo no encontrado: {file_path}")
        except Exception as e:
            print(f"Un error a ocurrido: {e}")
            
            
    def createComponent(self):
        # Get user input for mission name and device type
        mission_name = input("Enter the mission name (OrbitOne or VacMarc): ")
        device_type = input("Enter the type of device: ")

        # Get the current date and time
        creation_date = datetime.now().strftime("%d%m%y%H%M%S")

        # Generate a random status
        device_status = random.choice(["Excellent", "Good", "Warning", "Faulty", "Killed"])

        # Create a dictionary with the component information
        component_info = {
            "date": creation_date,
            "mission": mission_name,
            "device_type": device_type,
            "device_status": device_status
        }

        # Calculate hash
        component_info["hash"] = self.calculate_hash(component_info)
        
        # Save the component information to the existing or new JSON file
        file_path = os.path.join('apolo_11', 'src', 'routes', 'missions', f'{mission_name}_Components.json')
        
        
        if os.path.exists(file_path):
            # If the file already exists, read the content and parse it
            with open(file_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []

            # Append the new component to the existing data
            existing_data.append(component_info)

            # Save the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=2)
        else:
            # If the file doesn't exist, create a new file with the new component
            with open(file_path, 'w') as file:
                json.dump([component_info], file, indent=2)

        print("Component created and saved successfully.")

    def calculate_hash(self, data):
        data_str = json.dumps(data, sort_keys=True).encode('utf-8')
        return hashlib.sha256(data_str).hexdigest()