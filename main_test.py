from apolo_11.src.models.components import MissionComponents

gestor = MissionComponents()

gestor.cargar_componentes_desde_archivo("ColonyMoon")
gestor.mostrar_componentes()
gestor.agregar_componente("ColonyMoon", "Cohete", "Ares II")
gestor.mostrar_componentes()
gestor.guardar_componentes_en_archivo("ColonyMoon")
