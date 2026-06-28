from pathlib import Path
import schemdraw
import schemdraw.elements as elm

outfile = Path(__file__).with_suffix(".svg")

d = schemdraw.Drawing()

d += elm.SourceV().label("5V")
d += elm.Resistor().label("300Ω")
d += elm.LED()
d += elm.Ground()

d.save(str(outfile))