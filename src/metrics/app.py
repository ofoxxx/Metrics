import dash
from dash import html, dcc
import plotly.express as px
from metrics.core import get_commits_per_day

def create_app():
    commits_per_day = get_commits_per_day()
    fig = px.bar(commits_per_day, x='day', y='commits', title='Commits Per Day')

    app = dash.Dash(__name__)
    app.layout = html.Div(children=[
        html.H1(children='GitHub Analytics Dashboard'),
        dcc.Graph(
            id='commits-per-day',
            figure=fig
        ),
        # Add more graphs as needed
    ])
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
