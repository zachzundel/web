from tempfile import NamedTemporaryFile

from django.http import HttpResponse
from django.template import Context, loader

from PIL import Image, ImageDraw, ImageFont, ImageOps
from svgutils.compose import SVG, Figure, Line
from svgutils.transform import fromstring

AVATAR_BASE = 'assets/other/avatars/'
COMPONENT_BASE = 'assets/v2/images/avatar/'


def build_component_base(component_type='cardigan', width=899, height=1415, primary_color='#18C708',
                         secondary_color='#FFF', border_color='#333', stroke='#333', opacity='.15'):
    # config = {'width': width, 'height': height}
    return {
        'width': width,
        'height': height,
        'primary_color': primary_color,
        'secondary_color': secondary_color,
        'stroke': stroke,
        'opacity': opacity,
        'border_color': border_color,
    }


def get_svg_from_template(svg_template_type='cardigan'):
    context = {}
    svg_template_type = svg_template_type.lower()

    if svg_template_type == 'cardigan':
        context = build_component_base()

    component_template = loader.get_template(f'{svg_template_type}_base.txt')
    return component_template.render(context)


def build_avatar_component(path, icon_size=None, avatar_size=None):
    print('path:', path)
    icon_size = icon_size or (215, 215)
    avatar_component_size = avatar_size or (899.2, 1415.7)
    scale_factor = icon_size[1] / avatar_component_size[1]
    x_to_center = (icon_size[0] / 2) - ((avatar_component_size[0] * scale_factor) / 2)
    print('SCALE_FACTOR: ', scale_factor)
    print('x_to_center: ', x_to_center)
    print('avatar_component_size', avatar_component_size)
    print('icon_size:', icon_size)
    svg = SVG(f'{COMPONENT_BASE}{path}').scale(scale_factor).move(x_to_center, 0)
    print('SVG: ', svg)
    return svg


def build_temporary_avatar_component(icon_size=None, avatar_size=None, primary_color='#18C708',
                                     secondary_color='#FFF', component_type='cardigan'):
    icon_size = icon_size or (215, 215)
    avatar_component_size = avatar_size or (899.2, 1415.7)
    scale_factor = icon_size[1] / avatar_component_size[1]
    x_to_center = (icon_size[0] / 2) - ((avatar_component_size[0] * scale_factor) / 2)
    with NamedTemporaryFile(mode='w+') as tmp:
        svg_data = get_svg_from_template(component_type)
        print('SVG data', svg_data, str(svg_data))
        tmp.write(str(svg_data))
        tmp.seek(0)
        svg = SVG(tmp.name).scale(scale_factor).move(x_to_center, 0)
    return svg


def build_avatar_svg(svg_path='test.svg', line_color='#781623', icon_size=None, avatar_size=None):
    print('in build avatar svg')
    icon_size = icon_size or (215, 215)
    icon_width = icon_size[0]
    icon_height = icon_size[1]

    print('before final avatar')
    final_avatar = Figure(
        icon_width,
        icon_height,
        # Background
        Line(
            [(0, icon_height / 2), (icon_width, icon_height / 2)],
            width=f'{icon_height}px',
            color=line_color),
        # Other layers
        build_temporary_avatar_component(),
        # build_avatar_component('Clothing/cardigan-43B9F9.svg', icon_size),
        build_avatar_component('Ears/0-3F2918.svg', icon_size),
        build_avatar_component('Head/0-3F2918.svg', icon_size),
        build_avatar_component('Eyes/0.svg', icon_size),
        build_avatar_component('Mouth/0.svg', icon_size),
        build_avatar_component('Nose/0.svg', icon_size),
    )
    print('after final avatar: ', final_avatar)
    result_path = f'{COMPONENT_BASE}{svg_path}'
    print('result_path:', result_path)
    final_avatar.save(result_path)
    return result_path


def avatar(request):
    """Serve an avatar."""
    result_path = build_avatar_svg()
    with open(result_path) as file:
        response = HttpResponse(file, content_type='image/svg+xml')
    # os.remove(result_path)
    return response


def handle_avatar(request):
    preset_id = request.GET.get('preset_id', '')
    head = request.GET.get('head', '')
    clothing = request.GET.get('clothing', '')
    eyes = request.GET.get('eyes', '')
    mouth = request.GET.get('mouth', '')
    nose = request.GET.get('nose', '')


def get_svg_component(request):
    pass


def live_avatar_preview(request):
    avatar = handle_avatar(request)


def template_svg(svg_template_type='cardigan'):
    # response = HttpResponse(content_type='image/svg+xml')
    # response['Content-Disposition'] = 'attachment; filename="test.svg"'
    context = {}

    svg_template_type = svg_template_type.lower()

    if svg_template_type == 'cardigan':
        context = build_component_base()

    # avatar_data = (
    #     ('First row', 'Foo', 'Bar', 'Baz'),
    #     ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
    # )

    component_template = loader.get_template(f'{svg_template_type}_base.txt')
    # component_context = Context({
    #     'data': avatar_data,
    # })

    # response.write(t.render(c))
    # return response
    return component_template.render(context)
