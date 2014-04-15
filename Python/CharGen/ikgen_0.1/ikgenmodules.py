__author__ = "Andrew Delso"


import config

def printTitle(systemName):
	print "\t\t  Welcome to %s" % systemName
	print "\t\tCommand Line Character Generator"

def printRaceList(raceList):
	print "Please select a Race from the list below"
	print "Please use exact spelling"
	count = 1
	for each in raceList:
		print "%s" % str(count),
		print ": ",
		print "%s" % each
		count +=1
	return raw_input("Choice: ")

def checkLevelName(experience):
	#while type(experience) !=  type(str) or experience < 0: #this is not working for some reason
		#experience = input("Error: Value is not valid, please re-enter: ")
		#print str(experience) 

	if str(experience) < 50:
		return "Hero"
	elif str(experience) < 100:
		return "Veteran"
	else:
		return "Epic"

def GetRaceStats(levelName,race):
	return config.raceDict[race][levelName]
	