from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from config import config
import pypyodbc
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
                return redirect(url_for('ordencompra'))
            else:
                flash('Contraseña invalida...')
                return render_template('auth/login.html')
        else:
            flash('Usuario o contraseña Incorrecta')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/ordencompra')
@login_required
def ordencompra():
    return render_template('home.html')


@app.route('/inventario')
@login_required
def inventario():
    return render_template('inventory.html')

@app.route('/cliente')
@login_required
def cliente():
    return render_template('client.html')

@app.route('/realizar_compra')
@login_required
def realizar_compra():
    return render_template('doBuy.html')

@app.route('/realizar_venta')
@login_required
def realizar_venta():
    return render_template('doSell.html')

@app.route('/proveedor')
@login_required
def proveedor():
    return render_template('seller.html')

@app.route('/ordenes_compra')
@login_required
def ver_ord_comp():
    return render_template('BuyOrders.html')

@app.route('/ordenes_venta')
@login_required
def ver_ord_ven():
    return render_template('SellOrders.html')





@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return "<h1> ERROR 401 </h1> ", 401

def status_404(error):
    return "<h1> ERROR 404 </h1> ", 404




if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True, port=4000)

