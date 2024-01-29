from apolo_11.src.models.unknown_status_report import UnknownStatusReport

analizador = UnknownStatusReport()
analizador.analizar_archivos()
analizador.imprimir_resultados()
analizador.guardar_resultados_en_json()
