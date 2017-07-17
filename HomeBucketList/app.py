
from flask import Flask, request, render_template, sessions       #This code calls all our imports for the necessary modules

app = Flask(__name__)      #App initialization

app.config['SECRET_KEY'] = "Your_secret_string" #Secret key | Must be present to create user sessions


#The first page that starts once the user gets into the website
@app.route("/")
def index():
	return render_template('index.html')

#Registration page
@app.route("/register", methods=["POST", "GET"])
def register():
	return render_template('signup.html')

#Once Registered page then goes to the login page
@app.route("/validateLogin", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		name=request.form['Name']      #Session name created here
		email=request.form['inputEmail'] #Items being retrieved from input forms
		password=request.form['inputPassword']
		password2=request.form['confirmPassword']

		session['username'] = name

	return render_template('login.html', name=name)

#App run | Should not be deleted - Keeps the running of the website
if __name__ == "__main__":
    app.run(debug=True) #Debug is true to enable easy debugging - Can be delete that part