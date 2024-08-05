from flask import Flask      
from flask import request, redirect
from flask.templating import render_template

app = Flask(__name__)          

@app.route('/')                 
def hello():                  
    return redirect("static/ex03.html")

   
if __name__ == '__main__':     
    app.run(debug=True, port=80, host='0.0.0.0')
