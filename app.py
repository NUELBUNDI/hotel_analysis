import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap theme
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
    title="Hotel Dashboard"
)

server = app.server

# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Main", href="/")),
        dbc.NavItem(dbc.NavLink("Bookings", href="/bookings")),
        # dbc.NavItem(dbc.NavLink("Ratings", href="/ratings")),
        # dbc.NavItem(dbc.NavLink("Revenue", href="/revenue")),
    ],
    brand="Top 10 Hotel Analytics Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-4"
)

# App layout
app.layout = dbc.Container([
    navbar,
    dash.page_container
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True, port=8050)