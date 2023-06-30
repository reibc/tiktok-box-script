from ppadb.client import Client
from PIL import Image
import numpy
import time
import threading
import random
from multiprocessing import Process

def clicker(x, y):
    for i in range(1, 10): device.shell(f'input touchscreen tap {x} {y}')
    return

def box_clicker(device, x, y):
    
    for i in range(1, 3):
        device.shell(f'input touchscreen tap {x} {y}')
    return

def auto_tiktok(device, device_number):
    x = 496
    y = 828
    while True:
        white = True
        box_loop = True
        time.sleep(3.5)
        device.shell(f'input touchscreen tap 42 159')
        time.sleep(1)
        image = device.screencap()

        with open(f'screen{device_number}.png', 'wb') as f:
            f.write(image)

        image = Image.open(f'screen{device_number}.png')
        image = numpy.array(image, dtype=numpy.uint8)
        for pixel in list(image[y, x]):
            if pixel != 255:
                white = False
        if white:
            time.sleep(1)
            while box_loop:
                image = device.screencap()
                with open(f'screen{device_number}.png', 'wb') as f:
                    f.write(image)
                image = Image.open(f'screen{device_number}.png')
                image = numpy.array(image, dtype=numpy.uint8)
                for i in range(0, 3):
                    t = threading.Thread(target=box_clicker, args= (device, random.randrange(202, 420), random.randrange(859, 879)))
                    t.setDaemon(True)
                    t.start()
                main_thread = threading.current_thread()
                for t in threading.enumerate():
                    if t is main_thread:
                        continue
                    t.join()
                pixels = list(image[855, 358])
                if pixels[1] != 241:
                    box_loop = False
            time.sleep(0.5)
            device.shell('input keyevent 4')
            time.sleep(0.5)
        device.shell('input touchscreen swipe 350 800 350 187 300')

if __name__ == "__main__":
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()
    device = devices[0]
    Process1 = Process(target=auto_tiktok, args=(devices[1], 1))
    Process2 = Process(target=auto_tiktok, args=(devices[2], 2))
    Process1.start()
    Process2.start()