# Gym-Manager-Bot
Python bot that automatically logs in and refreshes page until next gym appointment is available, then books it for you.
Currently compatible with booking at Fit4Less locations across Canada on their gymmanager interface.
The bot can  book a desired appointment, which is mainly useful for booking at midnight when new slots open.
It can also auto-refresh until booking at any time is available at a selected location.
It uses Python and the Selenium package to run (thus these packages, as well as chromedriver.exe, must be installed prior to use).
It is packaged into a .exe program using pyinstaller but the program needs to be finalized before this version is uploaded.
