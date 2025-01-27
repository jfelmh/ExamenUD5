# Importando Blueprint desde Flask
from flask import Blueprint

# Creando la instancia del Blueprint
bp = Blueprint('todo', __name__, url_prefix='/todo')

# Definiendo rutas y funciones dentro del Blueprint
@bp.route('/list')
def index():
    return "Lista de tareas"

@bp.route('/create')
def create():
    return "Crear una tarea"

