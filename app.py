from flask import Flask,render_template
app=Flask(__name__)
@app.route("/home")
def home():
    return render_template("home.html",name="asad")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/employeePage")
def employeePage():
    return render_template("employeePage.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
    
    
if __name__=='__main__':
    app.run(debug=True)