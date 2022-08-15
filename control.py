# Multi Brightness Control
# Set brightness values for all monitors
# Created by Segilmez06 - sarpegilmez.com

from infi.systray import SysTrayIcon
import screen_brightness_control as sbc
import time
import os

def terminate(systray): os.kill(os.getpid(), 9) # Terminate function
def func_no(systray): pass # Empty function

wait = 0
monitor_count = len(sbc.list_monitors())
while monitor_count < 0: # Wait for other monitors to be connected
    time.sleep(1)
    if wait < 30: # Wait until 30 failed attempts
        monitor_count = len(sbc.list_monitors())
        wait += 1
    else: terminate(None) # No reason to waste system resources if there is no external monitor connected

last = sbc.get_brightness(display=0) # Set current brightness as last value

# Extract icon to file
img = bytearray(b"\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00 \x00\xb2\x01\x00\x00\x16\x00\x00\x00\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x03\x00\x00\x00(-\x0fS\x00\x00\x00\x01sRGB\x01\xd9\xc9,\x7f\x00\x00\x00\tpHYs\x00\x00\x0eM\x00\x00\x0eM\x01F\xd5h\t\x00\x00\x00\x8aPLTE\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf67h\x8d\x00\x00\x00.tRNS\x00\x8fa\x9dk\xa8C\\\x93\xedxW\xec0i\xdf\xff\xd7\xfb\xf9D\xd0\xb9]\xfc\xfar\x88>\xf4\xeeL\xb3\x907\xe6\xd9)[&\x89\xd3\xcf}q~\x0f\x08\x003\x00\x00\x00\x87IDATx\x9cm\x8f\xd9\x12\x820\x0cEc\x13[T\xd0\xaa\xb8\xa2\x82\x0b\xa0\xa8\xff\xff{\x86\xa6\xad\xe3\x8c\xe7)\xf7L\'\xb9\x05\x10\x06\n~A\xfa\xceC\x1d\x84I\x9c\xd0#6\xe3\t\xe74\x03o\xa63k\xe71\x03\xa8\x85e\x96y\xdc\xb2\xb2\x8e\xb5\xdcC\xdclE\xec\xf6\x88\x05(\xa2\xc3Q\xc4\xa9$2\xeeU%\xe2\x1cw\\\xae}\xbe\xd5!7i{\x7ft\xcf\xb6\xef#\x99\xef\xbfJ\xdf\x90I\xb2P]\xbf\xff\x7f\xceQ\x18?|\x00\x8e\x17\x07\x8d\xd3\xff\x95\x90\x00\x00\x00\x00IEND\xaeB`\x82")
with open("icon.ico", "wb") as image:
    image.write(img)

menu_options = (("Detected: " + str(monitor_count), None, func_no),) # Add connected monitor count as menu item

systray = SysTrayIcon("icon.ico", "Dual Brightness Control", menu_options, on_quit=terminate) # Initialize system tray icon
systray.start()

tooltip = "Detected: " + str(monitor_count) + "\nBrightness: " + str(last) + '%' # Set tooltip to current value
systray.update(hover_text=tooltip)

while True:
    current = sbc.get_brightness(display=0) # Get current brightness of the first monitor
    if current != last: # Compare with last value
        last = current # Set new value as last value

        for i in range(1, monitor_count): sbc.set_brightness(current, display=i) # Apply new value to all external monitors

        tooltip = "Detected: " + str(monitor_count) + "\nBrightness: " + str(current) + '%' # Set tooltip to current value
        systray.update(hover_text=tooltip)
        
        time.sleep(0.1) # Wait for 100ms to avoid flickering