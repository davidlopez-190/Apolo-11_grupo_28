from  apolo_11.src.usecase.StartSynchronize import syncUp,captureLogs

def init_app():
   print("Iniciando Sistema de Monitoreo Unificado...")
   print("--------------------------------------------")
   print(syncUp)
   print("--------------------------------------------")
   print(captureLogs)
   print("--------------------------------------------")
   
   
   while True:
    print("Desea ver mas? Seleccione una opción:")
    print("--------------------------------------------")
    print("1 - Ver Reportes Consolidados de las Misiones")
    print("2 - Acceder al Tablero de Control por parte de las Misiones")
    print("3 - Analizar Eventos por estado")
    print("4 - Consolidar Misiones")
    print("5 - Gestionar Desconexiones")
    print("6 - Calcular Porcentaje de Datos")
    print("7 - Limpiar Archivos")
    print("8 - Detener y Salir del programa")
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion == '1':
      pass
    elif opcion == '2':
       pass
    elif opcion == '8':
        print("Gracias por utilizar el Sistema de Monitoreo Unificado.")
        break 
    else:
        print("Opción inválida. Intente de nuevo.")
        
        

   
   

