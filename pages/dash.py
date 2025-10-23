import dash 
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from component.card import create_card
from utils.load_data import DataProcessor


dash.register_page(__name__, path='/',name='Main')


# Load the data

Ldata         = DataProcessor(r'data\kenya_hotels_detailed_data.xlsx')
meta_data      = Ldata.read_data('Hotel_Metadata')
list_of_hotels = meta_data['index'].unique().tolist()





# Layout for the main dashboard page

layout = dbc.Container(
    
    [
        html.H1("Welcome to the Hotel Analytics Dashboard", className="text-center my-4"),
        
        ## Dropdown Row
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='hotel-dropdown',
                    options=[{'label':h , 'value':h} for h in meta_data['index'].unique().tolist()],
                    value='Eka Hotel',
                    placeholder="Select a Hotel",
                )
                     ],width=4,),
               ],class_name='mb-4'),
        
        
        ## Cards Row
        dbc.Row([
            
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(id='card-image', src="", top=True, style={"height": "200px", "object-fit": "cover"}),
                    dbc.CardBody([
                        html.H5(id='card-title', className="card-title"),
                        html.H2(id='card-value', className="card-text")
                    ]),
                    
                dbc.Markdown([])
                
                
                ], color="primary", inverse=True)
            ], width=4),
        ]),
        
        
    ], fluid=True
    
    
                      )




# --- Callback ---
@callback(
    Output('card-image', 'src'),
    Output('card-title', 'children'),
    Output('card-value', 'children'),
    Input('hotel-dropdown', 'value')
)
def update_card(selected_hotel):
    if not selected_hotel:
        return "", "", ""
    hotel_data = meta_data[meta_data['index'] == selected_hotel].iloc[0]
    return hotel_data['original_image'], selected_hotel, f"⭐ {hotel_data['rating']}"
