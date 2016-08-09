import os

accounts = open("accounts", "r")
tab = []

for line in accoutns:
	tab.append(line.split(" "))
for i in range(len(tab)):
	tab[i][1] = tab[i][1][:-1]
for account in tab:
	os.system("mkdir " + account[0])
	os.system("cp config.json.templ " + account[0] + "/config.json")
	os.system("sed -i -e \'s/TEMPL_USERNAME/" + account[0] + "/g\' " + account[0] + "/config.json")
	os.system("sed -i -e \'s/TEMPL_PASSWORD/" + account[1] + "/g\' " + account[0] + "/config.json")
	os.system("docker run --name pokefarm__run_" + account[0] + " -d -t -v `pwd`" + account[0] + "/config.json:/usr/src/app/configs/config.json --link YOUR-MAP-CONTAINER-NAME:YOUR-MAP-CONTAINER-NAME YOUR-IMAGE-NAME")
	#os.system("docker run --name pokefarm__run_" + account[0] + " -d -t -v `pwd`" + account[0] + "/config.json:/usr/src/app/configs/config.json YOUR-IMAGE-NAME")
