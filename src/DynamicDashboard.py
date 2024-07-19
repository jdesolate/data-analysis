import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('../datasets/COVID-19 Coronavirus.csv').head(5)

total_quantity = df['Population'].sum()
df['Percentage'] = (df['Population'] / total_quantity) * 100

app = dash.Dash(__name__)

app.layout = html.Div([
  dcc.Dropdown(
  id='country-dropdown',
  options=[{'label': country, 'value': country} for country in df['Country']],
  value='Afghanistan',
  clearable=False
  ),
  dcc.Graph(id='population-bar-chart'),
  dcc.Graph(id='pie-chart'),
  dcc.Graph(id='cases-bar-chart'),
  dcc.Graph(id='deaths-bar-chart'),
  dcc.Graph(id='deaths-percentage-bar-chart'),
])

@app.callback(
  Output('cases-bar-chart', 'figure'),
  Input('country-dropdown', 'value')
)
def update_value_bar_chart(selected_country):
  filtered_df = df[df['Country'] == selected_country]
  fig = px.bar(filtered_df, x='Country', y='Total Cases', title=f'Total COVID Cases for {selected_country}')
  return fig

@app.callback(
  Output('deaths-bar-chart', 'figure'),
  Input('country-dropdown', 'value')
)
def update_deaths_bar_chart(selected_country):
  filtered_df = df[df['Country'] == selected_country]
  fig = px.bar(filtered_df, x='Country', y='Total Deaths', title=f'Total Deaths for {selected_country}')
  return fig

@app.callback(
  Output('deaths-percentage-bar-chart', 'figure'),
  Input('country-dropdown', 'value')
)
def update_deaths_bar_chart(selected_country):
  fig = px.bar(df, x='Country', y='Death percentage', title=f'Death Percentage for Each Country')
  return fig

@app.callback(
  Output('population-bar-chart', 'figure'),
  Input('country-dropdown', 'value')
)
def update_population_bar_chart(selected_country):
  filtered_df = df[df['Country'] == selected_country]
  fig = px.bar(filtered_df, x='Country', y='Population', title=f'Population for {selected_country}')
  return fig

@app.callback(
  Output('pie-chart', 'figure'),
  Input('country-dropdown', 'value')
)
def update_pie_chart(selected_country):
  fig = px.pie(df, names='Country', values='Population', title='Country Population Distribution', 
  color='Country', 
  color_discrete_sequence=px.colors.qualitative.Set3)
  return fig

if __name__ == '__main__':
  app.run_server(debug=True)
