from flask import Flask

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return "<h1> Selamat Datang {} </h1>".format(username)

if __name__=='__main__':
    app.run(debug=True)