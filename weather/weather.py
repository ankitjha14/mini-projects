import requests
from time import time,localtime,strftime

APPID="398a56fc54b4f8630122d0812bdcb16a"

def getLocalTimeFromUnix(sec):
	lt=localtime(sec)
	res=strftime("%H:%M:%S",lt)
	return res
def getLocalDateFromUnix(sec):
	lt=localtime(sec)
	res=strftime("%a, %d %b %Y",lt)
	return res

def IpInfo():
	try:
		r=requests.get("http://ipinfo.io/geo")
		r.raise_for_status()
		try:
			data=r.json()
			return data
		except:
			pass
		
	except requests.exceptions.HTTPError as err:
		print (err)
		exit()

def weather(flag=0):
	url="http://api.openweathermap.org/data/2.5/weather?"
	ipinfo=IpInfo()
	ip=ipinfo['ip']
	if flag==0:
		coordinates=ipinfo['loc']
		lat,lon=coordinates.split(',')
		url+="lat=%s&lon=%s"%(lat,lon)
	else:
		query=input("Enter the city name: ")
		print()
		url+="q=%s"%(query)
	
	unit="metric"
	degree='\u00b0'
	url+="&units=%s&APPID=%s"%(unit,APPID)
	#print(url)
	try:
		r=requests.get(url)
		r.raise_for_status()
		try:
			data=r.json()
			city=data['name']+", "+data['sys']['country']

			todayDate=getLocalDateFromUnix(int(data['dt']))
			#print (data)
			print("Weather at %s is: "%(city))
			print("Today= %s"%(todayDate))
			

			print("Now= %s%sC" %(data['main']['temp'],degree))
			print("Description= %s"%(data['weather'][0]['description']))
			#print("Min. Temperature= %s%sC" %(data['main']['temp_min'],degree))
			#print("Max. Temperature= %s%sC" %(data['main']['temp_max'],degree))
			print("Humidity= %s%%"%(data['main']['humidity']))
			print("Wind Speed= %sm/s"%(data['wind']['speed']))
			#print("Sunrise= %s"%(time.gmtime(int(data['sys']['sunrise']))))
			sunrise=getLocalTimeFromUnix(int(data['sys']['sunrise']))
			print("Sunrise= %s"%(sunrise))
			sunset=getLocalTimeFromUnix(int(data['sys']['sunset']))
			print("Sunset= %s"%(sunset))
			
			print("\nYour IP is= %s"%(ip))
			print("Want to get weather of some other location? Y/N or y/n ")
			ch=input()
			if ch=="Y" or ch=="y":
				weather(1)
			else:
				exit()

		except:
			pass
	except requests.exceptions.HTTPError as err:
		print (err)
		exit()

	

weather()