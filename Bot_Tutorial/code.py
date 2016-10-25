"""

All coordinates assume a screen resolution of 1920x1080, and Chrome
maximized with the Bookmarks Toolbar and uBlock Origin enabled.

x_pad=464
y_pad=242
Play area=x_pad+1, y_pad+1, x_pad+642, y_pad+481

"""


from PIL import ImageGrab
import os
import time


x_pad=464
y_pad=242

def screen_grab():
    box = (x_pad+1, y_pad+1, x_pad+642, y_pad+481)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screen_grab()


if __name__ == '__main__':
    main()
