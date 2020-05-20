#### The indentation error has been fixed.


## Assigning multiple URLS to a single webpage 

@app.route('/index')
@app.route('/home')
@app.route('/')
def aboutus():
    return '<h1>This is About US</h1>'




# Working with Templates


Folder Structure :


Base Project Folder
	- FlaskApp.py
	- templates
		- html pages
		- home.html
		- contactus.html


Create a HTML page/template

place the file in templates folder

import render_template into the app from flask

in the view function, use render_template to return the html page 
from the tempaltes folder.




# # Jinja templating system

{ % code/template tags %}

{{ variables }}
