from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

    @app.route('/bang123')
def bang():
    return 'bang123'

if __name__ =="__main__":
    app.run()