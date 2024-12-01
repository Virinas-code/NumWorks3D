from libnumworks2.keys import KEY_BACKSPACE
import libnumworks2

libnumworks2.canvas.set_pixel(10, 10, (92, 164, 221))
libnumworks2.canvas.set_pixel(20, 10, (92, 164, 221))
print(libnumworks2.canvas.get_pixel(10, 10))
libnumworks2.canvas.draw_string("wow it works", 50, 50, (255, 0, 255), (0, 0, 0))

while True:
    print(libnumworks2.keydown(KEY_BACKSPACE))
    libnumworks2.canvas.draw_string("wow it works", 50, 50, (255, 0, 255), (0, 0, 0))
