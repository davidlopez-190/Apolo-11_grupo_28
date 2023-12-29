from datetime import datetime
import hashlib

class BaseMission:
    def __init__(self, date, idmission, missionname, missiontype, devicetype, devicestate):
        self.date = date
        self.idmission = idmission
        self.missionname = missionname
        self.missiontype = missiontype
        self.devicetype = devicetype
        self.devicestate = devicestate
        self.hash = self.generate_hash()
    
    def missionstart(self):
        print(f"Mission '{self.missionname}' started at {self.date}.")

    def finmission(self):
        print(f"Mission '{self.missionname}' finished at {datetime.now()}.")

    def missionduration(self):
        start_time = datetime.strptime(self.date, "%d%m%y%H%M%S")
        end_time = datetime.now()
        duration = end_time - start_time
        return duration

    def generate_hash(self):
        mission_info = f"{self.idmission}{self.missionname}{self.date}{self.missiontype}{self.devicetype}{self.devicestate}"
        return hashlib.sha256(mission_info.encode()).hexdigest()
