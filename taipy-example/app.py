from taipy.gui import Gui, Markdown
import taipy.gui.builder as tgb
import pandas as pd
import requests


def load_user_data(limit: int = 10, offset: int = 0):
    response = requests.get(
        "http://localhost:8080/users",
        params={"limit": limit, "offset": offset},
    )
    return pd.DataFrame(response.json())


with tgb.Page(
    title="E-Commerce Dashboard", fillable=True, sidebar_state="collapsed"
) as page:
    tgb.toggle(theme=True, sidebar=True)
    tgb.text("E-Commerce Dashboard", h1=True)
    tgb.slider(
        id="limit",
        label="Number of records",
        min=10,
        max=10000,
        value=100,
        step=10,
    )
    tgb.slider(
        id="offset",
        label="Number of records to skip",
        min=0,
        max=10000,
        value=0,
    )

if __name__ == "__main__":
    Gui(page=page).run(title="E-Commerce Dashboard")
