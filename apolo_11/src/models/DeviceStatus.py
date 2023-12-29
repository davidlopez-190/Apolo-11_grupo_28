class DeviceStatus:
    def __init__(self):
        self.status_list = ["Excellent", "Good", "Warning", "Faulty", "Killed", "Unknown"]

    def getStatusList(self):
        return self.status_list