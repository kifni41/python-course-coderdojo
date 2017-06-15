from flask import Flask, render_template
from geometry.triangle import Triangle
from geometry.square import Square
from geometry.circle import Circle

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/geometry')
def route_geometry():
    return render_template('geometry.html')


@app.route('/triangle')
def route_triangle():
    t1 = Triangle(30, 44)
    return render_template('triangle.html', area=t1.calc_area())


@app.route('/square')
def route_square():
    t1 = Square(30)
    return render_template('square.html', area=t1.calc_area())

@app.route('/circle')
def route_circle():
    t1 = Circle(30)
    return render_template('circle.html', area=t1.calc_area())

app.run(debug=True, host='0.0.0.0', port=8888)
