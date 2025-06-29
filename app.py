import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Input, Output, State, Dash
from callback_error_plugin import add_error_notifications, generate_error_notification

add_error_notifications("Error message")



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            html.H2(
                                "Division Calculator",
                                className="text-center",
                                style={"fontSize": "2.2rem"},
                            )
                        ),
                        dbc.CardBody(
                            [
                                # Hibaüzenet a CardBody elején!
                                generate_error_notification(),
                                dbc.Label(
                                    "Enter a number:",
                                    html_for="input-number",
                                    style={"fontSize": "1.3rem"},
                                ),
                                dcc.Input(
                                    id="input-number",
                                    type="number",
                                    value=1,
                                    style={
                                        "fontSize": "1.3rem",
                                        "width": "100%",
                                        "marginBottom": "1rem",
                                        "marginTop": "0.5rem",
                                        "padding": "0.5rem",
                                        "borderRadius": "6px",
                                        "border": "1px solid #ccc",
                                    },
                                ),
                                dbc.Button(
                                    "Calculate",
                                    id="calc-btn",
                                    color="secondary",
                                    size="lg",
                                    style={
                                        "width": "100%",
                                        "fontSize": "1.2rem",
                                        "marginTop": "1rem",
                                    },
                                    n_clicks=0,
                                ),
                                html.Div(
                                    id="output-div",
                                    style={
                                        "fontSize": "1.4rem",
                                        "marginTop": "2rem",
                                        "minHeight": "2.5rem",
                                        "textAlign": "center",
                                    },
                                ),
                            ]
                        ),
                    ],
                    style={
                        "maxWidth": "400px",
                        "margin": "0 auto",
                        "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
                        "borderRadius": "12px",
                        "backgroundColor": "#f9f9f9",
                        "fontFamily": "Segoe UI, Arial, sans-serif",
                    },
                ),
                width=12,
            ),
            justify="center",
            align="center",
            style={"width": "100%"},
        )
    ],
    fluid=True,
    style={
        "height": "100vh",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
    },
)

@callback(
    Output("output-div", "children"),
    Input("calc-btn", "n_clicks"),
    State("input-number", "value"),
)
def update_output(n_clicks, value):
    if n_clicks == 0:
        return ""
    result = 10 / value
    return f"The result is {result}"


if __name__ == "__main__":
    app.run(debug=True)