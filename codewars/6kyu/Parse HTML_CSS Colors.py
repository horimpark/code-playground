def get_rgb(color):
    if len(color) == 3:
        r = int(color[0]*2, 16)
        g = int(color[1]*2, 16)
        b = int(color[2]*2, 16)
    else:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
    return {"r": r, "g": g, "b": b}

def parse_html_color(color):
    hex_value = color[1:] if color[0] == "#" else PRESET_COLORS[color.lower()][1:]
    res = get_rgb(hex_value)
    return res