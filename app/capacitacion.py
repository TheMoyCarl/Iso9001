# Módulo para capacitación y gestión de talleres ISO 9001
from app import db
from datetime import datetime

class TallerCapacitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.Date, default=datetime.utcnow)
    modalidad = db.Column(db.String(50), nullable=True)  # Virtual/Presencial
    enlace = db.Column(db.String(300), nullable=True)  # Link a video, guía, etc.
    responsable = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<TallerCapacitacion {self.titulo}>"
