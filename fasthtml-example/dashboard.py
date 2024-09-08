from fasthtml.common import (
    FastHTML,
    serve,
    Title,
    Div,
    H1,
    P,
    Table,
    Tr,
    Th,
    Td,
    Style,
    Link,
    to_xml,
    Script,
    Iframe,
    Input,
)
import plotly.express as px
import plotly
import requests
from fh_plotly import plotly_headers, plotly2fasthtml

# css = Link(
#     rel="stylesheet",
#     href="public/style.css",
#     type="text/css",
# )
app = FastHTML(hdrs=plotly_headers)

@app.get("/")
def home():
    slider_input = Input(
        type="range",
        min="0",
        max="100",
        value="50",
        class_="slider",
        id="myRange",
    )
    
    response = requests.get(
        "http://localhost:8080/users", params={"limit": 100, "offset": 0}
    )
    data = response.json()

    pie_fig = px.pie(
        data,
        values="social_nb_followers",
        names="country",
        title="Followers by Country",
    )

    density_fig = px.histogram(
        data,
        x="days_since_last_login",
        color="gender",
        title="Days Since Last Login Density Plot",
        marginal="box",
        nbins=1000,
        color_discrete_sequence=["#636EFA", "#EF553B"],
    )
    
    return (
        Div(H1("E commerce Dashboard"), P("Welcome to the E commerce Dashboard")),
        Div(Style(
                """
                    #mydiv {
                        height: 400px;
                        width: 100%;
                        background-color: #f1f1f1;
                        overflow: auto;
                    }
                """
            ),
            Table(
                Tr(
                    Th("User ID"),
                    Th("Country"),
                    Th("Language"),
                    Th("Followers"),
                    Th("Follows"),
                    Th("Products Liked"),
                    Th("Products Listed"),
                    Th("Products Sold"),
                    Th("Products Wished"),
                    Th("Products Bought"),
                    Th("Gender"),
                    Th("Civility Title"),
                    Th("Has Any App"),
                    Th("Has Android App"),
                    Th("Has iOS App"),
                    Th("Has Profile Picture"),
                    Th("Days Since Last Login"),
                    Th("Seniority"),
                    Th("Country Code"),
                ),
                *[
                    Tr(
                        Td(user["identifier_hash"]),
                        Td(user["country"]),
                        Td(user["language"]),
                        Td(user["social_nb_followers"]),
                        Td(user["social_nb_follows"]),
                        Td(user["social_products_liked"]),
                        Td(user["products_listed"]),
                        Td(user["products_sold"]),
                        Td(user["products_wished"]),
                        Td(user["products_bought"]),
                        Td(user["gender"]),
                        Td(user["civility_title"]),
                        Td(user["has_any_app"]),
                        Td(user["has_android_app"]),
                        Td(user["has_ios_app"]),
                        Td(user["has_profile_picture"]),
                        Td(user["days_since_last_login"]),
                        Td(user["seniority"]),
                        Td(user["country_code"]),
                    )
                    for user in data
                ]
            ),
        id="mydiv"),
        plotly2fasthtml(pie_fig),
        plotly2fasthtml(density_fig),
    )


serve()
