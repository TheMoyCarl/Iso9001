# Módulo para indicadores de desempeño y seguimiento ISO 9001
from app import db
from datetime import datetime

class IndicadorDesempeno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    unidad = db.Column(db.String(50), nullable=True)
    fecha = db.Column(db.Date, default=datetime.utcnow)
    responsable = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<IndicadorDesempeno {self.nombre}: {self.valor}{self.unidad}>"
