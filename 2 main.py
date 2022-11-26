import numpy as np
from PIL import Image, ImageDraw


def find_brightest_spot_v2(img_path, precision=1):
    """
    green rectangle is the darkest area
    red rectangle is the lightest area
    uses RGB format, you can also use BGR
    precision: the pixel step through which the brightness will be calculated
    """
    im = Image.open(img_path)#.convert('L')
    im_arr = np.asarray(im)
    dict_avg = {}
    sum_rgb = 0
    count = 0
    for height_x in range(49, im.size[1] - 49, precision):
        for width_y in range(49, im.size[0] - 49, precision):
            for height in range(height_x - 50, height_x + 50):
                for width in range(width_y - 49, width_y + 49):
                    sum_rgb += sum(im_arr[height][width])
                    count += 1
            dict_avg[(width_y, height_x, count)] = sum_rgb / count
            sum_rgb = 0
            count = 0
    max_key = max(dict_avg, key=dict_avg.get)
    min_key = min(dict_avg, key=dict_avg.get)
    img = Image.open(img_path)
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((max_key[0] - 49, max_key[1] - 49, max_key[0] + 49, max_key[1] + 49), outline=(255, 0, 0), width=1)
    idraw.rectangle((min_key[0] - 49, min_key[1] - 49, min_key[0] + 49, min_key[1] + 49), outline=(0, 255, 0), width=1)
    img.save('change.png')
    img.show()


find_brightest_spot_v2('img2.png', 10)
