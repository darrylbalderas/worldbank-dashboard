from flask import Flask, render_template, url_for
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import json
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", graphJSON=graphJSON)

if __name__ == '__main__':
    app.run()   