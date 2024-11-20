import random
import pandas as pd
import panel as pn

pn.extension("tabulator")

hdr = pn.pane.Markdown("## Hello world")
btn = pn.widgets.Button(name="Refresh", button_type="success")
df = pd.DataFrame([('foo', 99), ('bar', 42)], columns=['name', 'va'])
table = pn.widgets.Tabulator(df)

def make_df():
    names = ("foo", "bar", "zip", "linux", "bob", "mary")
    rows = []
    for i in range(random.randint(2, 8)):
        rows.append([random.choice(names), random.randint(1, 99)])
    return pd.DataFrame(rows, columns=["name", "val"])

def on_click(e):
    print("clicked button", e)
    table.value = make_df()
btn.on_click(on_click)

pn.layout.Column(
    hdr,
    btn,
    table,
).servable()
