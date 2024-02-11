from sprite_object import *
from npc import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/textures/static_sprite/'
        self.anim_sprite_path = 'resources/textures/animated_sprite/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_position = {}

        # sprite map

        # add_sprite(SpriteObject(game))
        # add_sprite(AnimatedSprite(game))

        # npc map

        # right room
        add_npc(NPC(game, pos=(2, 12)))
        add_npc(NPC(game, pos=(3, 13)))

        # left room
        add_npc(NPC(game, pos=(3, 3)))
        add_npc(NPC(game, pos=(3, 4)))
        # near left room
        add_npc(NPC(game, pos=(7, 3)))
        add_npc(NPC(game, pos=(9.5, 4.5)))

        # main hall
        add_npc(NPC(game, pos=(10, 8.5)))
        add_npc(NPC(game, pos=(16, 7.5)))
        add_npc(NPC(game, pos=(20, 8.5)))

        #big left room
        add_npc(NPC(game, pos=(13, 2)))
        add_npc(NPC(game, pos=(16, 3)))


    def update(self):
        self.npc_position = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
