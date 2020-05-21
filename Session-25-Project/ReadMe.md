Putting all together
- we need to generate a table that consists, min,max and description of
10days temparatures
- create the placeholder for table in frontend
- pass the table from the flask.app to frontend .

// Passing variables/arguments into urls

a URL takes an argument - url parameter
```
route/<parameter>
def viewFunction(parameter)
	use parameter

fulldetails/<placename>
def viewfunction(placename)	:
	use placeName


# default-arguments
def defaultArgs(principle,tenure,rate=8):
	
```

generate list of max & a list of min values
```
def sampleView():
	return render_template("templateName.html",mxl=max_list,mnl=min_list)
```

data: {{List_of_max_values}}
Chartjs Link
`https://www.chartjs.org/samples/latest/charts/bar/horizontal.html`
