import plotly.express as px
import pandas as pd

# Create the data
data = {
    "sector": ["AI/ML Platfrm", "Dev Tools", "Cloud Infra", "Data Mgmt", "Security", "DevOps/CI-CD", "Blockchain", "IoT/Edge", "Analytics", "Collaboration"],
    "total_funding_2025_b": [8.2, 6.1, 5.8, 4.3, 3.4, 2.9, 2.1, 1.7, 1.5, 1.2],
    "open_source_percentage": [78, 84, 71, 69, 63, 79, 95, 58, 67, 45]
}

df = pd.DataFrame(data)

# Create horizontal bar chart
fig = px.bar(df, 
             y='sector', 
             x='total_funding_2025_b',
             color='open_source_percentage',
             orientation='h',
             color_continuous_scale='Blues',
             title="2025 Funding by Sector & Open Source %",
             hover_data={'total_funding_2025_b': ':.1f', 'open_source_percentage': True})

# Update traces
fig.update_traces(cliponaxis=False)

# Update layout
fig.update_layout(
    xaxis_title="Funding ($B)",
    yaxis_title="Sector",
    coloraxis_colorbar=dict(title="Open Source %")
)

# Customize hover template to show both values
fig.update_traces(
    hovertemplate="<b>%{y}</b><br>" +
                  "Funding: $%{x:.1f}B<br>" +
                  "Open Source: %{color}%<br>" +
                  "<extra></extra>"
)

fig.write_image("images/funding_by_sector.png")