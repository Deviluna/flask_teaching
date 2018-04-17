"""
Introduction:
a web includes service logic and presentation logic.
for rendering templates,we use Jinja2
"""
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')#the default path of templates is "./templates",index.html is just a static page.

@app.route("/stock/<id>")
def stock(id):
    return render_template('stock.html',id=id)    #more tricks in stock.html



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)

"""
Do you like ♂ what you see?
this programme is much shorter than that in chapter.2,templates did it.
"""