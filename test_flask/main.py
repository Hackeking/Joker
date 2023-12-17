from flask import Flask,redirect,url_for,render_template,request
from mysql import mysql,register
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
        result = mysql(request.form['user_name'],request.form['pwd'])
        if result :
            return render_template('home.html',rel=f'welcome {request.form["user_name"]}!!')
        else:
            return render_template('index.html')

@app.route('/register',methods=['POST','GET'])
def register_redirect():
        return render_template('register.html')

@app.route('/register_Done',methods=['POST','GET'])
def register_page():
        result = register(request.form['user_name'],request.form['pwd'],request.form['email'])
        if result :
            return render_template('index.html')
        else:
            return render_template('register.html')
        
if __name__ == "__main__":
      app.run(debug=True)