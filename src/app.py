from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__) # Instancio Flask
mysql=MySQL()       # Instancio MySQL

if __name__== '__main__':   # Si es la rama principal ejecuto app
    app.run(debug=True)     # pongo debug para que muestre errores por consola