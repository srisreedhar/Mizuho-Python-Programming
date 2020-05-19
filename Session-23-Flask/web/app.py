from flask import Flask


app = Flask(__name__)

# View Function
# AboutUS page
@app.route('/aboutus')
def aboutus():
    return 'This is About US'

# home Page
@app.route('/')
def homePage():
	return "This is a Home Page"


# courses offered
@app.route('/courses')
def coursePage():
	return " This is course Page"

# contact us
@app.route('/contact')
def contactUS():
	return " Contact US Page"



if __name__ == '__main__':
	app.run(debug=True)   




