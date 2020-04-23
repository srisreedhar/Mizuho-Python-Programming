# get user input & build url

placeName=input("Enter the place -> ")
url="http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=10&mode=json&units=metric&APPID=YOURAPIKEYHERE"%(placeName)
print("The URL built is \n",url)

