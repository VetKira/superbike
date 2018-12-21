from flask import Flask, request, render_template,session,redirect, url_for
import mlab

app = Flask(__name__)
mlab.connect()

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/introduction")
def introduction():
    return render_template("intro.html")

@app.route("/phankhuc")
def phankhuc():
  return render_template("phankhuc.html")
  
if __name__ == '__main__':
  app.run(debug=True)