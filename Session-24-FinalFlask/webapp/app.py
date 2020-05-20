from flask import Flask, render_template


app = Flask(__name__)

# View Function
# AboutUS page
@app.route('/aboutus')
def aboutus():
    return '<h1>This is About US</h1>'

# home Page
@app.route('/sun')
def sun():
	return render_template("home.html")

# courses offered
@app.route('/courses')
def coursePage():
	return " <h1>This is course Page</h1>"

# contact us
@app.route('/contact')
def contactUS():
	return " <h1>Contact US Page</h1>"



if __name__ == '__main__':
	app.run(debug=True)   




