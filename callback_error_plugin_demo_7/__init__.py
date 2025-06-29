from dash import html, hooks, set_props, Input, Output

def generate_error_notification():
    return html.Div(
        [
            html.Div(
                [
                    html.Span(
                        "Callback errors will display here.",
                        id="error-text",
                        style={
                            "color": "red",
                            "fontWeight": "bold",
                            "fontSize": "2rem",
                            "backgroundColor": "black",
                            "margin": "0 auto",
                        },
                    ),
                    html.Button(
                        "×",
                        id="dismiss-button",
                        style={
                            "position": "absolute",
                            "top": "5px",
                            "right": "10px",
                            "fontSize": "2rem",
                            "background": "none",
                            "border": "none",
                            "color": "#a94442",
                            "cursor": "pointer",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "position": "relative",
                    "width": "100%",
                },
            )
        ],
        id="callback-error-banner-wrapper",
        style={
            "display": "none",
            "padding": "12px 16px",
            "border": "1px solid #f5c6cb",
            "background": "#c59599",
            "borderRadius": "0 0 8px 8px",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "right": "0",
            "width": "100vw",
            "zIndex": 9999,
            "textAlign": "center",
            "boxSizing": "border-box",
        },
    )

@hooks.layout(priority=1)
def update_layout(layout):
    if isinstance(layout, list):
        return [generate_error_notification()] + layout
    elif hasattr(layout, "children"):
        children = layout.children
        if not isinstance(children, list):
            children = [children]
        layout.children = [generate_error_notification()] + list(children)
        return layout
    return layout

@hooks.callback(
    Output("callback-error-banner-wrapper", "style"),
    Input("dismiss-button", "n_clicks"),
    prevent_initial_call=True,
)
def hide_banner(n_clicks):
    if n_clicks:
        return {"display": "none"}

@hooks.error()
def on_error(err):
    set_props("callback-error-banner-wrapper", {"style": {"display": "block"}})
    set_props("error-text", {"children": f"Error: {err}"})