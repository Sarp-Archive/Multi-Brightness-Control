# Multi Brightness Control - Clear version

import screen_brightness_control as sbc
import time

wait = 0
while len(sbc.list_monitors()) < 0:
    time.sleep(1)
    if wait < 30: wait += 1
    else: terminate(None)

last = sbc.get_brightness(display=0)

while True:
    current = sbc.get_brightness(display=0)
    if current != last:
        last = current
        for i in range(1, monitor_count): sbc.set_brightness(current, display=i)
        time.sleep(0.1)