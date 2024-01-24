import hashlib
from datetime import datetime


class MissionComponents:
    def __init__(self):
        self.componentes_espaciales = []

    def calcular_hash(self, *args: str) -> str:
        cadena_concatenada = "".join(map(str, args))
        hash_obj = hashlib.sha256(cadena_concatenada.encode())
        return hash_obj.hexdigest()

    def agregar_componente(
        self,
        mision: str,
        tipo_dispositivo: str,
        nombre_dispositivo: str,
        estado_dispositivo: str,
    ):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hash_componente = self.calcular_hash(
            fecha, mision, tipo_dispositivo, nombre_dispositivo, estado_dispositivo
        )

        componente = {
            "fecha": fecha,
            "mision": mision,
            "tipo_dispositivo": tipo_dispositivo,
            "nombre_dispositivo": nombre_dispositivo,
            "estado_dispositivo": estado_dispositivo,
            "hash": hash_componente,
        }

        self.componentes_espaciales.append(componente)
        print(f"Componente añadido:\n{componente}")

    def quitar_componente(self, hash_componente):
        for componente in self.componentes_espaciales:
            if componente["hash"] == hash_componente:
                self.componentes_espaciales.remove(componente)
                print(f"Componente eliminado:\n{componente}")
                return

        print(f"No se encontró un componente con el hash {hash_componente}")

    def mostrar_componentes(self):
        print("Componentes Espaciales:")
        for componente in self.componentes_espaciales:
            print(componente)


# Ejemplo de uso
gestor = MissionComponents()

gestor.agregar_componente("ColonyMoon", "Cohete", "Ares I", "Excellent")
gestor.agregar_componente("ColonyMoon", "Cohete", "Ares V", "Unknown")
gestor.agregar_componente("ColonyMoon", "Explorador", "Viper", "Unknown")

gestor.mostrar_componentes()

gestor.quitar_componente(gestor.componentes_espaciales[0]["hash"])

gestor.mostrar_componentes()
