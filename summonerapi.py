import requests
import re 

fileopener = open("allsummoners.txt", "r", encoding="utf-8")
allsummoners = fileopener.read()

regexmatch = re.findall(r"\'(.*?)\'", allsummoners)

summoners = []

convertdict = {}

for item in regexmatch:
    summoners.append(item)

for name in summoners:
    try:
        url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key=RGAPI-dd7c0f74-16b0-4c66-b858-6b155f3b1195"
        response = requests.get(url)
        jsoning = response.json()
        idnew = jsoning["id"]
        print(idnew)
        print(name)
        convertdict [name] = idnew
    except:
        print(name)
        print("Summoner not found")

fileopener2 = open("convertsummoner.txt", "w", encoding="utf-8")
fileopener2.write(str(convertdict))

# make sure all the single quotes are double quotes