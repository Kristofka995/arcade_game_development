import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        map = arcade.read_tmx("my_maps/platformer-map.tmx")
        self.talaj = arcade.tilemap.process_layer(map, "Talaj")
        self.dobozok = arcade.tilemap.process_layer(map, "dobozok")

    def on_draw(self):
        arcade.start_render()
        self.talaj.draw()
        self.dobozok.draw()
    def on_update(self, delta_time: float):
        pass


win = GameWindow(2100, 700, "Game Window")
arcade.run()