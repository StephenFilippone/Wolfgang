import plotly.express as px
import pandas as pd

df = pd.read_csv('TEMPER.csv')
df['Region'] = df['Region'].astype(str)

fig = px.scatter(df, x="Period", y="TEMPER", size='value', color='Region')

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [1, 2, 3],
        ticktext = ['One', 'Two', 'Three']
    )
)

fig.update_layout(scattermode="group",scattergap=0.75)

fig.show()