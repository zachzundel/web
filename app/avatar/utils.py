import svgwrite


class AvatarItem:
    """Define the setup and utility of an AvatarItem."""

    def __init__(self, width=899, height=1415, **kwargs):
        """Define initial data for the avatar item."""
        self.width = width
        self.height = height
        self.xmlns = kwargs.get('xmlns', 'http://www.w3.org/2000/svg')
        self.svg_base = f'<svg width="{self.width}" height="{self.height} xmlns="{self.xmlns}">'

    def get_base_svg(self, input):
        self.svg = f'{self.svg_base}{input}</svg>'


def build_svg(item_type, width=899, height=1415, fill=''):
    """Build the SVG."""
    if item_type == 'mustache':
        # '<svg width="899" height="1415" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path d="M609.3 811.7c-16-35.4-51.2-58.2-90-58.2h-35.5c-5.8 13.1-18.9 22.3-34.2 22.3-15.3 0-28.4-9.2-34.2-22.3h-35.6c-40.6 0-77 24.8-91.9 62.5l-21.5 80.4c-2.7 10.1 10.4 16.7 16.8 8.5l39-56.9c13.7-20 36.4-32 60.7-32h135.3c20 0 38.9 8.7 52 23.7l48.1 55.5c5.8 6.7 16.5.8 14.1-7.7l-21-71.6-2.1-4.2z" stroke="#333" stroke-width="14.716" fill="#000" fill-rule="nonzero"/><path d="M147.7 540.5h603.7V782H147.7z"/></g></svg>'
        return ''

def build_svg(svg_name='temp.svg', width=899, height=1415, debug=False):
    dwg = svgwrite.Drawing(svg_name, (width, height), debug=debug)
    group = dwg.g(fill='none', fill_rule='evenodd')
    path = group.add(
        dwg.path(
            d='M609.3 811.7c-16-35.4-51.2-58.2-90-58.2h-35.5c-5.8 13.1-18.9 22.3-34.2 22.3-15.3 0-28.4-9.2-34.2-22.3h-35.6c-40.6 0-77 24.8-91.9 62.5l-21.5 80.4c-2.7 10.1 10.4 16.7 16.8 8.5l39-56.9c13.7-20 36.4-32 60.7-32h135.3c20 0 38.9 8.7 52 23.7l48.1 55.5c5.8 6.7 16.5.8 14.1-7.7l-21-71.6-2.1-4.2z',
            stroke='#333',
            stroke_width="14.716",
            fill="#000",
            fill_rule="nonzero"
        ),
        dwg.path(d='M147.7 540.5h603.7V782H147.7z'),
    )
    return path


def hyperlink(name):
    dwg = svgwrite.Drawing(name, (200, 200), debug=True)
    # use the hyperlink element
    link = dwg.add(dwg.a('http://www.w3.org'))
    link.add(dwg.ellipse(center=(100, 50), r=(50, 25), fill='red'))
    dwg.save(pretty=True)
