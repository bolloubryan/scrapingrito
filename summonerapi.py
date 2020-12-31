import requests 

summoners = ['4GPA','08 31 2018','jrry','Yung Khalifa','wickdCali','LiftDoyuBruh','kimmindo','dÈDD', 'ÉDD', 'Petiyou14','Stratifyd','Chaindawgz','Based Escroto','CandyConnoisseur','IsuckSoMuch','Eriano','Rayuz','lsuna','Ocean Gale','Sonaros','iTorrent','Yooniversity','Bigbabies','PrimeMinisterKL','Doyouliftbruh','Rafuego','Homophobia','Real ting ','Sungju Park','Jetso789','Dragnic','Literally Sticks','vastdem','aish shiibaal','harrowharrow','Vacuums','KupoTheGreat3199','colourblind','Hans Zimmer','RealityKnight','TurmoiLord']

for name in summoners:
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+"?api_key=RGAPI-dd7c0f74-16b0-4c66-b858-6b155f3b1195"
    response = requests.get(url)
    jsoning = response.json()
    print(jsoning["id"] + "   " + name)