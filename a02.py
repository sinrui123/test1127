from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/abc')
def abc():
    return 'abcc'

if __name__ =="__main__":
    app.run()