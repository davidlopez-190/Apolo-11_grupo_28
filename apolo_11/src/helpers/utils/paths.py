import json
import os
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")


class DevicesPath:
    @staticmethod
    def devices_path() -> str:
        full_path = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "devices_folder_name"),
        )
        print(full_path)
        print(os.path.sep)
        return full_path

    #  @staticmethod
    # def mission_list():
    #    mission_str = config.get("apolo_11", "missions")
    #   mission_list = [str(value.strip()) for value in mission_str.split(",")]
    #  print(mission_list)
    # return mission_list

    @staticmethod
    def mission_dict():
        mission_json = config.get("apolo_11", "missions")
        mission_dict = json.loads(mission_json)
        print(mission_dict)
        return mission_dict


devicespath = DevicesPath()
devicespath.devices_path()
devicespath.mission_dict()
