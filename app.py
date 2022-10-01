from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/grafik')
def grafik():
    return render_template("grafik.html")


@app.route('/ShablonList')
def ShablonList():
    return render_template("ShablonList.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/tabel')
def tabel():
    return render_template("tabel.html")


@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/sing-in')
def sing_in():
    return render_template("sing-in.html")


@app.route('/PodrazdelenieSotrEdit')
def PodrazdelenieSotrEdit():
    return render_template("PodrazdelenieSotrEdit.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + "-" + str(id)


if __name__ == '__main__':
    app.run(debug=True)
