import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Create the data
data = {
    "company_name": ["GitHub", "Red Hat", "GitLab", "Elastic", "MongoDB", "Confluent", "HashiCorp", "Databricks", "Snowflake", "Docker"],
    "github_stars_k": [57.5, 2.1, 23.7, 68.2, 26.8, 9.2, 14.8, 39.0, 4.2, 68.7],
    "exit_valuation_b": [7.5, 34.0, 16.0, 7.0, 24.0, 9.5, 15.2, 43.0, 70.0, 1.1],
    "exit_type": ["Acquisition", "Acquisition", "IPO", "IPO", "IPO", "IPO", "IPO", "Private", "IPO", "Private"]
}

df = pd.DataFrame(data)

# Create abbreviated company names for better display
df['short_name'] = df['company_name'].apply(lambda x: x[:8] if len(x) > 8 else x)

# Create scatter plot
fig = px.scatter(df, 
                 x='github_stars_k', 
                 y='exit_valuation_b',
                 color='exit_type',
                 text='short_name',
                 hover_name='company_name',
                 color_discrete_sequence=['#DB4545', '#1FB8CD', '#2E8B57'],
                 title='GitHub Stars vs Exit Valuation',
                 labels={'github_stars_k': 'GitHub Stars (k)', 'exit_valuation_b': 'Exit Val ($b)'})

# Update traces for better visibility
fig.update_traces(
    cliponaxis=False, 
    marker=dict(size=12),
    textposition="top center",
    textfont=dict(size=10)
)

# Add trend line using all data points
x_vals = df['github_stars_k'].values
y_vals = df['exit_valuation_b'].values

# Calculate linear trend line (avoiding log scaling issues)
z = np.polyfit(x_vals, y_vals, 1)
x_trend = np.linspace(x_vals.min(), x_vals.max(), 100)
y_trend = z[0] * x_trend + z[1]

fig.add_trace(go.Scatter(
    x=x_trend, 
    y=y_trend, 
    mode='lines', 
    name='Trend', 
    line=dict(dash='dash', color='#5D878F', width=3),
    showlegend=True
))

# Update layout with centered legend
fig.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5))

# Use reasonable axis formatting
fig.update_xaxes(title='GitHub Stars (k)', tickformat='.0f')
fig.update_yaxes(title='Exit Val ($b)', tickformat='.0f')

# Save the chart
fig.write_image('github_stars_vs_exit_valuation.png')