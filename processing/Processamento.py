import PIL
from PIL import Image

def load_image(caminho_img):
    image = Image.open(caminho_img)
    return image


def img_resize(image, width, height ):
    img_resize = image.resize((width, height))
    return img_resize
