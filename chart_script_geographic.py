import plotly.express as px
import pandas as pd

# Create geographic distribution data
data = {
    "region": ["United States", "Europe", "Asia-Pacific", "Canada", "Israel", "Other"],
    "funding_percentage": [60, 25, 10, 3, 1.5, 0.5],
    "total_funding_b": [15.8, 6.6, 2.6, 0.8, 0.4, 0.2],
    "companies_count": [480, 200, 80, 24, 12, 4]
}

df = pd.DataFrame(data)

# Create pie chart for geographic distribution
fig = px.pie(df, 
             values='funding_percentage', 
             names='region',
             title='Geographic Distribution of Open Source Funding 2025',
             color_discrete_sequence=['#4299e1', '#667eea', '#764ba2', '#9f7aea', '#f093fb', '#f5f7fa'])

# Update traces for better visibility
fig.update_traces(
    textposition='inside', 
    textinfo='percent+label',
    hovertemplate="<b>%{label}</b><br>" +
                  "Funding Share: %{percent}<br>" +
                  "Total Funding: $%{customdata[0]:.1f}B<br>" +
                  "Companies: %{customdata[1]}<br>" +
                  "<extra></extra>",
    customdata=list(zip(df['total_funding_b'], df['companies_count']))
)

# Update layout
fig.update_layout(
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.05
    ),
    font=dict(size=12),
    margin=dict(l=20, r=120, t=60, b=20)
)

# Save the chart
fig.write_image('images/geographic_distribution.png', width=800, height=500)
print("Geographic distribution chart saved to images/geographic_distribution.png")