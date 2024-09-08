import streamlit as st
import plotly.express as px
import requests

st.set_page_config(
    page_title="E-commerce Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("E-commerce Dashboard")


# Load data
@st.cache_data(ttl=600)
def load_user_data(limit: int = 10, offset: int = 0):
    response = requests.get(
        "http://localhost:8080/users", params={"limit": limit, "offset": offset}
    )
    return response.json()


row_amount = st.slider(
    label="Number of records", min_value=10, max_value=10000, value=100, step=10
)
offset_amount = st.number_input(label="Number of records to skip", min_value=0, value=0)

data = load_user_data(limit=row_amount, offset=offset_amount)
st.dataframe(data)

# country pie chart
pie_fig = px.pie(data, names="country", title="User Type Distribution")
st.plotly_chart(pie_fig)

# amount of days since last login density plot
density_fig = px.histogram(
    data,
    x="days_since_last_login",
    color="gender",
    title="Days Since Last Login Density Plot",
    marginal="box",
    nbins=1000,
    color_discrete_sequence=["#636EFA", "#EF553B"],
)
st.plotly_chart(density_fig)

