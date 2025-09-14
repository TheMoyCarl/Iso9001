from app import create_app, db
from app.models import Usuario, Proyecto, Auditoria, NoConformidad, AccionCorrectiva, Riesgo, Actividad

app = create_app()

# Crear todas las tablas
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)