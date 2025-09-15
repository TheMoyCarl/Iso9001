from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Proyecto, Auditoria, NoConformidad, Riesgo, Actividad, Empresa
from app.documental import DocumentoSGC
from app.formatos import FormatoSGC
from app.capacitacion import TallerCapacitacion
from app.indicadores import IndicadorDesempeno
from app import db
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/")
def home():
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

@main.route("/auditorias/nueva", methods=["GET", "POST"])
def nueva_auditoria():
    if request.method == "POST":
        # Asignar automáticamente un ID de proyecto (por ejemplo, el primero disponible)
        proyecto = Proyecto.query.first()
        if not proyecto:
            return "No hay proyectos disponibles para asignar.", 400

        auditor = request.form.get("auditor")
        fecha_str = request.form.get("fecha")
        resultado = request.form.get("resultado")
        observaciones = request.form.get("observaciones")

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            return "Formato de fecha inválido.", 400

        nueva_auditoria = Auditoria(
            proyecto_id=proyecto.id,  # ID del proyecto asignado automáticamente
            auditor=auditor,
            fecha=fecha,
            resultado=resultado,
            observaciones=observaciones
        )

        db.session.add(nueva_auditoria)
        db.session.commit()

        # Devolver la fila HTML para la tabla
        return render_template("_auditoria_row.html", auditoria=nueva_auditoria)

    proyectos = Proyecto.query.all()
    return render_template("nueva_auditoria.html", proyectos=proyectos)

@main.route("/riesgos")
def riesgos():
    lista = Riesgo.query.all()
    return render_template("riesgos.html", riesgos=lista)

@main.route("/riesgos/nuevo", methods=["GET", "POST"])
def nuevo_riesgo():
    if request.method == "POST":
        # Validar datos recibidos
        riesgo = request.form.get("riesgo")
        probabilidad = request.form.get("probabilidad")
        impacto = request.form.get("impacto")
        plan = request.form.get("plan")

        if not riesgo or not probabilidad or not impacto or not plan:
            flash("Todos los campos son obligatorios.", "danger")
            return redirect(url_for("main.riesgos"))

        try:
            nuevo_riesgo = Riesgo(
                riesgo=riesgo,
                probabilidad=probabilidad,
                impacto=impacto,
                plan=plan
            )

            db.session.add(nuevo_riesgo)
            db.session.commit()

            flash("Riesgo creado exitosamente.", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al guardar el riesgo: {str(e)}", "danger")

        return redirect(url_for("main.riesgos"))

    return render_template("nuevo_riesgo.html")

@main.route("/actividades")
def actividades():
    lista = Actividad.query.all()
    return render_template("actividades.html", actividades=lista)

@main.route("/actividades/nueva", methods=["GET", "POST"])
def nueva_actividad():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        estado = request.form.get("estado")

        nueva_actividad = Actividad(
            nombre=nombre,
            estado=estado
        )

        db.session.add(nueva_actividad)
        db.session.commit()

        flash("Actividad creada exitosamente.", "success")
        return redirect(url_for("main.actividades"))

    return render_template("nueva_actividad.html")

@main.route("/documental")
def documental():
    documentos = DocumentoSGC.query.all()
    return render_template("documentos.html", documentos=documentos)

@main.route("/formatos")
def formatos():
    formatos = FormatoSGC.query.all()
    return render_template("formatos.html", formatos=formatos)

@main.route("/capacitacion/talleres")
def talleres():
    talleres = TallerCapacitacion.query.all()
    return render_template("capacitacion.html", talleres=talleres)

@main.route("/indicadores/desempeno")
def indicadores_desempeno():
    indicadores = IndicadorDesempeno.query.all()
    return render_template("indicadores.html", indicadores=indicadores)

@main.route("/clientes")
def clientes():
    return render_template("clientes.html")

@main.route("/configuracion")
def configuracion():
    return render_template("configuracion.html")

@main.route("/registro_iso")
def registro_iso():
    return render_template("registro_iso.html")

@main.route("/capacitacion")
def capacitacion():
    return render_template("capacitacion.html")

@main.route("/guardar_registro", methods=["POST"])
def guardar_registro():
    razon_social = request.form.get("razon_social")
    nit = request.form.get("nit")
    representante = request.form.get("representante")
    sector = request.form.get("sector")
    tipo_empresa = request.form.get("tipo_empresa")
    direccion = request.form.get("direccion")
    telefono = request.form.get("telefono")
    empleados = request.form.get("empleados")
    email = request.form.get("email")
    web = request.form.get("web")

    nueva_empresa = Empresa(
        razon_social=razon_social,
        nit=nit,
        representante=representante,
        sector=sector,
        tipo_empresa=tipo_empresa,
        direccion=direccion,
        telefono=telefono,
        empleados=empleados,
        email=email,
        web=web
    )

    db.session.add(nueva_empresa)
    db.session.commit()

    flash("Registro guardado exitosamente.", "success")
    return redirect(url_for("main.index"))

@main.route("/gestion")
def gestion():
    return render_template("gestion.html")
