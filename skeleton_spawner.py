from skeleton import Skeleton
from settings import Game_setting

class SkeletonSpawner:
    def __init__(self, all_sprites, drevorubac):
        self.max_skeletons = Game_setting().max_skeletons
        self.all_sprites = all_sprites
        self.drevorubac = drevorubac
        self.spawn_timer = 0
        self.spawn_interval = 2500

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_skeleton()
            self.spawn_timer = 0

    def spawn_skeleton(self):
        if len(self.all_sprites) <= self.max_skeletons:
            new_skeleton = Skeleton()

            self.all_sprites.add(new_skeleton)

            # This step is only so drevorubac and hit_sprite can be on the end of an sprite array
            # this sets the "highest" z-index for them, so every other entity will be under them
            self.all_sprites.remove(self.drevorubac.hit_sprite)
            self.all_sprites.remove(self.drevorubac)
            self.all_sprites.add(new_skeleton)
            self.all_sprites.add(self.drevorubac.hit_sprite)
            self.all_sprites.add(self.drevorubac)

            self.drevorubac.all_skeletons.append(new_skeleton)
