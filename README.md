# scrapingrito
Scraping the riot league of legends match history to get custom game information.

All you need to do to get this working;

1 -Install selenium

  -open powershell or cmd and run the command: pip install selenium
  resource: https://selenium-python.readthedocs.io/installation.html
  
2 -Install a chrome driver

  -download a driver from the following link; https://chromedriver.chromium.org/downloads and copy the path were you save it
  
3 - Where you have the chrome driver installed copy the path (as said above)

4 - Open the file gethtmldata.py and on line 183 insert the path you copied above in the appropriate spot. Example path; C:/Users/youruser/Downloads/chromedriver_win32/chromedriver.exe

5- use python or powershell to run: python gethtmldata.py -match

6- answer the prompts and send me the resulting files!
