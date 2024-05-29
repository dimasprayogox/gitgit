from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = [
        {
            'Nama' : 'Dimas',
            'email' : 'dimas@ahai.com',
            'alamat' : 'wakanda'
            },
        {
            'Nama' : 'Prayogo',
            'email' : 'pryege@ahai.com',
            'alamat' : 'wakandi'
            },
        {
            'Nama' : 'meh',
            'email' : 'moh@ahai.com',
            'alamat' : 'wau'
        }
    ]
    return render_template('user.html', users = data)

if __name__ == '__main__':
    app.run(debug = True)