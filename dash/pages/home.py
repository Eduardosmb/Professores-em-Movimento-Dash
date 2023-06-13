from datetime import *
import pandas as pd
import numpy as np
import plotly.express as px
from dash import html, dcc, callback
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

url = 'https://drive.google.com/file/d/18xXO1Eu2SZkzqKyvSkgFDqhN4eSpBhSJ/view?usp=sharing'
file_id = url.split('/')[-2]
csv_url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(csv_url)


url2 = 'https://drive.google.com/file/d/1LAzu60pHepo3Wu8r1_HrfSlVOClM0lSh/view?usp=sharing'
file_id2 = url2.split('/')[-2]
csv_url2 = f'https://drive.google.com/uc?id={file_id2}'
df_rotatividade_por_rendimento = pd.read_csv(csv_url2)

url3 = 'https://drive.google.com/file/d/13Z8pKgkoJWBPf0vkAC2qRws7jYLEYGCy/view?usp=sharing'
file_id3 = url3.split('/')[-2]
csv_url3 = f'https://drive.google.com/uc?id={file_id3}'
df_dados_gerais = pd.read_csv(csv_url3)

dropdown_options = [
    {'label': 'IDHM', 'value': 'IDHM'},
    {'label': 'IRD', 'value': 'IRD'},
    {'label': 'Número de Matrículas na Educação Básica', 'value': 'QT_MAT_BAS'},
    {'label': 'Número de Matrículas na Educação Infantil', 'value': 'QT_MAT_INF'},
    {'label': 'Número de Matrículas na Educação Especial', 'value': 'QT_MAT_ESP'},
    {'label': 'Número de Matrículas no Ensino Fundamental', 'value': 'QT_MAT_FUND'},
    {'label': 'Número de Matrículas no Ensino Médio', 'value': 'QT_MAT_MED'},
    {'label': 'Número de Docentes da Educação Básica', 'value': 'QT_DOC_BAS'},
    {'label': 'Número de Docentes da Educação Infantil', 'value': 'QT_DOC_INF'},
    {'label': 'Número de Docentes da Educação Especial', 'value': 'QT_DOC_ESP'},
    {'label': 'Número de Docentes do Ensino Fundamental', 'value': 'QT_DOC_FUND'},
    {'label': 'Número de Docentes do Ensino Médio', 'value': 'QT_DOC_MED'},
    {'label': 'Estrutura', 'value': 'ESTRUTURA'},
]

def idh_por_bairro():
    df10 = df.sort_values(by='IDHM', ascending=False).round(2)
    fig = px.bar(df10, x='DISTRITO', y='IDHM', labels={'DISTRITO':'DISTRITO'})
    fig.update_traces(marker_color='rgb(67,244,122)')
    return fig

def scatter_drop(data1='IRD', data2='IDHM'):
    df = df_dados_gerais
    df = df.sort_values(by=data2, ascending=False).round(2)
    fig = px.scatter(df, x=data1, y=data2)
    fig.update_traces(marker_color='rgb(67,244,122)')
    return fig

def rotatividade_por_rendimento():
    fig = px.bar(df_rotatividade_por_rendimento, x='rendimento', y='IDHM', labels={'IDHM':'Média de IDHM', 'rendimento':'Índice de regularidade do Docente'})
    fig.update_traces(marker_color='rgb(67,244,122)')
    return fig

dash.register_page(__name__, path='/home')

layout = html.Div([
    html.Section([
        html.Header([
            html.Img(src="/assets/logo.png", className="logo"),
            html.Div([
                dcc.Link(' Home', href='/', className="fa-solid fa-house"),
                dcc.Link(' Bibliografia', href='/links', className="fa-solid fa-magnifying-glass"),
                dcc.Dropdown(
                    id='demo-dropdown',
                    placeholder="Selecione os gráficos...",
                    maxHeight=300,
                    value=[],
                    multi=True,
                    options=[
                        {'label': 'IDH por bairro', 'value': 'IDH por bairro'},
                        {'label': 'Rotatividade por rendimento', 'value': 'Rotatividade por rendimento'},
                        {'label': 'Gráfico de Dispersão customizável', 'value': 'Gráfico de Dispersão customizável'},
                    ]
                ),
            ]),
        ]),
        html.Div([], id='numeros-interativos'),
        html.Div(id='dd-output-container'),

    ], className="content")
], className="banner2", id="sec2")

# callback do toggle
@dash.callback(
    Output("sec2", "className"),
    Input("toggle", "n_clicks"),
    State("sec2", "className"),
)
def toggle_classname(n, classname):
    if n and "active" in classname:
        return "banner"
    elif n:
        return "banner active"
    return classname

# callback do dropdown
@dash.callback(
    Output('dd-output-container', 'children'),
    Output('numeros-interativos', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    graphs = []
    dropdowns = []
    
    if 'IDH por bairro' in value:
        graphs.append(html.A([ 'IDH por Distrito' ]))
        graphs.append(dcc.Graph(figure=idh_por_bairro(), className="Idh por bairro"))
        
    if 'Rotatividade por rendimento' in value:
        graphs.append(html.A([ 'Rotatividade por rendimento' ]))
        graphs.append(dcc.Graph(figure=rotatividade_por_rendimento(), className="Rotatividade por rendimento"))
        
    if 'Gráfico de Dispersão customizável' in value:
        graphs.append(html.A([ 'Gráfico de Dispersão customizável' ]))
        scatter_plot_figure = dcc.Graph(id='scatterplot', figure=scatter_drop(), className="Gráfico de Dispersão customizável")
        graphs.append(scatter_plot_figure)
        dropdowns.append(dcc.Dropdown(id='dropdown1', placeholder="Selecione um dado...", maxHeight=300, value=[], options=dropdown_options, style={'width': '50%'}))
        dropdowns.append(dcc.Dropdown(id='dropdown2', placeholder="Selecione um dado...", maxHeight=300, value=[], options=dropdown_options, style={'width': '50%'}))
        graphs.append(html.Div(id='corr-text-container'))
    
    if not value:
        graphs.append(html.A([ 'IDH por bairro' ]))
        graphs.append(dcc.Graph(figure=idh_por_bairro(), className="Idh por bairro"))
        graphs.append(html.A([ 'Rotatividade por rendimento' ]))
        graphs.append(dcc.Graph(figure=rotatividade_por_rendimento(), className="Rotatividade por rendimento"))
        graphs.append(html.A([ 'Gráfico de Dispersão customizável' ]))
        graphs.append(dcc.Graph(id='scatterplot', figure=scatter_drop(), className="Gráfico de Dispersão customizável"))
    
    return graphs, dropdowns

@dash.callback(
    Output('scatterplot', 'figure'),
    Output('corr-text-container', 'children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value')
)
def update_scatterplot(dropdown1, dropdown2):
    if dropdown1 and dropdown2:
        fig = scatter_drop(dropdown1, dropdown2)
        
        corr_coef = np.corrcoef(df_dados_gerais[dropdown1], df_dados_gerais[dropdown2])[0, 1]
        corr_text = f'Correlação: {corr_coef:.2f}'
        
        fig.update_layout()
        
        return fig, corr_text
    
    return go.Figure(), None
