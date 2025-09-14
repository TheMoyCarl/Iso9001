import os

class Config:
    # Base de datos SQLite (para pruebas)
    SQLALCHEMY_DATABASE_URI = "sqlite:///iso9001.db"

    # Si quiere usar MySQL, cambie la URI:
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:contraseña@localhost/iso9001"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Para sesiones y seguridad