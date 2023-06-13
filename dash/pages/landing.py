from dash import html, dcc, callback
import dash
from dash.dependencies import Input, Output, State
from datetime import *
import pandas as pd
import numpy as np
import plotly.express as px

dash.register_page(
    __name__,
    path='/', #criando um path para pagina (MUDAR)
    name='Landing', #nome da pagina (MUDAR)
    title='Landing') #titulo da pagina (MUDAR)

layout = html.Div([

html.Section([

    html.Header([
        html.Img(src= "/assets/logo.png", className="logo"),
        html.Div([
            dcc.Link(' Graficos', href='/home', className="fa-solid fa-chart-simple"),
            dcc.Link(' Bibliografia', href='/links', className="fa-solid fa-magnifying-glass"),     
])

    ]),

    html.Div([
        #html.H1('Bem vindo!', className="title2"),
        #html.P('Aqui você pode encontrar os gráficos que mostram a evolução do IDH de São Paulo, além de poder comparar com outros países e estados do Brasil.', className="text2"),
        html.Video(src="/assets/video.mp4", autoPlay=True, loop=True, muted=True, className="video"),

    ],),

        html.Div(id='dd-output-container')], className="content")

], className="banner2")
