import json
import os
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")


class ReadConfig:
    @staticmethod
    def cycle_frequency_time() -> int:
        periodicity = int(config.get("apolo_11", "cycle_frequency_time"))
        return periodicity

    @staticmethod
    def prefix_mision_file_name() -> str:
        prefix = str(config.get("apolo_11", "prefix_mision_file_name"))
        return prefix

    @staticmethod
    def json_extension() -> str:
        json_extension = str(config.get("apolo_11", "json_extension"))
        return json_extension

    @staticmethod
    def file_number_range() -> int:
        file_number_range = int(config.get("apolo_11", "file_number_range"))
        return file_number_range

    @staticmethod
    def mission_dict():
        mission_json = config.get("apolo_11", "missions")
        mission_dict = json.loads(mission_json)
        print(mission_dict)
        return mission_dict

    @staticmethod
    def prefix_components():
        prefix_components = str(config.get("apolo_11", "prefix_components"))
        return prefix_components

    @staticmethod
    def mission_type_list():
        mission_str = config.get("apolo_11", "mission_type")
        mission_type_list = [str(value.strip()) for value in mission_str.split(",")]
        return mission_type_list

    @staticmethod
    def component_state_list():
        statate_str = config.get("apolo_11", "components_states")
        component_state_list = [str(value.strip()) for value in statate_str.split(",")]
        return component_state_list


class FullPaths:
    @staticmethod
    def devices_path() -> str:
        devices_path = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "routes_folder_name"),
            config.get("apolo_11", "devices_folder_name"),
        )
        return devices_path

    @staticmethod
    def backup_path() -> str:
        backup_path = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "routes_folder_name"),
            config.get("apolo_11", "backup_folder_name"),
        )
        return backup_path

    @staticmethod
    def missions_path() -> str:
        colonymoon_path_json = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "routes_folder_name"),
            config.get("apolo_11", "missions_folder_name"),
        )
        return colonymoon_path_json

    @staticmethod
    def reports_path() -> str:
        reports_path_json = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "routes_folder_name"),
            config.get("apolo_11", "reports_folder_name"),
        )
        return reports_path_json

    @staticmethod
    def registry_missions_file_path() -> str:
        colonymoon_path_json = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "routes_folder_name"),
            config.get("apolo_11", "missions_folder_name"),
            config.get("apolo_11", "registry_missions_unknown"),
        )
        return colonymoon_path_json
