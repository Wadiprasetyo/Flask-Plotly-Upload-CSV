from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import csv
import pandas as pd 
import numpy as np 
import plotly
import plotly.graph_objects as go 
import chart_studio.plotly as py 
import json

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        myFile = request.files['File']
        fn = secure_filename(myFile.filename)
    
        df = pd.read_csv(fn)
        x = np.array(list(df['x']))
        y = np.array(list(df['y']))
        plot = go.Scatter(x=x, y=y)

        plot = [plot]
        plotJSON = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('home1.html', x=plotJSON)

if __name__ == '__main__':
    app.run(debug=True)