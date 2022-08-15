# Multi Brightness Control
# Set brightness values for all monitors
# Created by Segilmez06 - sarpegilmez.com

version = '1.0'

# Print welcome message
import sys
if not "-s" in sys.argv[1:]: print("Multi Brightness Control")

# Print help message
if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]: 
    print("Usage: " + sys.argv[0] + " [options]")
    print("")
    print("Options:")
    print("\t-c <id>\t\t\t\tPrint current brightness of display.")
    print("\t-b <value> <id>\t\t\tSet brightness of display.")
    print("\t-g \t\t\t\tGet available displays.")
    print("\t-s \t\t\t\tDo not print any debug message. Does not affect output of -c argument.")
    print("")
    print("\t--check-packages\t\tCheck if required packages are installed")
    print("\t--skip-count-validation\t\tSkip checking of monitor count")
    print("\t--no-extract-icon\t\tDo not extract system tray icon to file")
    print("\t--no-systray-icon\t\tDo not add icon to system tray")
    print("")
    print("\t-h, --help\t\t\tShow this help")
    print("\t-v, --version\t\t\tShow version")
    sys.exit(0)

# Print version strings
if "-v" in sys.argv[1:] or "--version" in sys.argv[1:]: 
    print("Version " + version)
    print("Running on Python " + sys.version)
    sys.exit(0)

# Check for packages
if "--check-packages" in sys.argv[1:]:
    import pkg_resources
    import subprocess
    if not "-s" in sys.argv[1:]: print("Checking if need to install packages...")
    to_install = {'infi.systray', 'screen_brightness_control'} - {pkg.key for pkg in pkg_resources.working_set} # Determine packages to install
    if to_install:
        if not "-s" in sys.argv[1:]: print("%d packages is not installed." % len(to_install))
        for pkg in to_install:
            if not "-s" in sys.argv[1:]: print("Installing " + pkg)
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]) # Install packages via pip

# Import neccesary packages
if not "-s" in sys.argv[1:]: print("Importing packages...")
from infi.systray import SysTrayIcon
import screen_brightness_control as sbc
import time
import os

# Print available displays
if "-g" in sys.argv[1:]:
    for monitor in sbc.list_monitors():
        print(monitor)
    sys.exit(0)

# Print current brightness of display with id
elif "-c" in sys.argv[1:]:
    pos = sys.argv.index("-c")
    display_id = int(sys.argv[pos + 1])
    print(sbc.get_brightness(display=display_id))
    sys.exit(0)

# Set current brightness of display with id
elif "-b" in sys.argv[1:]:
    pos = sys.argv.index("-b")
    value = int(sys.argv[pos + 1])
    display_id = int(sys.argv[pos + 2])
    sbc.set_brightness(value, display=display_id)
    sys.exit(0)

def terminate(systray): os.kill(os.getpid(), 9) # Terminate function
def func_no(systray): pass # Empty function

# Check available display count
if not "--skip-count-validation" in sys.argv[1:]: # Check for available monitor count
    wait = 0
    monitor_count = len(sbc.list_monitors())
    while monitor_count < 0: # Wait for other monitors to be connected
        if not "-s" in sys.argv[1:]: print("Attempt %d: No external monitors found." % wait)
        time.sleep(1)
        if wait < 30: # Wait until 30 failed attempts
            monitor_count = len(sbc.list_monitors())
            wait += 1
        else:
            if not "-s" in sys.argv[1:]: print("Attempt %d: %d seconds passed and still no monitors connected. Terminating..." % wait)
            terminate(None) # No reason to waste system resources if there is no external monitor connected

# Print display count
if not "-s" in sys.argv[1:]: print("%d monitors found." % monitor_count)

# Set current brightness as last value
last = sbc.get_brightness(display=0)

# Print current brightness
if not "-s" in sys.argv[1:]: print("Primary display brightness is " + str(last) + "%.")

# Extract icon to file
if not "--no-extract-icon" in sys.argv[1:]:
    if not "-s" in sys.argv[1:]: print("Extracting icon to file...")
    img = bytearray(b"\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00 \x00\xb2\x01\x00\x00\x16\x00\x00\x00\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x03\x00\x00\x00(-\x0fS\x00\x00\x00\x01sRGB\x01\xd9\xc9,\x7f\x00\x00\x00\tpHYs\x00\x00\x0eM\x00\x00\x0eM\x01F\xd5h\t\x00\x00\x00\x8aPLTE\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf67h\x8d\x00\x00\x00.tRNS\x00\x8fa\x9dk\xa8C\\\x93\xedxW\xec0i\xdf\xff\xd7\xfb\xf9D\xd0\xb9]\xfc\xfar\x88>\xf4\xeeL\xb3\x907\xe6\xd9)[&\x89\xd3\xcf}q~\x0f\x08\x003\x00\x00\x00\x87IDATx\x9cm\x8f\xd9\x12\x820\x0cEc\x13[T\xd0\xaa\xb8\xa2\x82\x0b\xa0\xa8\xff\xff{\x86\xa6\xad\xe3\x8c\xe7)\xf7L\'\xb9\x05\x10\x06\n~A\xfa\xceC\x1d\x84I\x9c\xd0#6\xe3\t\xe74\x03o\xa63k\xe71\x03\xa8\x85e\x96y\xdc\xb2\xb2\x8e\xb5\xdcC\xdclE\xec\xf6\x88\x05(\xa2\xc3Q\xc4\xa9$2\xeeU%\xe2\x1cw\\\xae}\xbe\xd5!7i{\x7ft\xcf\xb6\xef#\x99\xef\xbfJ\xdf\x90I\xb2P]\xbf\xff\x7f\xceQ\x18?|\x00\x8e\x17\x07\x8d\xd3\xff\x95\x90\x00\x00\x00\x00IEND\xaeB`\x82")
    with open("icon.ico", "wb") as image:
        image.write(img)

# Add app icon to system tray
if not "--no-systray-icon" in sys.argv[1:]:
    menu_options = (("Detected: " + str(monitor_count), None, func_no),) # Add connected monitor count as menu item

    if not "-s" in sys.argv[1:]: print("Starting system tray icon...")
    systray = SysTrayIcon("icon.ico", "Dual Brightness Control", menu_options, on_quit=terminate) # Initialize system tray icon
    systray.start()

    tooltip = "Detected: " + str(monitor_count) + "\nBrightness: " + str(last) + '%' # Set tooltip to current value
    systray.update(hover_text=tooltip)

# Main loop for adjust in real time
if not "-s" in sys.argv[1:]: print("Starting main loop...")
while True:
    current = sbc.get_brightness(display=0) # Get current brightness of the first monitor
    if current != last: # Compare with last value
        last = current # Set new value as last value

        for i in range(1, monitor_count): sbc.set_brightness(current, display=i) # Apply new value to all external monitors

        if not "--no-systray-icon" in sys.argv[1:]:
            tooltip = "Detected: " + str(monitor_count) + "\nBrightness: " + str(current) + '%' # Set tooltip to current value
            systray.update(hover_text=tooltip)
        
        time.sleep(0.1) # Wait for 100ms to avoid flickering