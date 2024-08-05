from flask import Flask      # 플라스크 모듈 호출
from flask import request
from flask.templating import render_template

app = Flask(__name__)          # 플라스크 앱 생성

@app.route('/')                 # 기본('/') 웹주소로 요청이 오면 
def hello():                  # hello 함수 실행
    return 'Hello world~' 

@app.route('/param')              
def param():                 
    pram = request.args.get("menu", "탕수육")
    return 'param : ' + pram

@app.route('/post', methods=['POST', 'GET'])                 
def post():                  
    pram = request.form["menu"]
    return 'post' + pram

@app.route('/forw')                
def forw(): 
    a = "홍길동"                
    b = ["전우치", "장화홍련"]
    return render_template('forw.html', a=a, b=b)

@app.route('/emp')                 # 기본('/') 웹주소로 요청이 오면 
def emp():
    mylist = [
            {'e_id':'1', 'e_name':'가','addr':'대전', 'gen':'남'},
            {'e_id':'2', 'e_name':'나','addr':'부산', 'gen':'여'},
            {'e_id':'3', 'e_name':'다','addr':'광주', 'gen':'남'}
        ]
                          # hello 함수 실행
    return render_template('emp.html', mylist=mylist)
   
if __name__ == '__main__':     
    app.run(debug=True, port=80, host='0.0.0.0')
