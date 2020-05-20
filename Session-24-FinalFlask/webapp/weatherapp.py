from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("weatherdetail.html",name="sreedhar")

@app.route('/details')
def detailed_page():
	url="http://api.openweathermap.org/data/2.5/forecast/daily?q=hyderabad,in&cnt=10&mode=json&units=metric&APPID=2d80cf7142a085e6c34f383205d35118"
	#d=requests.get(url).json()
	d=requests.get(url).text
	data=json.loads(d)
	mn=data.get('list')[0].get('temp').get('min')
	mx=data.get('list')[0].get('temp').get('max')
	return render_template("weatherdetail.html",maximun=mx)



if __name__ == '__main__':
	app.run(debug=True)   




