import pygame
import pathlib
from pathlib import Path
ROOT = pathlib.Path.cwd() 
BASE_IMAGE_PATH = 'data/images'
def load_image(path):
    img = pygame.image.load(Path(ROOT,BASE_IMAGE_PATH, path))
    img.set_colorkey((0, 0, 0))
    return img