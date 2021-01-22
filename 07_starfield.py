import arcade
import random
fg_star_colors = [arcade.color.WHITE, arcade.color.BABY_BLUE, arcade.color.AQUA, arcade.color.BUFF, arcade.color.ALIZARIN_CRIMSON]
bg_star_colors = arcade.make_transparent_color(arcade.color.WHITE, 95)
#in line 3,4 we made the stars


def create_starfield(shape_list, color=arcade.color.WHITE, random_color=False):
    for i in range(200):
        x = random.randint(0, 1280)
        y = random.randint(0, 720)
        w = random.randint(1, 3)
        h = random.randint(1, 3)
        if random_color:
            color = random.choice(fg_star_colors)
        star = arcade.create_rectangle_filled(x, y, w, h, color)
        shape_list.append(star)


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        self.fg_stars1=arcade.ShapeElementList()

        create_starfield(self.fg_stars1, random_color=True)
        self.fg_stars2 = arcade.ShapeElementList()
        self.fg_stars2.center_y = 720
        create_starfield(self.fg_stars2, random_color=True)

        self.bg_stars1 = arcade.ShapeElementList()
        create_starfield(self.bg_stars1)

        self.bg_stars2=arcade.ShapeElementList()
        self.bg_stars2.center_y = 720
        create_starfield(self.bg_stars2)

        self.fg_star_speed = 150
        self.bg_star_speed = 100


    def on_draw(self):
        arcade.start_render()
        self.fg_stars1.draw()
        self.fg_stars2.draw()
        self.bg_stars1.draw()
        self.bg_stars2.draw()
        arcade.draw_triangle_filled(640, 20, 640+100, 20, 640+50, 100+20, arcade.color.BABY_BLUE)


    def move_stars(self, dt):
        self.fg_stars1.center_y -= self.fg_star_speed * dt
        self.fg_stars2.center_y -= self.fg_star_speed * dt
        self.bg_stars1.center_y -= self.bg_star_speed * dt
        self.bg_stars2.center_y -= self.bg_star_speed * dt


    def on_update(self, delta_time: float):
        self.move_stars(delta_time)


        if self.fg_stars1.center_y < -720:
            self.fg_stars1.center_y = 720
        if self.fg_stars2.center_y < -720:
            self.fg_stars2.center_y = 720
        if self.bg_stars1.center_y < -720:
            self.bg_stars1.center_y = 720
        if self.bg_stars2.center_y < -720:
            self.bg_stars2.center_y = 720






win = GameWindow(1280, 720, "starfield")
arcade.run()