# Importando la función create_app desde el paquete todor
from todor import create_app

# Validación y ejecución de la aplicación Flask
if __name__ == '__main__':
    # Crear la instancia de la aplicación
    app = create_app()

    # Ejecutar la aplicación
    app.run()


