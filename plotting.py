import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('sample.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)


app.layout = html.Div([
    dcc.Graph(
        id='Previewing Fitting Curve',
        figure={
            'data': [
                go.Scatter(
                    x = df['time'],
                    y = df['count'],
                    mode = 'lines',
                    name = 'Fitting Curve'
                ) 
            ],
            'layout': go.Layout(
                xaxis={'title': 'Time'},
                yaxis={'title': 'Count'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)