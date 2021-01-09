import re

#Before you put in the matches.txt do a find and replace for ]][[ to ], [

fileopener = open("matches.txt", "r", encoding="utf-8")
allsummoners = fileopener.read()
alllist = []

regexmatch = re.findall(r"\'(.*?)\'", allsummoners)

unique = []

for item in regexmatch:
    if item in unique:
        pass;
    else :
        if re.findall(r"\d\d\d\d\d\d\d\d\d\d", item):
            pass;
        else :
            if item == '�DD':
                item = 'ÉDD'
            if item == 'd�DD':
                item = 'dÈDD'
            if item == '�ucky7':
                item = 'Łucky7'
            unique.append(item)

print(unique)

fileopener = open("allsummoners.txt", "w", encoding="utf-8")
fileopener.write(str(unique))