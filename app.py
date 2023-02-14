from dash import Dash, dcc, html, Input, Output
import os
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

#machinedata = pd.read_csv('out.csv')

#drawing visual #1
#fig = px.line(machinedata, x = "Timestamp", y=  "Coolant")

app.layout = html.Div([
    html.H2('Development Dashboard'),
    #dcc.Graph(
        #figure = fig,
        #id = 'devgraph'
   # ),
    html.Div(id='display-value')
])


if __name__ == '__main__':
    app.run_server(debug=True)
