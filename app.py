import os

from flask import Flask, render_template, request
from mapgen import mapgen


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/",methods=('GET','POST'))
def index():
    if request.method == 'POST':
        
        m=mapgen(request.form)
        m.get_root().width = "800px"
        m.get_root().height = "600px"
        iframe = m.get_root()._repr_html_()


        return render_template('map.html',mapframe=m.get_root()._repr_html_())
    # m = mapgen()
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')