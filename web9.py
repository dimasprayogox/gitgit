from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data  = {
        'nama' : 'Dimas Prayogo',
        'usia' : 18
    }
    return render_template("bio.html",**data)

if __name__=='__main__':
    app.run(debug = True)