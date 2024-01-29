import json

from apolo_11.src.helpers.utils.read_config import FullPaths, ReadConfig

registry_missions_path = FullPaths.registry_missions_file_path()
json_extension = ReadConfig.json_extension()


class MissionHandler:
    def __init__(self):
        self.missions = self.read_missions_from_file()

    def read_missions_from_file(self):
        registry_file = f"{registry_missions_path}{json_extension}"

        with open(registry_file, "r") as file:
            missions = json.load(file)
        return missions

    def print_missions(self):
        print("\nLista de Misiones:")
        for mission in self.missions:
            print(f"\nMission: {mission['mission']}")
            print(f"Mnemonic: {mission['mnemonic']}")
            print(f"Mission Type: {mission['mission_type']}")
            print(f"Mission Goal: {mission['mission_goal']}")
            print("------------------------")

    def get_all_missions_info(self):
        missions_info = "\nLista de Misiones:\n"
        for mission in self.missions:
            missions_info += f"\nMission: {mission['mission']}\n"
            missions_info += f"Mnemonic: {mission['mnemonic']}\n"
            missions_info += f"Mission Type: {mission['mission_type']}\n"
            missions_info += f"Mission Goal: {mission['mission_goal']}\n"
            missions_info += "------------------------\n"
        return missions_info
