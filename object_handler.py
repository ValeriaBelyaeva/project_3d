from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'D:/school/project2/textures/static_sprite/'
        self.anim_sprite_path = 'D:/school/project2/textures/animated_sprite/'
        add_sprite = self.add_sprite

        # sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)