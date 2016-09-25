import requests

def IpInfo():
	r=requests.get("http://ipinfo.io/geo")

	if r.status_code==200:
		data=r.json()
		print("IP : %s" % data['ip'])
		print("Coordinates : %s" % data['loc'])
		print("City : %s" % data['city'])
		print("Region : %s" % data['region'])
		print("Country : %s" % data['country'])
		print("Pin code : %s" % data['postal'])
	else:
		print("Try again later")


IpInfo()