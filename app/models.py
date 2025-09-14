from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    responsable = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), nullable=False)

class Auditoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proyecto_id = db.Column(db.Integer, db.ForeignKey("proyecto.id"), nullable=False)
    auditor = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    resultado = db.Column(db.String(100), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)

class NoConformidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auditoria_id = db.Column(db.Integer, db.ForeignKey("auditoria.id"), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

class AccionCorrectiva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no_conformidad_id = db.Column(db.Integer, db.ForeignKey("no_conformidad.id"), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

class Riesgo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    riesgo = db.Column(db.String(200), nullable=False)
    probabilidad = db.Column(db.String(50), nullable=False)
    im
