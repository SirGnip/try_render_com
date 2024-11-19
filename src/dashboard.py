import panel as pn

pn.extension()

hdr = pn.pane.Markdown("## Hello world")
btn = pn.widgets.Button(name="Refresh", button_type="success")

pn.layout.Column(
    hdr,
    btn
).servable()
