import colorgram

IMAGE = "hirst spot picture.jpg"

class CollectColors:
    def __init__(self):
        self.rgb_colors = []

    def extract(self):
        colors = colorgram.extract(IMAGE, 30)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            if max(r, g, b) - min(r, g, b) > 10 or (r < 230 and g < 230 and b < 230):
                self.rgb_colors.append((r, g, b))
        return self.rgb_colors
