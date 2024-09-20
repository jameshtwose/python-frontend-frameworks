from shiny.express import input, render, ui
from shinywidgets import render_plotly
import requests
import pandas as pd
import plotly.express as px

ui.page_opts(
    title="E-Commerce Dashboard",
    fillable=True,
    sidebar_state="collapsed",
)


def load_user_data(limit: int = 10, offset: int = 0):
    response = requests.get(
        "http://localhost:8080/users",
        params={"limit": limit, "offset": offset},
    )
    return pd.DataFrame(response.json())


with ui.sidebar():
    ui.input_slider(
        id="limit",
        label="Number of records",
        min=10,
        max=10000,
        value=100,
        step=10,
    )
    ui.input_slider(
        id="offset",
        label="Number of records to skip",
        min=0,
        max=10000,
        value=0,
    )

with ui.card(full_screen=True):

    @render.data_frame
    def show_data():
        df = load_user_data(limit=input.limit(), offset=input.offset())
        return df


with ui.card(full_screen=True):
    with ui.layout_columns():

        @render_plotly
        def show_pie_chart():
            df = load_user_data(limit=input.limit(), offset=input.offset())
            fig = px.pie(
                df,
                names="country",
                title="User Type Distribution",
                # labels={"country": "Country"},
            )
            fig.update_traces(textposition='inside')
            fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
            return fig

        @render_plotly
        def show_density_plot():
            df = load_user_data(limit=input.limit(), offset=input.offset())
            return px.histogram(
                df,
                x="days_since_last_login",
                color="gender",
                title="Days Since Last Login Density Plot",
                marginal="box",
                nbins=1000,
                color_discrete_sequence=["#636EFA", "#EF553B"],
            )
