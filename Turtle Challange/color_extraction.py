import colorgram


def extract_color():
    rgb_colors = []
    colors = colorgram.extract('image.webp', 30)

    for color in colors:
        r = color.rgb.r / 255
        g = color.rgb.g / 255
        b = color.rgb.b / 255
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors
