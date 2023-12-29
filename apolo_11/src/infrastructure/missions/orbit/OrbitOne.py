from  apolo_11.src.models.BaseMission import BaseMission
from  apolo_11.src.models.DeviceMission import DeviceMission
from  apolo_11.src.models.DeviceStatus import DeviceStatus

class OrbitOne(BaseMission, DeviceMission, DeviceStatus):
    def __init__(self, date, idmission, missionname, missiontype, devicetype, devicestate):
        super().__init__(date, idmission, missionname, missiontype, devicetype, devicestate)
        