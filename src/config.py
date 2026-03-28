import configparser

config = configparser.ConfigParser()
config.read("settings.cfg")

DATA_DIR = config.get("ROOT", "/data_dir")
DATA_INTERNAL = config.get("ROOT", "data/data_internal")
DATA_EXTERNAL = config.get("ROOT", "data/data_external")
LOGGING = config.get("ROOT", "/logging")
DEBUG = config.getboolean("ROOT", "debug")


