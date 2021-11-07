from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

mc = MyCobot(PI_PORT, PI_BAUD)
mc.set_color(255, 255, 0)
print(PI_PORT)
print(PI_BAUD)