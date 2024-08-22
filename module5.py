from cgi import test
from pickle import NONE
from sre_parse import CATEGORIES
from pandas.tseries.offsets import Second
import prophet
from prophet.plot import plot_components_plotly, plot_plotly

import wget
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import plotly.express as px
import dash
from dash import Input, Output, dcc, html
import plotly.graph_objs as go
import numpy as np
import datetime


df=pd.read_csv('avocado-updated-2020.csv')
print(df.info())

print(df['type'].value_counts(dropna=False))
print(df['geography'].value_counts(dropna=False))

msk=df['geography']=='Los Angeles'
fig=px.line(df[msk],x='date',y='average_price',color='type')

fig.show()

avocado=pd.read_csv('avocado-updated-2020.csv')
app=dash.Dash()
app.layout=html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    dcc.Dropdown(id='geo-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in avocado['geography'].unique()],
                 value='New York'),
    dcc.Graph(id='price-graph')
    ])
@app.callback(
    Output(component_id='price-graph',component_property='figure'),
    Input(component_id='geo-dropdown',component_property='value')
    )
def updated_graph(selected_geography):
    filtered_avocado=avocado[avocado['geography']==selected_geography]
    line_fig=px.line(filtered_avocado,
                     x='date',y='average_price',
                     color='type',
                     title=f'avocado prices in {selected_geography}')
    return line_fig
if __name__=='__main__':
    app.run_server(debug=True)
    



