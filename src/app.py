from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from config import config
import  pypyodbc
#models 
from models.ModelUser import ModelUser

#entities

from models.entities.User import User


app = Flask(__name__)

csrf = CSRFProtect(app)

db = pypyodbc.connect(config['development'].connection_string)
print(db)

app.config.from_object(config['development'])


login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)

        if logged_user is not None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Contraseña invalida...')
                return render_template('auth/login.html')
        else:
            flash('Usuario o contraseña Incorrecta')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/pedidos')
@login_required
def home():
    cur = db.cursor()
    cur.execute('SELECT * FROM Pedidos order by FechaEmision desc')
    data = cur.fetchall()
    cur.close()

    '''
    cur = db.cursor()
    cur.execute('SELECT * FROM Detalle_Pedido')
    data2 = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT * FROM Deuda')
    data3 = cur.fetchall()
    cur.close()

    '''
    
    return render_template('home.html', pedido =data,)

#ruta detalle pedido por id de pedido
@app.route('/pedido/<id>')
@login_required
def detallepedido(id):
    cur = db.cursor()
    cur.execute('SELECT * FROM Pedidos  order by FechaEmision desc')
    data2 = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT * FROM Detalle_pedido WHERE Pedido_Codigo = {0}'.format(id))
    data = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT * FROM Deuda WHERE Pedido_Codigo = {0}'.format(id))
    data3 = cur.fetchall()
    cur.close()


    return render_template('home.html', detalle =data,pedido=data2,deuda=data3,)

#actualizar estado de pedido a Aprobado
@app.route('/pedido/aprobar/<id>')
def aprobarpedido(id):
    cur = db.cursor()
    cur.execute("UPDATE Pedidos SET Estado = 'Aprobado' WHERE Codigo = {0}".format(id))
    db.commit()
    cur.close()
    return redirect(url_for('home'))

#actualizar estado de pedido a Rechazado, si esta rechazado enviar alerta
@app.route('/pedido/rechazar/<id>')
def rechazarpedido(id):
    
    cur = db.cursor()
    cur.execute("UPDATE Pedidos SET Estado = 'Rechazado' WHERE Codigo = {0}".format(id))
    db.commit()

    cur.close()
    return redirect(url_for('home'))



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return "<h1> Pagina no encontrada/autorizada </h1> ", 401

def status_404(error):
    return "<h1> Pagina no encontrada/autorizada </h1> ", 404


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        #si esta vacio el formulario retornar un mensaje
        if request.form['id'] == '':
            flash('Ingrese un codigo de pedido')
            return redirect(url_for('home'))
        else:
            ide = request.form['id']
            cur = db.cursor()
            cur.execute('SELECT * FROM Pedidos WHERE Codigo = {0}'.format(ide))
            data = cur.fetchall()
            cur.close()
            
            if data == []:
                flash('No se encontro el pedido')
                return redirect(url_for('home'))

            cur = db.cursor()
            cur.execute('SELECT * FROM Detalle_pedido WHERE Pedido_Codigo = {0}'.format(ide))
            data2 = cur.fetchall()
            cur.close()

            cur = db.cursor()
            cur.execute('SELECT * FROM Deuda WHERE Pedido_Codigo = {0}'.format(ide))
            data3 = cur.fetchall()
            cur.close()
            return render_template('home.html', pedido =data, detalle =data2,deuda=data3,)

    else:
        return render_template('home.html')





if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True, port=4000)

