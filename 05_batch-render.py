import arcade


class GameWindow(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title, resizable=True)
        self.center_window()
        self.batch=arcade.ShapeElementList()


        ellipse1=arcade.create_ellipse_filled(440, 360, 50, 50, arcade.color.GOLDEN_BROWN)
        ellipse2=arcade.create_ellipse_outline(640, 360, 50, 50, arcade.color.RAJAH)
        ellipse3=arcade.create_ellipse_filled_with_colors(840, 360, 50, 80, arcade.color.GOLDEN_BROWN, arcade.color.UP_MAROON)


        triangle = arcade.create_polygon([[0, 0], [100, 0], [50, 100]], arcade.color.EGYPTIAN_BLUE)


        rect=arcade.create_rectangle_filled(100,360,100,150, arcade.color.GREEN)

        self.batch.append(ellipse1)
        self.batch.append(ellipse2)
        self.batch.append(ellipse3)
        self.batch.append(triangle)
        self.batch.append(rect)


    def on_draw(self):
        arcade.start_render()
        self.batch.draw()


win=GameWindow(1280, 720, "Game Window")
arcade.run()