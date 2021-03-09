from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template ("home.html")

@app.route("/market")
def hello():
    return render_template ("market.html")


if __name__==("__main__"):
   app.run(debug=True)