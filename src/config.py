import configparser

config = configparser.ConfigParser()
config.read("settings.cfg")

DATA_DIR = config.get("path", "/data_dir")
DATA_INTERNAL = config.get("path", "data/data_internal")
DATA_EXTERNAL = config.get("path", "data/data_external")
LOGGING = config.get("path", "/logging")
DEBUG = config.getboolean("path", "debug")


