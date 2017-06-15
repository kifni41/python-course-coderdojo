from flask import Flask
from flask import request
import json
import geometry.triangle as gtriangle
import geometry.square as gsquare
import geometry.circle as gcircle
import requests
import bs4

application = Flask(__name__)

@application.route('/')
def index() :
	return "Hello World!"

@application.route('/triangle')
def triangle() :
	# mengambil parameter dari HTTP GET
	bottom = request.args.get('bottom')
	height = request.args.get('height')

	# pesan error jika parameter tidak lengkap
	if(not bottom or not height) :
		return json.dumps({"error":"Please specify parameter : bottom & height"})

	# pesan error jika parameter tidak valid
	if(not isInt(bottom) or not isInt(height)) :
		return json.dumps({"error":"Parameter must be a number."})

	t1 = gtriangle.Triangle(int(bottom), int(height))
	# Membuat dictiionary untuk result
	obj = {"bottom":bottom,"height":height,"area":t1.calc_area()}
	return json.dumps(obj)

@application.route('/square')
def square() :
	# mengambil parameter dari HTTP GET
	side = request.args.get('side')

	# pesan error jika parameter tidak lengkap
	if(not side) :
		return json.dumps({"error":"Please specify parameter : side"})

	# pesan error jika parameter tidak valid
	if(not isInt(side)) :
		return json.dumps({"error":"Parameter must be a number."})

	s1 = gsquare.Square(int(side))
	obj = {"side":side, "area":s1.calc_area()}
	return json.dumps(obj)

@application.route('/circle')
def circle() :
	# mengambil parameter dari HTTP GET
	radius = request.args.get('radius')

	# pesan error jika parameter tidak lengkap
	if(not radius) :
		return json.dumps({"error":"Please specify parameter : radius"})

	# pesan error jika parameter tidak valid
	if(not isInt(radius)) :
		return json.dumps({"error":"Parameter must be a number."})


	c1 = gcircle.Circle(int(radius))
	area = c1.calc_area()
	obj = {"radius":radius, "area":area}
	return json.dumps(obj)

@application.route('/waktusholat')
def waktusholat() :
	url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=308'
	r = requests.get(url)

	if r.status_code == 200 :
		#print(r.text)
		data = bs4.BeautifulSoup(r.content,'lxml')
		#print(data)
		#find table_highlight class
		row = data.find_all('tr','table_highlight')
		#print(row)
		cols = row[0].find_all('td')
		jadwal = {'imsak':None,'subuh':None,'dzuhur':None,'ashar':None,'maghrib':None,'isya':None}
		for idx, val in enumerate(cols) :
			#print(idx)
			#print(val)
			if(idx == 1) :
				jadwal['imsak'] = val.get_text()
			elif(idx == 2) :
				jadwal['subuh'] = val.get_text()			
			elif(idx == 3) :
				jadwal['dzuhur'] = val.get_text()
			elif(idx == 4) :
				jadwal['ashar'] = val.get_text()			
			elif(idx == 5) :
				jadwal['maghrib'] = val.get_text()
			elif(idx == 6) :
				jadwal['isya'] = val.get_text()			
		return json.dumps(jadwal)
	else :
		return 'Unable to get data from website'

def isInt(val) :
	try:
		int(val)
		return True
	except ValueError :
		return False

if __name__ == '__main__':
        application.run(debug=True,host="0.0.0.0",port=8888)