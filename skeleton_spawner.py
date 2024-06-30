from skeleton import Skeleton


class SkeletonSpawner:
    def __init__(self, all_sprites, drevorubac):
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
        new_skeleton = Skeleton()
        self.all_sprites.add(new_skeleton)

        # Adding to the 3rd last index (instead of using append)
        #index = min(-3, -len(self.drevorubac.all_skeletons) - 1)
        self.drevorubac.all_skeletons.append(new_skeleton)
