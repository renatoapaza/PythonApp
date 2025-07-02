# Importa la clase Flask y la función render_template desde el módulo flask.
from flask import Flask, render_template

# Crea una instancia de la clase Flask y asigna la aplicación actual a la variable 'app'.
app = Flask(__name__)

# Define una ruta para la raíz del sitio web ('/').
@app.route('/')
def home():
    """
    Render the home template.
    
    This route renders a template named 'home.html' and passes the 'posts' list to it.
    """
    # Devuelve el resultado de renderizar el template 'home.html'.
    return render_template('home.html')

# Define una ruta para '/ping'.
@app.route('/ping')
def ping():
    """
    Respond with a 'pong' string.
    """
    # Devuelve la cadena "pong" como respuesta a la ruta '/ping'.
    return "pong modified"

# Verifica si el archivo actual está siendo ejecutado como el programa principal.
if __name__ == '__main__':
    # Si se está ejecutando como el programa principal, inicia la aplicación en el puerto 5000.
    app.run(port=5000)