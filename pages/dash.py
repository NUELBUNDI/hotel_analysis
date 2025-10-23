import dash 
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from utils.load_data import DataProcessor
from component.callback_ import update_image_card,updated_kpi_card
from component.card import kpi_card


dash.register_page(__name__, path='/',name='Main')


# Load the data

Ldata         = DataProcessor(r'data\kenya_hotels_detailed_data.xlsx')
meta_data      = Ldata.read_data('Hotel_Metadata')
list_of_hotels = meta_data['index'].unique().tolist()
list_of_hotels= list_of_hotels.sort()

# Read Price Rooms Sheet
price_rooms_data = Ldata.read_data('Price_Rooms')

# Detailed Amenities Data
detailed_amenities_data = Ldata.read_data('Detailed_Amenities')


# Create a dictionary for hotels

hotel_dict                       = Ldata.read_data('Unique Code')
hotel_dictionary_start_with_code = dict(zip(hotel_dict['Hotel Code'], hotel_dict['Hotel Name']))
hotel_dictionary_start_with_name = dict(zip(hotel_dict['Hotel Name'], hotel_dict['Hotel Code']))



# Layout for the main dashboard page

layout = dbc.Container(
    
    [
       
        
        ## Dropdown Row and KPI Cards
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='hotel-dropdown',
                    options=[{'label':h , 'value':h} for h in sorted(meta_data['index'].unique().tolist())],
                    value='Eka Hotel',
                    placeholder="Select a Hotel",
                )
                     ],width=4,),
            
            dbc.Col([
                html.H3("Welcome to the Hotel Analytics Dashboard", className="text-center"),
            ])
    
            
            
            
               ],class_name='mb-4'),
        

        
        
        ## Cards Row
        dbc.Row([
            
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(id='card-image', src="", top=True, style={"height": "350", "object-fit": "cover"}),
                    dbc.CardBody([
                        html.H6(id='card-title', className="card-title"),
                    ]),
                    
                
                ], color="primary", inverse=True)
            ], width=4 ),
            
            dbc.Col([
                    kpi_card('card-revenue', 'Lowest Room Price', icon="fas fa-bed")

                
                ],xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([
                kpi_card('card-rating', 'Overall Rating', icon="fas fa-star")
                
                
                ],xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([
                kpi_card('card-ammenties', 'Number of Amenities', icon="fas fa-list-check")
                
                ],xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([
                kpi_card('card-location-rating', 'Location Rating', icon="fas fa-location-dot")

                
                ],xs=12, sm=6, md=6, lg=3, xl=2),
            
            
         ]),
        
        
    ], fluid=True
                      )

# --- Callback ---

# Image Card Callback
update_image_card()
# KPI Card Callbacks 
updated_kpi_card()
    

