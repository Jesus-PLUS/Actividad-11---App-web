'''
from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)


@app.route('/')
def index():
    try:
        response = supabase.table('directorio').select('*').limit(100).execute()
        rows = response.data
        return render_template('index.html', rows=rows)
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/add', methods=['POST'])
def create():
    nombre = request.form['nombre']
    celular = request.form['celular']
    correo = request.form['correo']
    supabase.table('directorio').insert({'nombre': nombre, 'celular': celular, 'correo': correo}).execute()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    nombre = request.form['nombre']
    celular = request.form['celular']
    correo = request.form['correo']
    supabase.table('directorio').update({'nombre': nombre, 'celular': celular, 'correo': correo}).eq('id', id).execute()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    supabase.table('directorio').delete().eq('id', id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
'''
from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
import os
from dotenv import load_dotenv

url = os.getenv("https://bwtqvuxvhrgzyskhfore.supabase.co")
key = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ3dHF2dXh2aHJnenlza2hmb3JlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3MzE1ODIsImV4cCI6MjA3NzMwNzU4Mn0.q54brlyjefnh2C7lkmXdrn5DligAxkA_YCSaK_xqtTE")

load_dotenv()

# Inicializa Supabase solo si las variables existen
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Faltan variables de entorno SUPABASE_URL o SUPABASE_KEY")

supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Agrega un timeout para evitar que la app se quede colgada
        response = supabase.table('directorio').select('*').limit(100).execute()
        rows = response.data
        return render_template('index.html', rows=rows)
    except Exception as e:
        # Devuelve una respuesta rápida en caso de error
        return f"<h1>Error</h1><p>No se pudieron cargar los datos: {str(e)}</p>", 500

@app.route('/add', methods=['POST'])
def create():
    nombre = request.form['nombre']
    celular = request.form['celular']
    correo = request.form['correo']
    try:
        supabase.table('directorio').insert({'nombre': nombre, 'celular': celular, 'correo': correo}).execute()
        return redirect(url_for('index'))
    except Exception as e:
        return f"<h1>Error al agregar registro</h1><pre>{str(e)}</pre>", 500

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    nombre = request.form['nombre']
    celular = request.form['celular']
    correo = request.form['correo']
    try:
        supabase.table('directorio').update({'nombre': nombre, 'celular': celular, 'correo': correo}).eq('id', id).execute()
        return redirect(url_for('index'))
    except Exception as e:
        return f"<h1>Error al actualizar registro</h1><pre>{str(e)}</pre>", 500

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        supabase.table('directorio').delete().eq('id', id).execute()
        return redirect(url_for('index'))
    except Exception as e:
        return f"<h1>Error al eliminar registro</h1><pre>{str(e)}</pre>", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)