
from MovingShapes import Circle, Square, Diamond, Frame

frame = Frame()
shape = Square(frame, 30)
shape.goto_curr_xy()
#shape1.move_tick()

while True:
    frame.graphics_update()
    shape.goto_curr_xy()
    shape.move_tick()