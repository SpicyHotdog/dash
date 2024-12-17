from dash import Dash, html

class MainApplication:
    def __init__(self):
        self.__app = Dash(
            __name__,
            use_pages=True,
        )
        self.set_layout()

    @property
    def app(self):
        return self.__app
    
    def set_layout(self):
        self.app.layout = html.Div(["Your Dash App Layout..."])

Application = MainApplication()
app = Application.app.server
