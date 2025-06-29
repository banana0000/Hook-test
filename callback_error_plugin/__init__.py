from dash import html, hooks, set_props, Input, Output

def generate_error_notification():
    return html.Div(
        [
            html.Span(
                "Callback errors will display here.",
                id="error-text",
                style={
                    "color": "red",
                    "fontWeight": "bold",
                    "fontSize": "1.1rem",
                    "backgroundColor": "black"
                },
            ),
            html.Button(
                "×",
                id="dismiss-button",
                style={
                    "position": "absolute",
                    "top": "5px",
                    "right": "10px",
                    "fontSize": "1.2rem",
                    "background": "none",
                    "border": "none",
                    "color": "#a94442",
                    "cursor": "pointer",
                },
            ),
        ],
        id="callback-error-banner-wrapper",
        style={
            "display": "none",
            "padding": "12px 16px",
            "border": "1px solid #f5c6cb",
            "background": "#c59599",
            "borderRadius": "8px",
            "position": "relative",
            "marginBottom": "18px",
            "textAlign": "center",
        },
    )

def add_error_notifications(error_text="There was an error"):
    @hooks.layout(priority=1)
    def update_layout(layout):
        # Megkeressük a CardBody-t, és annak children-jének elejére szúrjuk a hibaüzenetet
        def insert_error_banner(component):
            # Ha ez a CardBody, akkor módosítjuk a children-t
            if hasattr(component, "type") and getattr(component.type, "__name__", "") == "CardBody":
                children = list(component.children)
                children.insert(0, generate_error_notification())
                component.children = children
                return component
            # Ha van children attribútuma, rekurzívan keresünk tovább
            if hasattr(component, "children"):
                if isinstance(component.children, list):
                    component.children = [insert_error_banner(child) for child in component.children]
                elif component.children is not None:
                    component.children = insert_error_banner(component.children)
            return component

        if isinstance(layout, list):
            return [insert_error_banner(child) for child in layout]
        else:
            return insert_error_banner(layout)

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
        set_props("error-text", {"children": f"{error_text}: {err}"})

