# Speichert die Daten eines Tile-Typs:
import pygame


class ObjectType(object):
    # Im Konstruktor speichern wir den Namen
    # und erstellen das Rect (den Bereich) dieses Typs auf der Tileset-Grafik.
    def __init__(self, name, start_x, start_y, width, height):
        self.name = name
        self.rect = pygame.rect.Rect(start_x, start_y, width, height)