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
    response = supabase.table('directorio').select('*').limit(100).execute()
    rows = response.data
    return render_template('index.html', rows=rows)


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
    app.run(debug=True)


'''
import mysql.connector
cnx = mysql.connector.connect(user='dbUser', password='dbUserPass',
                              host='localhost',
                              database='sistemasOperativos')

def mostrarTabla():
    result = cursor.execute("SELECT * FROM directorio LIMIT 100")
    rows = cursor.fetchall()
    for rows in rows:
        print(rows)

programa = True

print(cnx)

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:

        while (programa):
            print(""" 
                1. Crear datos en la tabla (INSERT)
                2. Leer datos de la tabla (SELECT)
                3. Actualizar datos de la tabla (UPDATE)
                4. Eliminar datos de la tabla (DELETE)
                5. Salir
            """)
            menu = input("¿Qué opción desea?: ")

            opcion = True

            match (menu):
                case "1":
                    while opcion:
                        nombre = input("Nombre: ")
                        telefono = input("Telefono: ")
                        correo = input("Correo: ")

                        cursor.execute(
                            f"INSERT INTO directorio(nombre, celular, correo) VALUES ('{nombre}','{telefono}','{correo}')")
                        cnx.commit()

                        mostrarTabla()

                        ciclo = True
                        while ciclo:
                            respuesta = input("\n¿Desea ingresar otro registro? (y/n)?: ")
                            respuesta = respuesta.upper()

                            if respuesta == "Y":
                                opcion = True
                                ciclo = False
                            elif respuesta == "N":
                                opcion = False
                                ciclo = False
                            else:
                                print("Selecciona una opción válida")
                                ciclo = True

                case "2":
                    mostrarTabla()

                case "3":
                    while opcion:
                        mostrarTabla()

                        idUsuario = int(input("\nSelecciona el id del usuario que se desea modificar: "))

                        nombreNuevo = input("Nombre nuevo: ")
                        telefonoNuevo = input("Telefono nuevo: ")
                        correoNuevo = input("Correo nuevo: ")

                        cursor.execute(
                            f"UPDATE directorio SET nombre='{nombreNuevo}',celular='{telefonoNuevo}',correo='{correoNuevo}' WHERE id = {idUsuario}")
                        cnx.commit()

                        mostrarTabla()

                        ciclo = True
                        while ciclo:
                            respuesta = input("\n¿Desea actualizar otro registro? (y/n)?: ")
                            respuesta = respuesta.upper()

                            if respuesta == "Y":
                                opcion = True
                                ciclo = False
                            elif respuesta == "N":
                                opcion = False
                                ciclo = False
                            else:
                                print("Selecciona una opción válida")
                                ciclo = True

                case "4":
                    while opcion:

                        mostrarTabla()

                        idUsuarioElim = int(input("\nSelecciona el id del usuario que se desea eliminar: "))

                        cursor.execute(f"DELETE FROM directorio WHERE id = {idUsuarioElim}")
                        cnx.commit()

                        mostrarTabla()

                        ciclo = True
                        while ciclo:
                            respuesta = input("\n¿Desea eliminar otro registro? (y/n)?: ")
                            respuesta = respuesta.upper()

                            if respuesta == "Y":
                                opcion = True
                                ciclo = False
                            elif respuesta == "N":
                                opcion = False
                                ciclo = False
                            else:
                                print("Selecciona una opción válida")
                                ciclo = True

                case "5":
                    programa = False
                case _:
                    print("Selecciona una opción válida")

    cnx.close()

else:
    print("Could not connect")

    '''