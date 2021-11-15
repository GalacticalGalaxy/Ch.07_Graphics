'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade

SH = 160
SW = SH
arcade.open_window(SW, SH, "Bryce Huey", True)
arcade.set_background_color(arcade.color.LIGHT_BLUE)
arcade.start_render()

#Back knocht------------------------------------------------------------
arcade.draw_rectangle_filled(5,5,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(5,15,10,10,arcade.color.GRAY_ASPARAGUS)
arcade.draw_rectangle_filled(5,25,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(15,5,10,10,arcade.color.GRAY_ASPARAGUS)
arcade.draw_rectangle_filled(15,15,10,10,arcade.color.GRAY_ASPARAGUS)
arcade.draw_rectangle_filled(15,25,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(25,5,10,10,arcade.color.GRAY_ASPARAGUS)
arcade.draw_rectangle_filled(25,15,10,10,arcade.color.DARK_GREEN)

#handal------------------------------------------------------------------
arcade.draw_rectangle_filled(25,25,10,10,arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(35,25,10,10,arcade.color.DARK_TAN)
arcade.draw_rectangle_filled(25,35,10,10,arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(35,35,10,10,arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(45,35,10,10,arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled(35,45,10,10,arcade.color.DARK_TAN)
arcade.draw_rectangle_filled(45,45,10,10,arcade.color.DARK_BROWN)

#Blue sperator thingy------------------------------------------------------
arcade.draw_rectangle_filled(45,55,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(45,65,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(45,75,10,10,arcade.color.DARK_CYAN)
arcade.draw_rectangle_filled(45,85,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(55,65,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(55,75,10,10,arcade.color.DARK_GREEN)

arcade.draw_rectangle_filled(35,65,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(35,75,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(35,85,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(35,95,10,10,arcade.color.DARK_CYAN)
arcade.draw_rectangle_filled(25,85,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(25,95,10,10,arcade.color.DARK_GREEN)

arcade.draw_rectangle_filled(55,45,10,10,arcade.color.DARK_CYAN)
arcade.draw_rectangle_filled(65,45,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(75,45,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(85,45,10,10,arcade.color.DARK_CYAN)
arcade.draw_rectangle_filled(65,55,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(75,55,10,10,arcade.color.DARK_GREEN)

arcade.draw_rectangle_filled(65,35,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(75,35,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(85,35,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(95,35,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(85,25,10,10,arcade.color.DARK_CYAN)
arcade.draw_rectangle_filled(95,25,10,10,arcade.color.DARK_GREEN)

arcade.draw_rectangle_filled(55,55,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(65,65,10,10,arcade.color.DARK_CYAN)
y = 0

#SWORD-------------------------------------------------------------------
# 55,75 to 125,155
for i in range(55, 126, 10):
    y = i+20
    arcade.draw_rectangle_filled(i   , y, 10, 10, arcade.color.DARK_GREEN)
    arcade.draw_rectangle_filled(i+10, y, 10, 10, arcade.color.CYAN)
    arcade.draw_rectangle_filled(i+20, y, 10, 10, arcade.color.LIGHT_CYAN)
    arcade.draw_rectangle_filled(i+20, y-10, 10, 10, arcade.color.CYAN)
    arcade.draw_rectangle_filled(i+20, y-20, 10, 10, arcade.color.DARK_GREEN)

arcade.draw_rectangle_filled(135,155,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(145,155,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(155,155,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(155,145,10,10,arcade.color.DARK_GREEN)
arcade.draw_rectangle_filled(155,135,10,10,arcade.color.DARK_GREEN)



arcade.finish_render()
arcade.run()