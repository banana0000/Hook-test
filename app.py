from dash import dcc, html, callback, Input, Output, State, Dash
import callback_error_plugin_demo_7

app = Dash(__name__)

def serve_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.H2(
                        "Division Calculator",
                        style={"textAlign": "center", "fontSize": "2.2rem"},
                    ),
                    html.Label(
                        "Enter a number:",
                        htmlFor="input-number",
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
                    html.Button(
                        "Calculate",
                        id="calc-btn",
                        style={
                            "width": "100%",
                            "fontSize": "1.2rem",
                            "marginTop": "1rem",
                            "padding": "0.5rem",
                            "borderRadius": "6px",
                            "backgroundColor": "#6c757d",
                            "color": "white",
                            "border": "none",
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
                ],
                style={
                    "maxWidth": "400px",
                    "margin": "80px auto 0 auto",  # 80px top margin a banner miatt
                    "boxShadow": "0 2px 12px rgba(0,0,0,0.08)",
                    "borderRadius": "12px",
                    "backgroundColor": "#f9f9f9",
                    "fontFamily": "Segoe UI, Arial, sans-serif",
                    "padding": "32px",
                },
            )
        ]
    )

app.layout = serve_layout()

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