import random
import numpy as np
from PIL import Image, ImageFont, ImageDraw

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def helper_watermark(image_name):
    im = Image.fromarray(image_name)
    initial_coordinate = 15
    for j in range(6):
        sentance = ""
        for i in range(2):
            sentance = sentance +" "+ random_line('cracklib-small')
        font_type = ImageFont.truetype('/usr/share/fonts/AkaashNormal.ttf', random.randint(18,36))
        draw = ImageDraw.Draw(im)
        draw.text((15,initial_coordinate),sentance,font=font_type,fill=(0))
        initial_coordinate = initial_coordinate+40
    im.show()
    return np.asarray(im)
    # return im

def load_data(train_path="train/*", test_path="test/*"):
    import glob
    import numpy as np
    filelist_train = glob.glob(train_path)
    filelist_test = glob.glob(test_path)

    import cv2
    x_train = np.array([np.array(cv2.imread(fname, 0)) for fname in filelist_train])
    x_test = np.array([np.array(cv2.imread(fname, 0)) for fname in filelist_test])
    return x_train, x_test

x_train,x_test = load_data()

def add_water_mark(data):
    noisy = np.array([helper_watermark(i) for i in data])
    return noisy
        
noisy_x_train = add_water_mark(x_train)
noisy_x_test = add_water_mark(x_test)