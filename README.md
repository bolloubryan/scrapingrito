# scrapingrito
Scraping the riot league of legends match history to get custom game information.

All you need to do to get this working;
-Install selenium
  -open powershell or cmd and run the command: pip install selenium
  resource: https://selenium-python.readthedocs.io/installation.html
-Install a chrome driver
  -download a driver from the following link; https://chromedriver.chromium.org/downloads and copy the path were you save it
- Where you have the chrome driver installed copy the path (as said above)
- Open the file gethtmldata.py and on line 183 insert the path you copied above in the appropriate spot. Example path; C:/Users/youruser/Downloads/chromedriver_win32/chromedriver.exe
