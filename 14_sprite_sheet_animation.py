import arcade

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()
        self.guy=arcade.AnimatedTimeSprite()
        self.guy.textures= []


        for i in range(6):
            texture = arcade.load_texture("my_sprites/girl.png", x=i*256, y=0, width=256, height=256)
            self.guy.textures.append(texture)


        self.guy.center_x=640
        self.guy.center_y=360


    def on_draw(self):
        arcade.start_render()
        self.guy.draw()


    def on_update(self, delta_time: float):
        self.guy.update_animation()




win= GameWindow(1280, 720, "GameWindow")
arcade.run()