import os
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")


class DevicesPath:
    # @staticmethod
    def devices_path(self) -> str:
        full_path = os.path.join(
            config.get("apolo_11", "apolo_11_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
            config.get("apolo_11", "scr_folder_name"),
        )
        print(full_path)
        return full_path


DevicesPath.devices_path
