import mesop as me
import mesop.labs as mel
import requests
import pandas as pd
import plotly.express as px
import plotly.offline


def load_user_data(limit: int = 10, offset: int = 0):
    response = requests.get(
        "http://localhost:8080/users",
        params={"limit": limit, "offset": offset},
    )
    return pd.DataFrame(response.json())


@me.stateclass
class State:
    initial_input_value: str = "50.0"
    initial_slider_value: float = 50.0
    slider_value: float = 50.0


def on_value_change(event: me.SliderValueChangeEvent):
    state = me.state(State)
    state.slider_value = event.value
    state.initial_input_value = str(state.slider_value)


@me.page(path="/")
def app():
    state = me.state(State)
    me.html(
        '<header><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></header>',
        mode="sandboxed",
    )
    me.html("<h1>E-commerce Dashboard</h1>")
    me.html("<h2>Load data</h2>")
    me.text("Number of records")
    me.slider(
        min=10,
        max=1000,
        on_value_change=on_value_change,
        value=state.initial_slider_value,
    )
    data = load_user_data(limit=state.slider_value)
    with me.box(
        style=me.Style(
            padding=me.Padding.all(10), height=500, overflow="auto"
        )
    ):
        me.table(
            data,
            header=me.TableHeader(sticky=True),
        )
    with me.box():
        pie_fig = px.pie(
            data, names="country", title="User Type Distribution"
        )
        pie_div = plotly.offline.plot(
            pie_fig, include_plotlyjs=False, output_type="div"
        )
        me.html("<h3>Pie chart of country</h3>")
        me.html(pie_div, mode="sandboxed")
