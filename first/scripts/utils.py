import pygame
import pathlib
from pathlib import Path
import os


ROOT = pathlib.Path.cwd() 
BASE_IMAGE_PATH = 'data/images'
def load_image(path):
    img = pygame.image.load(Path(ROOT,BASE_IMAGE_PATH, path))
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(Path(BASE_IMAGE_PATH, path)):
        images.append(load_image(Path(path, img_name)))
    return images