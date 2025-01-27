# Importando Blueprint
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db

# Creando instancia del Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Creando ruta y función de registro
@bp.route('/register', methods=['GET', 'POST'])
def register():
    # Validación de datos
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si el nombre de usuario ya existe
        user_name = User.query.filter_by(username=username).first()
        if user_name:
            flash('El nombre de usuario ya está registrado', 'danger')
            return redirect(url_for('auth.register'))

        # Encriptando password
        hashed_password = generate_password_hash(password)

        # Crear un nuevo usuario
        user = User(username=username, password=hashed_password)
        
        # Agregar el nuevo usuario a la base de datos
        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        
        return redirect(url_for('auth.login'))

    # Si no se hace un POST, simplemente se renderiza el formulario sin errores
    return render_template('auth/register.html')

# Creando ruta y función de login
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Buscar al usuario en la base de datos
        user = User.query.filter_by(username=username).first()
        
        # Verificar si el usuario existe y si la contraseña es correcta
        if user and check_password_hash(user.password, password):
            flash('Inicio de sesión exitoso', 'success')
            # Aquí puedes agregar lógica para iniciar sesión (sesiones o cookies)
            return redirect(url_for('todo.index'))  # Redirigir a la página principal (o donde prefieras)
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')
