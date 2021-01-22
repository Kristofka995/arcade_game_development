import arcade

MOVEMENT_SPEED = 12
JUMP_SPEED = 50
GRAVITY = 5


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_HALF_WIDTH = WINDOW_WIDTH / 2
WINDOW_ZERO = 0

MAP_WIDTH = 31*70
MAP_HEIGHT = 10*70
TITLE_WIDTH = 70

class GameWindow(arcade.Window):
    def __init__(self, width, height, title, resizable=True):
        super().__init__(width, height, title, resizable=True )
        self.center_window()

        map = arcade.read_tmx("my_maps/platformer-map.tmx")
        self.talaj = arcade.tilemap.process_layer(map, "Talaj", use_spatial_hash=True)
        self.dobozok = arcade.tilemap.process_layer(map, "dobozok", use_spatial_hash=True)
        self.szalag = arcade.tilemap.process_layer(map,"szalag", use_spatial_hash=True)

        self.player = arcade.Sprite("my_sprites/greene.png", center_x = 100, center_y=175 )

        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.talaj, gravity_constant=GRAVITY)


    def on_draw(self):
        arcade.start_render()
        self.talaj.draw()
        self.dobozok.draw()
        self.szalag.draw()
        self.player.draw()
        # if self.player.center_y < 0:
        #     arcade.draw_text("Meghaltál, de kapsz még egy esélyt! 2 életed maradt!", 250, 600, arcade.color.ANTI_FLASH_WHITE, 30)


    def on_update(self, delta_time: float):
        self.physics.update()
#following
        if self.player.center_x > WINDOW_HALF_WIDTH and self.player.center_x < MAP_WIDTH - TITLE_WIDTH -WINDOW_HALF_WIDTH:
            change_view = True
        else:
            change_view = False

        if change_view:# left, right, top,bottom
            arcade.set_viewport(self.player.center_x - WINDOW_HALF_WIDTH,
                                self.player.center_x + WINDOW_HALF_WIDTH, 0, WINDOW_HEIGHT)
        if self.player.center_y < 0:
             self.player.set_position(center_x=100, center_y=175)
        #     change_view = True
        # else:
        #     change_view= False
        #
        # if change_view:#left, right, top, bottom
        #     arcade.set_viewport(self.player.center_x - WINDOW_HALF_WIDTH,


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

        if symbol == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        if symbol == arcade.key.UP:
            if self.physics.can_jump():
                self.player.change_y = JUMP_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol== arcade.key.RIGHT:
            self.player.change_x = 0



win = GameWindow(1280, 700, "Game Window")
arcade.run()