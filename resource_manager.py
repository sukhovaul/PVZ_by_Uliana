import pygame as pg
import pytmx
from settings import*

class ResourceManager:
    def __init__(self):
        self.maps = {}

    def load_map(self, map_name, file_path):
        self.maps[map_name] = pytmx.load_pygame(file_path)
        return self.maps[map_name]