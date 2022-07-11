from pynut import *

def get_choords(x, y):
    print("Now at: {}".format((x, y)))

with mouse.listener(on_move = get_coords) as listen:
    listen.join()
