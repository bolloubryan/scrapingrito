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
	#print("Three things to enter: ")
	#username = input("Enter your riot username: ")
	#password = getpass.getpass("Enter your riot password: ")
	#summonerurl = input("Enter the link to your riot match history")
	username = "petiyou14"
	password = "Nobleandhigh1998"
	summonerurl = "https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/216553215"
	# try:
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

	SCROLL_PAUSE_TIME = 0.5
	last_height = Browser.execute_script("return document.body.scrollHeight")

	while(True):
		try:
			Browser.find_element_by_id("game-summary-20997")
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

	# print("failed1 new one")
	# PageElement4 = Browser.find_element_by_id("binding-775")
	# print("failed2")
	# PageElement4.click()
	# print("failed3")
	# time.sleep(1)
	# print(Browser.current_url)
	# print("failed4")
	# time.sleep(1)
	# print("failed5")
	# Browser.get("https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/216553215")
	# Browser.refresh()

	pageraw = Browser.page_source

	regexmatch = re.findall(r"\<div id\=\"binding\-\d+\" class\=\"binding\" style\=\"\"\>Custom\<\/div\>", pageraw)

	idstoclick = []

	for reggie in regexmatch:
		reggie1 = reggie.split('id="')[1]
		reggie2 = reggie1.split('" class')[0]
		idstoclick.append(reggie2)
	#print(idstoclick)
	#pageraw.split('" class="binding" style="">Custom</div>')

	# fileopener = open("pagesource.txt", "w")
	# fileopener.write(str(pageraw.encode("utf-8")))

	#matchidurl = []

	allsummoners = []
	summoners = []

	counter = len(idstoclick)

	for ids in idstoclick:
		print(ids)
		print("This many ids left: " + str(counter))
		counter -= 1
		if counter == 90:
			break;
		SCROLL_PAUSE_TIME = 1
		last_height = Browser.execute_script("return document.body.scrollHeight")

		while(True):
			try:
				PageElement6 = Browser.find_element_by_id(ids)
				#PageElement6 = Browser.find_element_by_id("binding-773")
				PageElement6.click()
				time.sleep(1)
				urlb = Browser.current_url
				#matchidurl.append(urlb)
				rawpage = Browser.page_source
				matchregex = re.findall(r"match\-history\/(NA1|NA)\/\d+\".*?\>(.*?)\<\/a\>", rawpage)
				#<a href="#match-history/NA1/210676684" class="summoner-long">CandyConnoisseur</a>
				#print(matchregex)

				#print(urlb)
				urlbID = re.search(r"match\-details\/(NA1|NA)\/(.*?)\/", urlb)
				#print(urlbID[2])
				for maggie in matchregex:
					maggie1 = maggie[1]
					summoners.append(maggie1)
					#print(maggie1)
				summoners.pop(0)
				summoners.append(urlbID[2])
				allsummoners.append(summoners)
				summoners = []
				print(allsummoners)
				#print("found")
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

		time.sleep(1)
		Browser.get("https://matchhistory.na.leagueoflegends.com/en/#match-history/NA1/216553215")
		time.sleep(1)
		Browser.refresh()
		time.sleep(2.5)
		
	
	fileopener = open("matpart.txt", "w")
	fileopener.write(str(allsummoners))
	
def main():
	#Take the script arguments from the user input
	Args = CLIArguments()

	#If none of the Arguments are True
	if not any(Args):
 		print("\nNo validation requested. Try -h or --help for your options\n")
 		sys.exit()

	#Setting the driver as chrome
	ChromeDriver = webdriver.Chrome(executable_path='C:/Users/bollouballs/Downloads/chromedriver_win32/chromedriver.exe')


	if Args [0] == True:
		getMatchids(ChromeDriver)
		print("getMatchids")
		time.sleep(5)
	
	ChromeDriver.close()

main()