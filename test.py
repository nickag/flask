from flask import Flask,render_template,request,url_for,redirect,session
import os


app=Flask(__name__)
app.secret_key=os.urandom(24)


def valid(uname,passwd):
    if uname=="nitin" and passwd=='ag':
        return True
    else:
        return False

@app.route("/")
def hello_world():
	return "Hello!, world. Learning Flask!"


@app.route("/user/<user>")
def user(user):
    return "Hello %s" %user
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        if valid(request.form['username'],request.form['password']):
            session['username']=request.form['username']
            return redirect(url_for('hello',name=request.form['username']))

    return render_template("login.html")

@app.route("/hello/<name>")
def hello(name="user"):
    return render_template('hello.html',name=name)

if __name__=="__main__":
    app.run(debug=True)

