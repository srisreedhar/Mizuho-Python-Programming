from flask import Flask


app = Flask(__name__)

# View Function
# AboutUS page
@app.route('/aboutus')
def aboutus():
    return '<h1>This is About US</h1>'

# home Page
@app.route('/')
def homePage():
	return """ <!DOCTYPE html>
<html>
<style>
body {
  background-image: url('https://images-na.ssl-images-amazon.com/images/I/513MX-WVPGL._SL1000_.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
}
</style>
<body>

<h2>Welcome </h2>

<p>i do not want any text here</p>

</body>
</html>
 """


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




