from flask import Flask, render_template, url_for
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import json
from climate import get_figures


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    figures = get_figures()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", ids=ids, figuresJSON=figuresJSON)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()   