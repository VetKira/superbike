from flask import Flask, request, render_template,session,redirect, url_for
import mlab
from models.superbike import Bike

app = Flask(__name__)
mlab.connect()

@app.route("/")
def homepage():
  return render_template("homepage.html")

# @app.route("/<brand>")
# def intro(brand):
#   return render_template("intro.html", hangxe=brand )

@app.route("/<brand>")
def phankhuc(brand):
  bikes = Bike.objects(hangxe=brand)
  return render_template("phankhuc.html",hangxe=brand, bikes = bikes)

@app.route("/<brand>/<name>")
def thongso(brand,name):
  info = Bike.objects(bikename=name)
  return render_template("thongso.html", hangxe = brand, dongxe = name, info = info)
  
if __name__ == '__main__':
  app.run(debug=True)