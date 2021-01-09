import argparse, sys, time
import getpass
import re
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException, ElementNotVisibleException, UnexpectedAlertPresentException

def CLIArguments():
	ArgParser = argparse.ArgumentParser()
	ArgParser.add_argument("-match", required=False, action='store_true', default=False, help="Get all match ids")
	Args = ArgParser.parse_args()
	return [Args.match]
	
def getMatchids (Browser):
	print("Three things to enter: ")
	username = input("Enter your riot username: ")
	password = getpass.getpass("Enter your riot password: ")
	summonerurl = input("Enter the link to your riot match history, navigate to https://matchhistory.na.leagueoflegends.com and log in. EG: https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/216553215: ")

	Browser.get(summonerurl)
	time.sleep(5)
	PageElement = Browser.find_element_by_name("username")
	PageElement.clear()
	PageElement.send_keys(username)
	PageElement2 = Browser.find_element_by_name("password")
	PageElement2.clear()
	PageElement2.send_keys(password)
	PageElement3 = Browser.find_element_by_xpath("//button[@type='submit']")
	PageElement3.send_keys(Keys.RETURN)
	time.sleep(5)
	Browser.refresh()
	time.sleep(5)

	while (True):
		searchstart = input("Enter 1 to enter the exact date and time for the first game to start scrapping from.\nEnter 2 to scroll to the first custom game")

		if searchstart == "1":
			searchtime = input("Enter the duration of the game in the format: MM:SS. EG: 36:24. *** NO SPACES: ")
			datetime = input("Enter the duration of the game in the format: MM/DD/YYYY. EG: 36:24. *** NO SPACES AND NO NEED FOR LEADING ZEROS: ")

			SCROLL_PAUSE_TIME = 0.5
			last_height = Browser.execute_script("return document.body.scrollHeight")
			while(True):
				try:
					pageraw = Browser.page_source
					time.sleep(SCROLL_PAUSE_TIME)
					datematch = re.findall(r"\<div id=\"(date-duration-\d+)\" class=\"date-duration\" style=\"\"\>\<span class=\"date-duration-duration\"\>\<div id=\"binding-\d+\" class=\"binding\" style=\"\">\b"+searchtime+r"\b\<\/div\>\<\/span\> \<span class=\"date-duration-date\"\>\<div id=\"binding-\d+\" class=\"binding\" style=\"\">\b"+datetime+r"\b<\/div><\/span><\/div>", pageraw)
					time.sleep(SCROLL_PAUSE_TIME)
					print(datematch)
					PageElement6 = Browser.find_element_by_id(datematch[0])
					time.sleep(SCROLL_PAUSE_TIME)
					print("Found")
					break;
				except:
						# Scroll down to bottom
						Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

						# Wait to load page
						time.sleep(SCROLL_PAUSE_TIME)

						# Calculate new scroll height and compare with last scroll height
						new_height = Browser.execute_script("return document.body.scrollHeight")
						if new_height == last_height:
							print("End of page")
							break;
						last_height = new_height
			time.sleep(5)
			break;
		elif searchstart == "2":
			stop = input("Scroll to the first custom game and type in anything then press Enter to start scraping: SCROLL TILL YOU SEE FIRST GAME -> [Any Key] + [Enter]")
			break;
		else:
			print("Please enter 1 or 2 idiot")

	pageraw = Browser.page_source

	fileopener = open("checkcustoms.txt", "w", encoding="utf-8")
	fileopener.write(str(pageraw))

	typematch = re.findall(r"\<span class\=\"map-mode-queue\"\>\<div id\=\"binding-\d+\" class=\"binding\" style\=\"\"\>(.*?)\<\/div\>\<\/span\>", pageraw)
	timematch = re.findall(r"\<span class\=\"date-duration-duration\"\>\<div id\=\"binding\-\d+\" class\=\"binding\" style\=\"\"\>(.*?)\<\/div\>", pageraw)
	datematch = re.findall(r"\<span class\=\"date-duration-date\"\>\<div id\=\"binding\-\d+\" class\=\"binding\" style\=\"\"\>(.*?)\<\/div\>", pageraw)

	matchlist = X = [list(e) for e in zip(timematch, datematch, typematch)]

	custommatches = []

	for items in matchlist:
		if items[2].lower() == 'custom':
			custommatches.append([items[0],items[1]])

	allsummoners = []
	summoners = []

	counter = len(custommatches)

	for match in custommatches:
		print(match[0])
		print(match[1])

		print("This many matches left to scrape: " + str(counter))
		counter -= 1

		SCROLL_PAUSE_TIME = 0.5
		last_height = Browser.execute_script("return document.body.scrollHeight")

		while(True):
			try:
				time.sleep(SCROLL_PAUSE_TIME)
				datematch = re.findall(r"\<div id=\"(date-duration-\d+)\" class=\"date-duration\" style=\"\"\>\<span class=\"date-duration-duration\"\>\<div id=\"binding-\d+\" class=\"binding\" style=\"\">\b"+match[0]+r"\b\<\/div\>\<\/span\> \<span class=\"date-duration-date\"\>\<div id=\"binding-\d+\" class=\"binding\" style=\"\">\b"+match[1]+r"\b<\/div><\/span><\/div>", pageraw)
				time.sleep(SCROLL_PAUSE_TIME)
				PageElement6 = Browser.find_element_by_id(datematch[0])
				time.sleep(SCROLL_PAUSE_TIME)
				PageElement6.click()
				time.sleep(SCROLL_PAUSE_TIME)

				urlb = Browser.current_url
				urlbID = re.search(r"match\-details\/(NA1|NA)\/(.*?)\/", urlb)

				rawpage = Browser.page_source
				matchregex = re.findall(r"match\-history\/(NA1|NA)\/\d+\".*?\>(.*?)\<\/a\>", rawpage)

				howlingyuck = re.findall(r"Howling Abyss", rawpage)

				if (howlingyuck):
					print("Hollowing Abyss skipping")
					pass;
				else:
					customyes = re.findall(r"Custom", rawpage)
					if(customyes):
						for maggie in matchregex:
							maggie1 = maggie[1]
							summoners.append(maggie1)
						summoners.pop(0)
						summoners.append(urlbID[2])
						allsummoners.append(summoners)
						summoners = []
						print(allsummoners)
						break;
			except:
				# Scroll down to bottom
				Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

				# Wait to load page
				time.sleep(SCROLL_PAUSE_TIME)

				# Calculate new scroll height and compare with last scroll height
				new_height = Browser.execute_script("return document.body.scrollHeight")
				if new_height == last_height:
					print("End of page")
					break;
				last_height = new_height

		time.sleep(0.5)

		Browser.get(summonerurl)

		time.sleep(0.5)
		Browser.refresh()
		time.sleep(0.5)		
	
	print("Got all the matches! If you see an error just copy and paste it out of the console into a text file.")
	fileopener = open("matches.txt", "a")
	fileopener.write(str(allsummoners))
	
def main():
	#Take the script arguments from the user input
	Args = CLIArguments()

	#If none of the Arguments are True
	if not any(Args):
 		print("\nNo Argument provied. Try -h or --help for your options\n")
 		sys.exit()

	#Setting the driver as chrome
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	ChromeDriver = webdriver.Chrome(executable_path='C:/Users/bollouballs/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)


	if Args [0] == True:
		getMatchids(ChromeDriver)
		print("Success and we done. Written by Bryan Bollou. Github: https://github.com/bolloubryan. Website: bollou.com")
		time.sleep(5)
	
	ChromeDriver.close()

main()