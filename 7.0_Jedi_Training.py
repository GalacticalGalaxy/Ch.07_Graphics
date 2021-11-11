#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
SW = 500
SH = 400

arcade.open_window(SW, SH, "Jedi Training", True)
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for i in range(0,SW+1,20):
    arcade.draw_line(i, 0, i, 400, arcade.color.BLACK, 2)
    arcade.draw_line(0, i, 600, i, arcade.color.BLACK, 2)

arcade.draw_rectangle_filled(50,370,60,20, arcade.color.PHLOX)
arcade.draw_rectangle_filled(200,260,40,20, arcade.color.BLUSH, -45)
arcade.draw_point(300,300,(0,0,0),5)
arcade.draw_line(80,20,120,60,(arcade.color.BLUE), 1)
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_rectangle_filled(460,10,5,5, arcade.color.RED)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)
arcade.draw_text("I love you. I know.", 20, 155, arcade.color.BRICK_RED, 20)
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)










arcade.finish_render()
arcade.run()
