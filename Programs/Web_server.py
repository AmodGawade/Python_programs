#!/Users/amod/venv/bin/python
# name : Amod
from flask import Flask

app = Flask(__name__)

@app.route('/')
def func_():
    a = '''<html> <body><h1> Amod Gawade Website</h1> <br> <h3> Python Programs are listed below </h3></body></html>'''
    return a

@app.route('/list/')
def func2():
    return "nice"

# boiler plate
if __name__ == "__main__":
    app.run()
