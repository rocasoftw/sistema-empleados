from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__) # Instancio Flask
mysql=MySQL()       # Instancio MySQL

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='empleados'

mysql.init_app(app)

@app.route('/')
def index():
    sql="INSERT INTO empleados (id, nombre, correo, foto) VALUES (NULL, 'Pepe', 'pepe@email.com', 'fotodepepe.jpg');"

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)

    conn.commit()   # Le digo que ejecute la peticion

    return render_template('empleados/index.html')
    

if __name__== '__main__':   # Si es la rama principal ejecuto app
    app.run(debug=True)     # pongo debug para que muestre errores por consola