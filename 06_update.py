import arcade

class GameWindow(arcade.Window):
    def __init__(self, width, length, title):
        super().__init__(width, length, title)
        self.center_window()
        self.circle_x=640
        self.circle_y=360
        self.speed_x=300
        self.speed_y=300


    def on_draw(self):
        arcade.start_render()
        arcade.draw_ellipse_filled(self.circle_x, self.circle_y, 80, 80, arcade.color.AO)
        arcade.draw_ellipse_outline(self.circle_x, self.circle_y, 80, 80, arcade.color.YELLOW_ROSE)
        arcade.draw_text(f"x:{self.circle_x:.0f} - y:{self.circle_y:.0f}", 10, 720-20, arcade.color.WHITE, 16)


    def on_update(self, delta_time: float):
        self.circle_x +=self.speed_x * delta_time
        self.circle_y +=self.speed_y * delta_time


        if self.circle_x > 1280-40:
            self.circle_x=1280-40
            self.speed_x *= -1
        if self.circle_x < 0+40:
            self.circle_x=0+40
            self.speed_x *= -1
        if self.circle_y > 720-40:
            self.circle_y=720-40
            self.speed_y *= -1
        if self.circle_y <0+40:
            self.circle_y=0+40
            self.speed_y *= -1



win = GameWindow(1280, 720, "Game Window")
arcade.run()