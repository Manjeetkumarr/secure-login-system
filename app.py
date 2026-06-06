from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt
import re

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql+pymysql://flaskuser:903612949072000@localhost/secure_login'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'super_secret_key_123'

db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class LoginHistory(db.Model):

    __tablename__ = "login_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100)
    )

    ip_address = db.Column(
        db.String(100)
    )

    login_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    return True


@app.route('/')
def home():
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username'].strip()

        email = request.form['email'].strip()

        password = request.form['password']

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:

            flash(
                "Username already exists",
                "danger"
            )

            return redirect('/register')

        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:

            flash(
                "Email already registered",
                "danger"
            )

            return redirect('/register')

        if not validate_password(password):

            flash(
                "Password must contain uppercase, lowercase and number",
                "danger"
            )

            return redirect('/register')

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        new_user = User(
            username=username,
            email=email,
            password=hashed_password.decode('utf-8')
        )

        db.session.add(new_user)

        db.session.commit()

        flash(
            "Account created successfully",
            "success"
        )

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        user = User.query.filter_by(
            username=username
        ).first()

        if not user:

            flash(
                "User does not exist",
                "danger"
            )

            return redirect('/login')

        if not bcrypt.checkpw(
            password.encode('utf-8'),
            user.password.encode('utf-8')
        ):

            flash(
                "Wrong password",
                "danger"
            )

            return redirect('/login')

        session['user'] = user.username

        history = LoginHistory(
            username=username,
            ip_address=request.remote_addr
        )

        db.session.add(history)

        db.session.commit()

        flash(
            "Login Successful",
            "success"
        )

        return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():

    if 'user' not in session:

        return redirect('/login')

    return render_template(
        'dashboard.html',
        username=session['user']
    )


@app.route('/logout')
def logout():

    session.pop(
        'user',
        None
    )

    flash(
        "Logged out successfully",
        "success"
    )

    return redirect('/login')


with app.app_context():

    db.create_all()


if __name__ == '__main__':

    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
