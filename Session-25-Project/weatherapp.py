from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("weatherdetail.html",name="sreedhar")

@app.route('/details')
def detailed_page():
	url="http://api.openweathermap.org/data/2.5/forecast/daily?q=hyderabad,in&cnt=10&mode=json&units=metric&APPID=APIKEY"
	#d=requests.get(url).json3()
	d=requests.get(url).text
	data=json.loads(d)
	mn=data.get('list')[0].get('temp').get('min')
	mx=data.get('list')[0].get('temp').get('max')
	des=data.get('list')[0].get('weather')[0].get('description',"Not Available")
	return render_template("weatherdetail.html",maximun=mx,minimum=mn,description=des)

@app.route('/fulldetails/<placename>')
def fulldetailed_page(placename):
	url="http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=10&mode=json&units=metric&APPID=APIKEY"%(placename)
	resp=requests.get(url).text
	data=json.loads(resp)
	table=""
	for eachDay in data.get('list'):
		table=table+"""<tr><td> %s </td><td> %s </td><td> %s </td></tr>"""%(eachDay.get('temp').get('max'),eachDay.get('temp').get('min'),eachDay.get('weather')[0].get('description',"Not Available"))
	return render_template("fullweatherdetails.html",tabledata=table,PlaceName=placename)




# ,eachDay.get('weather')[0].get('description',"Not Available")


if __name__ == '__main__':
	app.run(debug=True)   




