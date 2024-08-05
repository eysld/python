from flask import Flask,request,redirect,jsonify
from flask.templating import render_template

app = Flask(__name__) 

@app.route('/')   
def main(): 
    return 'Hello Docker' 

if __name__ == '__main__': 
    app.run(debug=True, port=5000, host='0.0.0.0')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    