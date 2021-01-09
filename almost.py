#add contents of matcheswithid.txt here
summonerids = []

if len(summonerids) == 0:
    print("Go into the python file and add the contents of the matcheswithid.txt to the appropriate location.")
else:
    for listed in summonerids:
        if len(listed) > 10:
            counter = 1
            for item in range(0,len(listed)-1):
                if (counter < 6):
                    teamid = 100
                else :
                    teamid = 200
                print(listed[item]+"    "+listed[10]+"    "+str(counter)+"    "+str(teamid))
                counter +=1
        