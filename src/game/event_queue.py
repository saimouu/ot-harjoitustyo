import pygame


class EventQueue:
    def __init__(self):
        pass

    def get(self):
        return pygame.event.get()
