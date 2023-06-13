from dash import html, dcc, callback
import dash
from dash.dependencies import Input, Output, State
from datetime import *
import pandas as pd
import numpy as np
import plotly.express as px

dash.register_page(
    __name__,
    path='/links', #criando um path para pagina (MUDAR)
    name='Links', #nome da pagina (MUDAR)
    title='Links') #titulo da pagina (MUDAR)

layout = html.Div([

html.Section([

    html.Header([
        html.Img(src= "/assets/logo.png", className="logo"),
        html.Div([
            dcc.Link(' Home', href='/', className="fa-solid fa-house"),
            dcc.Link(' Graficos', href='/home', className="fa-solid fa-chart-simple"),    
])

    ]),

    html.Div([
        html.H1(' Bibliografia', className="fa-solid fa-magnifying-glass", id = "bibliografiatitulo"),
        #html.P('Aqui você pode encontrar as fontes utilizadas para a criação dos graficos.', className="text3"),
        

        html.Div([
        html.P('Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira | Inep. Censo Escolar. Disponível em https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar. Acesso em 31 de Maio de 2023.', className="text3"),
        html.P('Scielo. Indicadores de retenção e rotatividade dos docentes da educação básica. Disponível em https://www.scielo.br/j/cp/a/B6szXszKwjCjCcDqpJFXsNJ/?lang=pt. Acesso em 31 de Maio de 2023.', className="text3"),
        html.P('Governo do Estado de São Paulo. Localize Escola. Disponível em http://www.educacao.sp.gov.br/central-de-atendimento/index_escolas.asp. Acesso em 01 de Junho de 2023.', className="text3"),
        html.P('City Facts. CityFacts. Disponível em https://pt.city-facts.com/. Acesso em 01 de Junho de 2023. ', className="text3"),
], className="bibliografia"),

    ],),

        html.Div(id='dd-output-container')], className="content")

], className="banner2")
