import time, os, sys, colorama

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
	moscow = time.time() + time.timezone + 3 * 3600
	elements = []
	if Europe:
		elements.append(colorama.Fore.YELLOW + "CURRENT TIME (EUROPE):")
		for i in timezone_:
			time_ = moscow + timezone_[i] * 3600
			color = colorama.Fore.WHITE
			if time_ // 3600 == time.time() // 3600:
				color = colorama.Fore.GREEN
			element = i + ": " + time.ctime(time_)
			elements.append(color + element)
	if Europe and Russia:
		elements.append("")
	if Russia:
		elements.append(colorama.Fore.YELLOW + "CURRENT TIME (RUSSIA):")
		for i in timezone:
			time_ = moscow + timezone[i] * 3600
			color = colorama.Fore.WHITE
			if time_ // 3600 == time.time() // 3600:
				color = colorama.Fore.GREEN
			element = i + ": " + time.ctime(time_)
			elements.append(color + element)
	return "\n".join(elements)

def watch():
	colorama.init()
	try:
		while True:
			os.system("cls")
			print(update())
			time.sleep(1)
	except KeyboardInterrupt:
		pass

watch()