import os


class OsSystem:   
    
    @staticmethod
    def clear_console():
        clear = os.system('cls' if os.name == 'nt' else 'clear')
        return clear