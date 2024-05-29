from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    keywords = request.args.get('keywords')
    page = request.args.get('page')
    return "<h1>Hasil pencarian : {} di Page {}</h1>".format(keywords,page)

if __name__=='__main__':
    app.run(debug=True)