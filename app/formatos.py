# Formatos estandarizados para el SGC
# Ejemplo: Lista de chequeo de pruebas, registro de incidencias, plantilla de auditoría

from app import db
from datetime import datetime

class FormatoSGC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)  # Ej: Chequeo, Incidencia, Auditoría, Acta
    nombre = db.Column(db.String(200), nullable=False)
    datos = db.Column(db.Text, nullable=True)  # JSON o texto con los datos del formato
    fecha = db.Column(db.Date, default=datetime.utcnow)
    responsable = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<FormatoSGC {self.nombre} ({self.tipo})>"
