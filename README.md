# Gym-Manager-Bot
DESCRIPTION:

Python bot that automatically logs in and refreshes page until next gym appointment is available, then books it for you.
Currently compatible with booking at Fit4Less locations across Canada on their gymmanager interface.
The bot can  book a desired appointment, which is mainly useful for booking at midnight when new slots open.
It can also auto-refresh until booking at any time is available at a selected location.
It uses Python and the Selenium package to run (thus these packages, as well as chromedriver.exe, must be installed prior to use).
It is packaged into a .exe program using pyinstaller but the program needs to be finalized before this version is uploaded.

USAGE:
1. Ensure Selenium, Tkinter, Python 3.7+, and ChromeDriver are installed and added to PATH where necessary
2. Run 'py main.py' on command line
3. Enter in information, currently there's no error trapping so enter information as instructed
4. Select 'Run Bot'
5. When the command line outputs 'Booked!', check your account and the booking should be complete
