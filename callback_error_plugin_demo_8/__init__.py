from dash import html, hooks, set_props, Input, Output

def error_banner_component(
    banner_id="callback-error-banner-wrapper",
    text_id="error-text",
    dismiss_id="dismiss-button",
    default_text="Callback errors will display here.",
    color="red",
    background="black",
    border_color="#f5c6cb",
    z_index=9999,
    position="top",
):
    return html.Div(
        [
            html.Div(
                [
                    html.Span(
                        default_text,
                        id=text_id,
                        style={
                            "color": color,
                            "fontWeight": "bold",
                            "fontSize": "2rem",
                            "backgroundColor": background,
                            "margin": "0 auto",
                        },
                    ),
                    html.Button(
                        "×",
                        id=dismiss_id,
                        style={
                            "position": "absolute",
                            "top": "5px",
                            "right": "10px",
                            "fontSize": "2rem",
                            "background": "none",
                            "border": "none",
                            "color": color,
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
        id=banner_id,
        style={
            "display": "none",
            "padding": "12px 16px",
            "border": f"1px solid {border_color}",
            "background": "#c59599",
            "borderRadius": "0 0 8px 8px",
            "position": "fixed",
            "top": "0" if position == "top" else "unset",
            "bottom": "0" if position == "bottom" else "unset",
            "left": "0",
            "right": "0",
            "width": "100vw",
            "zIndex": z_index,
            "textAlign": "center",
            "boxSizing": "border-box",
        },
    )

def register_error_banner_callbacks(
    banner_id="callback-error-banner-wrapper",
    text_id="error-text",
    dismiss_id="dismiss-button",
    default_text="Callback errors will display here.",
    color="red",
    background="black",
    border_color="#f5c6cb",
    z_index=9999,
    position="top",
):
    @hooks.callback(
        Output(banner_id, "style"),
        Input(dismiss_id, "n_clicks"),
        prevent_initial_call=True,
    )
    def hide_banner(n_clicks):
        if n_clicks:
            return {
                "display": "none",
                "padding": "12px 16px",
                "border": f"1px solid {border_color}",
                "background": "#c59599",
                "borderRadius": "0 0 8px 8px",
                "position": "fixed",
                "top": "0" if position == "top" else "unset",
                "bottom": "0" if position == "bottom" else "unset",
                "left": "0",
                "right": "0",
                "width": "100vw",
                "zIndex": z_index,
                "textAlign": "center",
                "boxSizing": "border-box",
            }

    def show_banner(message):
        set_props(
            banner_id,
            {
                "style": {
                    "display": "block",
                    "padding": "12px 16px",
                    "border": f"1px solid {border_color}",
                    "background": "#c59599",
                    "borderRadius": "0 0 8px 8px",
                    "position": "fixed",
                    "top": "0" if position == "top" else "unset",
                    "bottom": "0" if position == "bottom" else "unset",
                    "left": "0",
                    "right": "0",
                    "width": "100vw",
                    "zIndex": z_index,
                    "textAlign": "center",
                    "boxSizing": "border-box",
                }
            },
        )
        set_props(text_id, {"children": message})

    return show_banner