from configparser import ConfigParser


config = ConfigParser()
config.read('./config.ini')
class ReadConfig:   

    @staticmethod
    def cycle_frequency_time():
        periodicity = int(config.get('apolo_11', 'cycle_frequency_time'))
        return periodicity