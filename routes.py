from app import app, render_template

@app.route("/")
@app.route("/home")
def home ():
    return render_template("home.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")
    

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descrição = request.form['descrição']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO formulario (email, assunto, descrição VALUES (%s, %s, %s)'), (email, assunto, descrição) 

        mysql. connection.commit()

        cur.close()

        return 'sucess'

    return render_template("contato.html")

if __name__=='__main__':
    app.run(debug=True)
