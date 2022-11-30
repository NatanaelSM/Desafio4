from app import app, render_template
from flask import request
from flask_mysqldb import MySQL
from flask import Flask

app.config['MYSQL_Host'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'natanael'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route("/")
@app.route("/home")
def home ():
    return render_template("index.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")
    

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        descricao = request.form.get('descrição')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos (email, nome, assunto) VALUES (%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucess'

    return render_template("contato.html")

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)


if __name__=='__main__':
    app.run(debug=True)
