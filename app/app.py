from dash import Dash, page_container, html

class MainApplication:
    def __init__(self):
        self.__app = Dash(
            __name__,
            use_pages=True,
            pages_folder=""
        )
        self.set_layout()

    @property
    def app(self):
        return self.__app

    def set_layout(self):
        self.app.layout = html.Div(["Build something here..."])


# Instantiate the Dash application
Application = MainApplication()
# Expose the Flask server to Vercel
app = Application.app.server  # Vercel expects `app` to be the Flask instance
print('test')

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 5000))  # Use dynamic port
    Application.app.run(port=port, dev_tools_ui=True, debug=True, host="0.0.0.0")
