from dash import Input, Output, callback
from utils.load_data import DataProcessor
from dash import dash
from utils.plot_function import plot_bar


Ldata         = DataProcessor(r'data\kenya_hotels_detailed_data.xlsx')
meta_data      = Ldata.read_data('Hotel_Metadata')

# Read Price Rooms Sheet
price_rooms_data = Ldata.read_data('Price_Rooms')

# Detailed Amenities Data
detailed_amenities_data = Ldata.read_data('Detailed_Amenities')


# Create a dictionary for hotels

hotel_dict                       = Ldata.read_data('Unique Code')
hotel_dictionary_start_with_code = dict(zip(hotel_dict['Hotel Code'], hotel_dict['Hotel Name']))
hotel_dictionary_start_with_name = dict(zip(hotel_dict['Hotel Name'], hotel_dict['Hotel Code']))


def update_image_card():
    # --- Callback ---
    @callback(
        Output('card-image', 'src'),
        Output('card-title', 'children'),
        # Output('card-value', 'children'),
        Input('hotel-dropdown', 'value')
    )
    def update_card(selected_hotel):
        if not selected_hotel:
            return "", "", ""
        hotel_data = meta_data[meta_data['index'] == selected_hotel].iloc[0]
        return hotel_data['original_image'], selected_hotel
    
    
def updated_kpi_card():
    @callback(
        Output('card-revenue', 'children'),
        Output('card-ammenties', 'children'),
        Output('card-rating', 'children'),
        Output('card-location-rating', 'children'),
        Input('hotel-dropdown', 'value')
    )

    def update_kpi_card(input_value):
        
        hotel_code = hotel_dictionary_start_with_name.get(input_value)
        
        if not input_value:
            return "$0"
        
        hotel_price_data        = price_rooms_data[price_rooms_data['unicode'] == hotel_code]['rate_lowest'].min()
        hotel_price_data_in_kes = hotel_price_data * 130  # Assuming conversion rate to KES
        
        # Detailed Amenities
        amenities = detailed_amenities_data[ (detailed_amenities_data['unicode'] == hotel_code) & (detailed_amenities_data['available'] == True)]['amenity'].nunique()
        
        
        # Overall Rating
        overal_rating = meta_data[meta_data['unicode'] == hotel_code]['overal_rating'].iloc[0]
        
        # Location Rating 
        location_rating = meta_data[meta_data['unicode'] == hotel_code]['location_rating'].iloc[0]
        
        
        return f"KES{hotel_price_data_in_kes:,.0f}" ,   f"{amenities}"  , f"{overal_rating}", f"{location_rating}"
    
    
    
def update_bar_chart():
        
    @callback(Output('price-trend-graph', 'figure'),Input('hotel-dropdown', 'value'))
    def plot_price_bar(selected_hotel):
        
        hotel_code = hotel_dictionary_start_with_name.get(selected_hotel)
        
        if selected_hotel is None:
            return dash.no_update
        
        price_rooms_data_filtered                   = price_rooms_data[price_rooms_data['unicode'] == hotel_code]
        price_rooms_data_filtered['rate_lowest_']   = price_rooms_data_filtered['rate_lowest'] * 130  # Convert to KES
        price_rooms_data_filtered_grouped           = price_rooms_data_filtered.groupby('room_name')['rate_lowest_'].min().reset_index()[:4]

        fig = plot_bar(price_rooms_data_filtered_grouped, x_col='room_name', y_col='rate_lowest_', title=f'Room Prices for Top 4 {selected_hotel} (in KES)')
        
        return fig
        
