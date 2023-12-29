class DeviceMission:
    def __init__(self):
        self.device_list = {}

        # If type and id are provided, return specific device
        if type is not None and id is not None:
            return self.device_list.get((type, id))

        # If type is provided, return devices of that type
        if type is not None:
            return {k: v for k, v in self.device_list.items() if k[0] == type}

        # If id is provided, return devices with that id
        if id is not None:
            return {k: v for k, v in self.device_list.items() if k[1] == id}

        # If neither type nor id is provided, return the entire device list
        return self.device_list

    def addDevice(self, type, id):
        if (type, id) not in self.device_list:
            self.device_list[(type, id)] = f"{type} {id} added successfully."
        else:
            return f"Device {type} {id} already exists."

    def removeDevice(self, type, id):
        device_key = (type, id)
        if device_key in self.device_list:
            del self.device_list[device_key]
            return f"Device {type} {id} removed successfully."
        else:
            return f"Device {type} {id} not found."