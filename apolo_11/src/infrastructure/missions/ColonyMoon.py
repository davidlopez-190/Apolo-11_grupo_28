from missions.misiones import Mision
class MisionEspecial(Mision):
    def __init__(self, nombre_mision=None):
        super().__init__(nombre_mision)
        self.cargo_especial = self.generar_cargo_especial()

    def generar_cargo_especial(self):
        return f"Cargo especial para {self.nombre_mision}"

    def to_dict_especial(self):
        datos_mision = self.to_dict()
        datos_mision["cargo_especial"] = self.cargo_especial
        return datos_mision

# Ejemplo de uso de la clase MisionEspecial:
mision_especial = MisionEspecial(nombre_mision="Misión Beta")
datos_mision_especial = mision_especial.to_dict_especial()
print(datos_mision_especial)
