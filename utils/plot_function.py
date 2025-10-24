import pandas as pd 
import plotly.express as px


def plot_bar(data: pd.DataFrame, x_col: str, y_col: str, title: str = None):
    """
    Create a professional bar chart with enhanced styling.
    
    Args:
        data: DataFrame containing the data
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        title: Chart title (optional)
    """
    # Sort data for better visualization
    data_sorted = data.sort_values(by=y_col, ascending=False)
    
    # Create figure
    fig = px.bar(
        data_sorted,
        x=x_col,
        y=y_col,
        title=title or f'{y_col} by {x_col}',
        template='plotly_white',
        color=y_col,
        color_continuous_scale='Blues'
    )
    
    # Professional styling updates
    fig.update_traces(
        marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5,
        opacity=0.9,
        texttemplate='%{y:,.0f}',
        textposition='outside',
        textfont_size=11
    )
    
    fig.update_layout(
        # Title styling
        title={
            'text': title or f'{y_col} by {x_col}',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial, sans-serif'}
        },
        
        # Axes styling
        xaxis={
            'title': x_col.replace('_', ' ').title(),
            'tickangle': -45 if len(data) > 10 else 0,
            'showgrid': False,
            'showline': True,
            'linewidth': 2,
            'linecolor': '#34495e',
            'title_font': {'size': 14, 'color': '#2c3e50'}
        },
        yaxis={
            'title': y_col.replace('_', ' ').title(),
            'showgrid': True,
            'gridwidth': 1,
            'gridcolor': '#ecf0f1',
            'showline': True,
            'linewidth': 2,
            'linecolor': '#34495e',
            'title_font': {'size': 14, 'color': '#2c3e50'}
        },
        
        # Layout
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'family': 'Arial, sans-serif', 'color': '#2c3e50'},
        height=415,
        margin=dict(l=80, r=40, t=80, b=80),
        
        # Remove colorbar for cleaner look
        coloraxis_showscale=False,
        
        # Hover template
        hovermode='x unified'
    )
    
    # Update hover template for better info display
    fig.update_traces(
        hovertemplate='<b>%{x}</b><br>' +
                      f'{y_col}: %{{y:,.2f}}<br>' +
                      '<extra></extra>'
    )
    
    return fig