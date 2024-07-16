import reflex as rx

from .routes import index, detail, comparison, about


app = rx.App()
app.add_page(index, title="Home")
app.add_page(detail, title="Detail View")
app.add_page(comparison, title="Comparison View")
app.add_page(about, title="About")