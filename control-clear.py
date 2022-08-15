import screen_brightness_control as control
import time

wait = 0
while len(control.list_monitors()) < 2:
    time.sleep(1)
    if wait < 30: wait += 1
    else: exit(0)

last = control.get_brightness(display=0)

while True:
    current = control.get_brightness(display=0)
    if current != last:
        last = current
        for d in control.list_monitors(): control.set_brightness(current, d)
        time.sleep(0.01)