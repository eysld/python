from flask import Flask, request, redirect, jsonify     
from flask.templating import render_template

app = Flask(__name__)          

@app.route('/')                 
def hello():                  
    return redirect("static/axios.html")

@app.route('/ajax', methods=['POST'])                 
def ajax():
    data = request.get_json()
    print(data['menu'])                  
    return jsonify(message = "ok")

@app.route('/axios', methods=['POST'])                 
def axios():
    data = request.get_json()
    print(data['menu'])             
    return jsonify(message = "ok")
   
if __name__ == '__main__':     
    app.run(debug=True, port=80, host='0.0.0.0')
