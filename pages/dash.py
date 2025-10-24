import dash 
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from utils.load_data import DataProcessor
from component.callback_ import update_image_card,updated_kpi_card ,update_bar_chart
from component.card import kpi_card
from utils.plot_function import plot_bar


dash.register_page(__name__, path='/',name='Main')


# Load the data

Ldata           = DataProcessor(r'data\kenya_hotels_detailed_data.xlsx')
meta_data       = Ldata.read_data('Hotel_Metadata')
list_of_hotels  = meta_data['index'].unique().tolist()
list_of_hotels  = list_of_hotels.sort()

# Read Price Rooms Sheet
price_rooms_data = Ldata.read_data('Price_Rooms')

# Detailed Amenities Data
detailed_amenities_data = Ldata.read_data('Detailed_Amenities')

# Service Reviews
service_reviews_data = Ldata.read_data('Service_Reviews')



# Create a dictionary for hotels
hotel_dict                       = Ldata.read_data('Unique Code')
hotel_dictionary_start_with_code = dict(zip(hotel_dict['Hotel Code'], hotel_dict['Hotel Name']))
hotel_dictionary_start_with_name = dict(zip(hotel_dict['Hotel Name'], hotel_dict['Hotel Code']))



# Layout for the main dashboard page

layout = dbc.Container(
    [
        # --- Dropdown + Title Row ---
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='hotel-dropdown',
                    options=[{'label': h, 'value': h} for h in sorted(meta_data['index'].unique().tolist())],
                    value='Eka Hotel',
                    placeholder="Select a Hotel",
                )
            ], width=4),
            dbc.Col([kpi_card('card-revenue', 'Lowest Room Price', icon="fas fa-bed")],
                    xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([kpi_card('card-rating', 'Overall Rating', icon="fas fa-star")],
                    xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([kpi_card('card-ammenties', 'Number of Amenities', icon="fas fa-list-check")],
                    xs=12, sm=6, md=6, lg=3, xl=2),
            dbc.Col([kpi_card('card-location-rating', 'Location Rating', icon="fas fa-location-dot")],
                    xs=12, sm=6, md=6, lg=3, xl=2),
            
            

            # dbc.Col([
                
            #     # html.H3("Welcome to the Hotel Analytics Dashboard", className="text-center"),
            
            
            # ])
        ], class_name='mb-4'),

        # --- Cards Row ---
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(id='card-image', src="", top=True,
                                style={"height": "350px", "object-fit": "cover"}),
                    dbc.CardBody([
                        html.H6(id='card-title', className="card-title"),
                                ]),
                         ], color="primary", inverse=True)
                    ], width=4),
            dbc.Col([
                  dcc.Graph(id='price-trend-graph')
                    ], width=8,class_name='mb-4 shadow-sm'),
            
        


        ], class_name='mb-4'),

        # --- Tables---
        dbc.Row([
            
            
            dbc.Col([
                
                dag.AgGrid(
                    id='service-review-table',
                    rowData=service_reviews_data.to_dict('records'),
                    columnDefs=[{"headerName": i.replace('_', ' ').title(), "field": i} for i in service_reviews_data.columns],
                    defaultColDef={"sortable": True, "filter": True, "resizable": True},
                    columnSize="sizeToFit",
                    dashGridOptions={"pagination": True, "paginationPageSize": 10},
                )
                
                
                
                   ]),
            dbc.Col([
                
                
                
                
                   ])
            


                 ]),
    ],
    fluid=True
)

                      

# --- Callback ---

# Image Card Callback
update_image_card()

# KPI Card Callbacks 
updated_kpi_card()

# Bar Chart Callback
update_bar_chart()

# Servce Review Table Callback

@callback(
    
    Output('service-review-table', 'rowData'),
    Input('hotel-dropdown', 'value')
)
def update_service_review_table(selected_hotel):
    
    if selected_hotel is None:
        dash.no_update
        
        
    hotel_code    = hotel_dictionary_start_with_name.get(selected_hotel)
    filtered_data = service_reviews_data[service_reviews_data['unicode'] == hotel_code]
    
    pass

