from flask import Flask, request, redirect, jsonify     
from flask.templating import render_template

app = Flask(__name__)          

@app.route('/')                 
def hello():                  
    return 'Hello Docker'


if __name__ == '__main__':     
    app.run(debug=True, port=80, host='0.0.0.0')
