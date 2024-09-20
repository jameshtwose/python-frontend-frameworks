from bowtie import App, command
from bowtie.visual import Plotly
from bowtie.control import Slider
import numpy as np

app = App(sidebar=True)
chart = Plotly()
slider = Slider(minimum=1, maximum=10, start=5, step=0.1)

app.add_sidebar(slider)
app.add(chart)


@app.subscribe(slider.on_change)
def plot_sine(freq):
    t = np.linspace(0, 10, 100)
    chart.do_all(
        {
            "data": [
                {
                    "type": "scatter",
                    "mode": "lines+markers",
                    "x": t,
                    "y": np.sin(freq * t),
                }
            ]
        }
    )


@command
def main():
    return app
