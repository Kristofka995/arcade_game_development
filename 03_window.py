import arcade


class GameWindow(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title, resizable=True)
        self.center_window()

    def on_draw(self):
                #circle
        arcade.start_render()
        arcade.draw_circle_filled(240, 360, 30, arcade.color.BLUE)
        arcade.draw_circle_outline(340, 360, 30, arcade.color.BUFF)

                #ellipse
        arcade.draw_ellipse_filled(100, 100, 50, 80, arcade.color.AQUA)
        arcade.draw_ellipse_outline(200, 100, 50, 80, arcade.color.AMETHYST)

                #rectangle
        arcade.draw_rectangle_filled(300, 100, 50, 50, arcade.color.RASPBERRY_GLACE)
        arcade.draw_rectangle_outline(400, 100, 50, 100, arcade.color.YANKEES_BLUE, 4)

                #text-szöveg
        arcade.draw_text("Kóder Klub", 20, 720-80, arcade.color.ALMOND, 24)
                #arc-iv
        arcade.draw_arc_filled(640, 720-80, 120, 120, arcade.color.YELLOW_GREEN, 0, 90)
        arcade.draw_arc_filled(1040, 720-80, 120, 120, arcade.color.GLITTER, 0, 180)

                #triangle
        arcade.draw_polygon_outline([[0, 0], [50, 0], [25, 50]], arcade.color.RAZZMIC_BERRY)

            #polygon
        arcade.draw_polygon_outline([[640, 360],
                                     [640+50, 360],
                                     [640+75, 360+25],
                                     [640+25, 360+50],
                                     [640-25, 360+25]], arcade.color.EARTH_YELLOW)

win=GameWindow(1280, 720, "Game Window")
arcade.run()