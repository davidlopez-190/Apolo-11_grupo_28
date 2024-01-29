import json
from typing import Any, Dict

from apolo_11.src.helpers.utils.read_config import FullPaths, ReadConfig

registry_missions_path = FullPaths.registry_missions_file_path()
json_extension = ReadConfig.json_extension()
registry_file = f"{registry_missions_path}{json_extension}"


class MissionManager:
    def __init__(self):
        self.missions = self.read_missions_from_file()

    def read_missions_from_file(self):
        with open(registry_file, "r") as file:
            missions = json.load(file)
        return missions

    def write_missions_to_file(self):
        with open(registry_file, "w") as file:
            json.dump(self.missions, file, indent=2)

    def add_mission(
        self, mission: str, mnemonic: str, mission_type: str, mission_goal: str
    ):
        new_mission: Dict[str, Any] = {
            "mission": mission,
            "mnemonic": mnemonic,
            "mission_type": mission_type,
            "mission_goal": mission_goal,
        }
        self.missions.append(new_mission)
        self.write_missions_to_file()

    def remove_mission(self, mission_name: str):
        for mission in self.missions:
            if mission["mission"] == mission_name:
                self.missions.remove(mission)
                self.write_missions_to_file()
                print(f"Misión {mission_name} eliminada.")
                return
        print(f"No se encontró una misión con el nombre {mission_name}.")

    def generar_archivos_misiones(self) -> None:
        # Logica para generar archivos de salida de misiones desconocidas (pendiente)
        pass
