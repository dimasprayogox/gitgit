from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Halaman Utama tod</h1>"

@app.route('/about')
def about():
    return "<h1>Halaman <div style='color:pink'>About</div></h1>"

@app.route('/contact')
def contact():
    return "<h1>Halaman <div style='color:red'>Contact </div></h1>"

if __name__ == '__main__':
    app.run(debug=True)