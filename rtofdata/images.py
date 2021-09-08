import drawSvg as draw
from rtofdata.specification.data import Specification


def create_flow_svg(spec: Specification):
    d = draw.Drawing(200, 100, displayInline=False)

    # Draw a rectangle
    r = draw.Rectangle(0, 0, 40, 50, fill='#1248ff')
    r.appendTitle("Our first rectangle")  # Add a tooltip
    d.append(r)

    d.saveSvg('output/example.svg')


if __name__ == "__main__":
    create_flow_svg(1)