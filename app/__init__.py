from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )
    app.config.from_object("config.Config")

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Importar modelos para que SQLAlchemy los reconozca
    from app import models
    from app import documental, formatos, capacitacion, indicadores

    # Registrar rutas
    from app.routes import main
    app.register_blueprint(main)

    return app