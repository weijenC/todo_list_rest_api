import configparser


config = configparser.ConfigParser()
config.read("/opt/config/cognixus_app.ini")

# Program
base_path = config["program"]["base_path"]
log_path = config["program"]["log_path"]

# Database
host_db = config["database"]["host"]
port_db = int(config["database"]["port"])
username_db = config["database"]["username"]
password_db = config["database"]["password"]
database_db = config["database"]["database"]
