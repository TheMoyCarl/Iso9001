# Módulo para estructura documental ISO 9001:2015
# Permite registrar y consultar documentos clave del SGC

from app import db
from datetime import datetime

class DocumentoSGC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)  # Ej: Política, Procedimiento, Acta, Registro
    nombre = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(300), nullable=True)  # Enlace a Google Drive, SharePoint, GitHub, etc.
    fecha = db.Column(db.Date, default=datetime.utcnow)
    version = db.Column(db.String(20), nullable=True)
    responsable = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<DocumentoSGC {self.nombre} ({self.tipo})>"
