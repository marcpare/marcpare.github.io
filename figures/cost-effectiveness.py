
import plotly.express as px

template = "plotly_dark"

models = [
    "claude-3.7-sonnet",
    "llama-4-maverick",
    "qwq-32b",
    "deepseek-r1",
    "gpt-4o",
    "llama-4-scout",
    "gemini-2.0-flash-001",
    "gemma-3-27b-it",
]

f1s = [
    0.811,
    0.748,
    0.738,
    0.696,
    0.694,
    0.677,
    0.575,
    0.549,
]

cost = [
    15,
    0.85,
    0.2,
    2.18,
    10,
    0.45,
    0.4,
    0.2,
]

precisions = [
    0.79,
    0.675,
    0.702,
    0.618,
    0.614,
    0.715,
    0.495,
    0.461,
]

recalls = [
    0.833,
    0.839,
    0.778,
    0.798,
    0.798,
    0.643,
    0.687,
    0.676,
]




# set the y axis range to 0 to 1
fig = px.scatter(x=cost, y=f1s, template=template, labels={"x": "Cost ($ / M Output Tokens)", "y": "F1 Score"}, title="Data Discovery Cost Effectiveness")
fig.update_yaxes(range=[0, 1])
fig.update_layout(title_x=0.5)
fig.update_layout(font=dict(family="-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial"))

for x, y, label in zip(cost, f1s, models):
    fig.add_annotation(
        x=x,
        y=y,
        text=label,
        showarrow=False,
        textangle=45,
        font=dict(size=10, color="white"),
        xanchor="left",
        yanchor="top"
    )


if __name__ == "__main__":
    # Read the filename of the output image from the command line
    import sys
    output_filename = sys.argv[1]
    fig.write_image(output_filename, width=900)
