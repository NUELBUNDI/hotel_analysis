import dash 
from   dash import Dash, html, dcc
import dash_bootstrap_components as dbc



def create_card(title, value, image_url=None, color="primary"):
    image_component = dbc.CardImg(
        src=image_url or "",   # leave blank until updated
        top=True,
        id=f"{title}-image",   # <-- add this ID
        style={
            "height": "200px",
            "object-fit": "cover",
            "width": "100%"
        }
    )

    card_content = [
        image_component,
        dbc.CardBody([
            html.H4(title, className=f"text-{color}"),
            html.H2(value, id=f"{title}-value", className="card-value"),
        ])
    ]
    
    return dbc.Card(card_content, className="mb-4 text-center shadow")
