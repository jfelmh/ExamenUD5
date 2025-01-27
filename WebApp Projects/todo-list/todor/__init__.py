# Importando la clase Flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Creando extensión de la base de datos
db = SQLAlchemy()

# Creando función de control
def create_app():
    # Creando la variable de iniciación
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev_esit',  # Coma añadida aquí
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"  # Clave correcta: SQLALCHEMY_DATABASE_URI
    )

    # Iniciando conexión
    db.init_app(app)

    # Registrando Blueprint
    from . import todo  # Asegúrate de que todo.py esté en el mismo paquete
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    # Definiendo rutas
    @app.route('/')
    def index():
        return render_template('index.html')

    # Creación de tablas a partir de los modelos
    with app.app_context():
        db.create_all()  # Creando las tablas en la base de datos

    return app

# Ejecutando la aplicación
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


