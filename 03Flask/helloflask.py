from flask import Flask
from flask import request
import json
import geometry.triangle as gtriangle
import geometry.square as gsquare
import geometry.circle as gcircle

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

def isInt(val) :
	try:
		int(val)
		return True
	except ValueError :
		return False

if __name__ == '__main__':
        application.run(debug=True,host="0.0.0.0",port=8888)