from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/employee details/")
def Employee():
    return render_template('employeedetails.html')


if(__name__=='__main__'):
    app.run(debug=True)