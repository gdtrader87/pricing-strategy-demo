"""
A minimal Panel dashboard example demonstrating how to apply a Material
design theme. This script uses Panel to create a simple scatter plot from a
synthetic dataset. The Material design theme is applied by passing
`design='material'` to `pn.extension()`. When run with `panel serve`,
the resulting dashboard will have a polished Material aesthetic.

To view the dashboard, install the required libraries (panel, hvplot,
pandas, numpy) and run:

    panel serve panutoreload
    

Then open the provided local URL in your web browser.
"""

import pandas as pd
import numpy as np

try:
    import panel as pn
    import hvplot.pandas  # noqa: F401 to register hvplot on DataFrame
except ImportError as e:
    raise ImportError(
        "This example requires the 'panel' and 'hvplot' libraries. "
        "Install them with 'pip install panel hvplot'."
    ) from e


def build_dashboard() -> pn.Column:
    """
    Build and return a simple Panel dashboard using a Material design theme.

    The dashboard consists of a header and a scatter plot of synthetic data.
    """
    # Apply Material design theme
    pn.extension(design="material")

    # Generate synthetic data
    n_points = 100
    rng = np.random.default_rng(0)
    x = rng.normal(loc=0, scale=1, size=n_points)
    y = 2 * x + rng.normal(scale=0.5, size=n_points)
    df = pd.DataFrame({"x": x, "y": y})

    # Create scatter plot using hvplot
    scatter = df.hvplot.scatter(x="x", y="y", title="Synthetic Scatter Plot", xlabel="X", ylabel="Y")

    # Assemble dashboard layout
    header = pn.pane.Markdown("## Material Theme Dashboard", sizing_mode="stretch_width")
    return pn.Column(header, scatter, sizing_mode="stretch_width")


# When run with `panel serve`, Panel looks for objects marked as servable
# and displays them. Calling build_dashboard() here registers the dashboard.
dashboard = build_dashboard()
dashboard.servable()

