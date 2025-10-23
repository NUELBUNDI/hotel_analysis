import dash 
from   dash import Dash, html, dcc
import dash_bootstrap_components as dbc



def kpi_card(card_revenue, title, icon="fas fa-chart-line", color="#2174ab"):
    
    kpi_card = dbc.Card([
        dbc.CardBody([
            html.Div([
                dbc.Row([
                    # Icon column
                    dbc.Col([
                        html.Div([
                            html.I(
                                className=icon,
                                style={
                                    "fontSize": "2.5rem",
                                    "color": color,
                                    "opacity": "0.9"
                                }
                            )
                        ], style={
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "height": "100%"
                        })
                    ], width=4),
                    
                    # Content column
                    dbc.Col([
                        # Title with subtle styling
                        html.P(
                            title,
                            className="mb-1",
                            style={
                                "fontSize": "0.75rem",
                                "fontWeight": "600",
                                "letterSpacing": "0.5px",
                                "textTransform": "uppercase",
                                "color": "#5a6c7d"
                            }
                        ),
                        # Main KPI value with emphasis
                        html.H3(
                            id=f'{card_revenue}',
                            className="mb-0",
                            style={
                                "fontWeight": "700",
                                "color": "#1a252f",
                                "fontSize": "clamp(1.2rem, 2vw, 1.75rem)"
                            }
                        ),
                    ], width=8, style={"textAlign": "center"})
                ], className="g-0")
            ])
        ], className="p-3")
    ], 
    className="shadow border-0 h-25",
    style={
        "minHeight": "110px",
        "borderRadius": "12px",
        "transition": "transform 0.2s, box-shadow 0.2s",
        "background": f"linear-gradient(135deg, {color}20 0%, {color}35 100%)",
        "borderLeft": f"4px solid {color}"
    })
    
    return kpi_card