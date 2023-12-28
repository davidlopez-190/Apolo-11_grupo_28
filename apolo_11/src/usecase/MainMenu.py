import os
import time

from  apolo_11.src.helpers.utils.oSystem import clear_screen


def showMenu():  
  time.sleep(3)
  clear_screen()  
  print("======================== Menu ========================") 
  print("1 - Ver Reportes Consolidados de las Misiones")
  print("2 - Analizar Eventos por estado")
  print("3 - Consolidar Misiones")
  print("4 - Gestionar Desconexiones")
  print("5 - Calcular Porcentaje de Datos")
  print("6 - Limpiar Archivos")
  print("7 - Establecer nueva frecuencia de ejecucion del programa")
  print("8 - Acceder al Tablero de Control por parte de las Misiones")
  print("9 - Detener y Salir del programa")
