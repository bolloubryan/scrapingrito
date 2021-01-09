import json
import re

fileopener = open("convertsummoner.txt", "r", encoding="utf-8")
raw = fileopener.read()
allsummoners =  json.loads(raw)

#add contents of matches.txt here
allmatches = []

if len(allmatches) == 0:
    print("Go into the python file and add the contents of the matches.txt to the appropriate location.")
else:
    for listed in allmatches:
        counter = 0
        for item in listed:
            if re.findall(r"\d\d\d\d\d\d\d\d\d\d", item):
                pass;
            else:
                listed[counter] = allsummoners[item]
                counter += 1
                
    fileopener2 = open("matcheswithid.txt", "w", encoding="utf-8")
    fileopener2.write(str(allmatches))