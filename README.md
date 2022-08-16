# Multi Brightness Control

[![Code Quality](https://api.codiga.io/project/34389/score/svg "Code Quality")](https://app.codiga.io/hub/project/34389/Multi-Brightness-Control)

Multi Brightness Control is an utility for changing brightnesses for all monitors at same time. Only works on Windows. It reads primary display (aka. internal display in laptops) brightness value and applies to all other displays. For example, if you connect an external monitor to your laptop and change screen brightness via action center or keyboard, other external monitor's brightness will also change.

There is two versions:

- Full: Creates an system tray icon to track current value and connected display count. Also supports command line arguments.
- Clear: Just core feature. Only checks brightness and applies to all monitors.

## Installation

1) Clone the repository: `git clone https://github.com/Segilmez06/Multi-Brightness-Control`
2) Enter the directory: `cd Multi-Brightness-Control`
3) Install the dependencies: `pip install -r requirements.txt`
4) Run the script: `python main.py` or `python clear.py`

Also you can create link to script in startup folder to run it on login.

## Contributing

You can help me by reporting bugs, suggesting features or creating pull requests.
