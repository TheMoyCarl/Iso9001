from flask import Blueprint, render_template
from app.models import Proyecto, Auditoria, NoConformidad, Riesgo, Actividad
from app import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("dashboard.html")

@main.route("/dashboard")
def dashboard():
    cumplimiento = 82  # Simulación, luego se calcula con datos
    auditorias = Auditoria.query.count()
    no_conformidades = NoConformidad.query.count()
    satisfaccion = 4.3  # Ejemplo, luego se calcula de encuestas
    
    return render_template("dashboard.html",
                           cumplimiento=cumplimiento,
                           auditorias=auditorias,
                           no_conformidades=no_conformidades,
                           satisfaccion=satisfaccion)

@main.route("/auditorias")
def auditorias():
    lista = Auditoria.query.all()
    return render_template("auditorias.html", auditorias=lista)

@main.route("/riesgos")
def riesgos():
    lista = Riesgo.query.all()
    return render_template("riesgos.html", riesgos=lista)

@main.route("/actividades")
def actividades():
    lista = Actividad.query.all()
    return render_template("actividades.html", actividades=lista)
