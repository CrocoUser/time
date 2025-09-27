import time, os, sys

timezone_ = {"FWT ": -4, "FWST": -3, "WET ": -3, "WEST": -2, "CET ": -2, "CEST": -1, "EET ": -1, "EEST": 0, "FET ": 0}
timezone = {"KALT": -1,  "MSK ": 0,  "SAMT": 1,  "YEKT": 2,  "OMST": 3,  "KRAT": 4,  "IRKT": 5,  "YAKT": 6,  "VLAT": 7,  "MAGT": 8,  "PETT": 9}

Europe = True
Russia = True
if len(sys.argv) > 1:
	if sys.argv[1] == "Europe":
		Russia = False
	elif sys.argv[1] == "Russia":
		Europe = False

def update():
	moscow = time.time() - 2 * 3600
	elements = []
	if Europe:
		elements.append("CURRENT TIME (EUROPE):")
		for i in timezone_:
			element = i + ": " + time.ctime(moscow + timezone_[i] * 3600)
			elements.append(element)
	if Europe and Russia:
		elements.append("")
	if Russia:
		elements.append("CURRENT TIME (RUSSIA):")
		for i in timezone:
			element = i + ": " + time.ctime(moscow + timezone[i] * 3600)
			elements.append(element)
	return "\n".join(elements)

def watch():
	try:
		while True:
			os.system("cls")
			print(update())
			time.sleep(1)
	except KeyboardInterrupt:
		pass

watch()