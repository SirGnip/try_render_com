import pandas as pd
import panel as pn

pn.extension("tabulator")

hdr = pn.pane.Markdown("## Hello world")
btn = pn.widgets.Button(name="Refresh", button_type="success")
df = pd.DataFrame([('foo', 99), ('bar', 42)], columns=['name', 'va'])
table = pn.widgets.Tabulator(df)
def on_click(e):
    print("clicked button", e)
btn.on_click(on_click)

pn.layout.Column(
    hdr,
    btn,
    table,
).servable()
