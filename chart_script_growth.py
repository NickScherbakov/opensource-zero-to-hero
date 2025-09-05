import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Create growth trends data (2019-2025)
years = list(range(2019, 2026))
data = {
    "year": years,
    "total_funding_b": [8.2, 12.1, 15.6, 18.9, 21.2, 24.1, 26.4],
    "companies_funded": [245, 320, 420, 510, 630, 720, 800],
    "average_round_size_m": [8.5, 9.2, 10.1, 11.8, 13.2, 14.7, 15.8],
    "open_source_percentage": [45, 52, 58, 63, 67, 71, 74]
}

df = pd.DataFrame(data)

# Create subplot with secondary y-axis
fig = go.Figure()

# Add funding trend
fig.add_trace(go.Scatter(
    x=df['year'], 
    y=df['total_funding_b'],
    mode='lines+markers',
    name='Total Funding ($B)',
    line=dict(color='#4299e1', width=3),
    marker=dict(size=8),
    hovertemplate="<b>%{x}</b><br>Total Funding: $%{y:.1f}B<extra></extra>"
))

# Add companies funded trend
fig.add_trace(go.Scatter(
    x=df['year'], 
    y=df['companies_funded']/10,  # Scale down for visibility
    mode='lines+markers',
    name='Companies Funded (×10)',
    line=dict(color='#667eea', width=3, dash='dash'),
    marker=dict(size=8),
    yaxis='y2',
    hovertemplate="<b>%{x}</b><br>Companies: %{customdata}<extra></extra>",
    customdata=df['companies_funded']
))

# Add average round size trend
fig.add_trace(go.Scatter(
    x=df['year'], 
    y=df['average_round_size_m'],
    mode='lines+markers',
    name='Avg Round Size ($M)',
    line=dict(color='#764ba2', width=3, dash='dot'),
    marker=dict(size=8),
    yaxis='y3',
    hovertemplate="<b>%{x}</b><br>Avg Round: $%{y:.1f}M<extra></extra>"
))

# Update layout with multiple y-axes
fig.update_layout(
    title='Open Source Funding Growth Trends (2019-2025)',
    xaxis=dict(title='Year', tickmode='linear', tick0=2019, dtick=1),
    yaxis=dict(
        title='Total Funding ($B)',
        title_font=dict(color='#4299e1'),
        tickfont=dict(color='#4299e1'),
        side='left'
    ),
    yaxis2=dict(
        title='Companies Funded (×10)',
        title_font=dict(color='#667eea'),
        tickfont=dict(color='#667eea'),
        anchor='x',
        overlaying='y',
        side='right',
        range=[0, 100]
    ),
    yaxis3=dict(
        title='Avg Round Size ($M)',
        title_font=dict(color='#764ba2'),
        tickfont=dict(color='#764ba2'),
        anchor='free',
        overlaying='y',
        side='right',
        position=0.95,
        range=[0, 20]
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    hovermode='x unified',
    font=dict(size=12),
    margin=dict(l=50, r=80, t=80, b=50)
)

# Save the chart
fig.write_image('images/growth_trends.png', width=900, height=500)
print("Growth trends chart saved to images/growth_trends.png")