import plotly.express as px
import pandas as pd
import panel as pn
import requests

pn.extension("plotly", design="material", sizing_mode="stretch_width")


# Load data
@pn.cache
def load_user_data(limit: int = 10, offset: int = 0):
    response = requests.get(
        "http://localhost:8080/users",
        params={"limit": limit, "offset": offset},
    )
    return pd.DataFrame(response.json())


# Slider widgets
limit_input = pn.widgets.IntSlider(
    name="Number of records", start=10, end=10000, value=100, step=10
)
offset_input = pn.widgets.IntSlider(
    name="Number of records to skip", start=0, end=10000, value=0, step=10
)
# Table
btable = pn.Row(
    pn.bind(load_user_data, limit_input, offset_input),
    height=500,
)

# having issues binding the data to the charts
df = load_user_data()

bpie = pn.pane.Plotly(
    px.pie(
        df,
        names="country",
        title="User Type Distribution",
    ),
    height=500,
)

bdensity = pn.pane.Plotly(
    px.histogram(
        df,
        x="days_since_last_login",
        color="gender",
        title="Days Since Last Login Density Plot",
        marginal="box",
        nbins=1000,
        color_discrete_sequence=["#636EFA", "#EF553B"],
    ),
    height=500,
)

# Dashboard
pn.template.FastListTemplate(
    site="E-commerce",
    title="Dashboard",
    main=[limit_input, offset_input, btable, bpie, bdensity],
).servable()
