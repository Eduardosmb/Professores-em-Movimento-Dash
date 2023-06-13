from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
df2 = pd.read_excel('violencia_por_ird_media.xlsx')
df = pd.read_excel('resultados_finais_idh_ird.xlsx')


# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['IRD', 'IDHM'],
                       value='IRD',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
       
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
])

@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.scatter(df, y='IRD', x=col_chosen)
    return fig

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)