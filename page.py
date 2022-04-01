import dash
# Code from: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import PIL
import plotly.express as px

BACKGROUND_IMAGE_PATH = 'pages/assets/background.PNG'
img = PIL.Image.open(BACKGROUND_IMAGE_PATH)

myCard = dbc.Card([
    dbc.CardImg(src=BACKGROUND_IMAGE_PATH, top=True, alt='Cant load background'),
    dbc.CardImgOverlay(
        dbc.Col(html.H1(f'To demo that the Path works on PIL library, img size is:{img.size}', className='text-center'), style={'textAlign': 'center'})
        )])

layout = html.Div(
    [
       myCard
    ]
)
