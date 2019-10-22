import dash

"""
A safe place for the dash app to hang out.
"""

app = dash.Dash(__name__)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "UC Berkeley Graduate Data Visualization Contest"
