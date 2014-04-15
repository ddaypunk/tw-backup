__author__ = "Andrew Delso"


import ikgenmodules
import config

ikgenmodules.printTitle("Iron Kingdoms RPG")
experiencePts = raw_input("What experience level is your Character?: ")
experienceLevel =  ikgenmodules.checkLevelName(experiencePts)
charName = raw_input("What is your character's Name?: ")
print " "
print " "
print "Okay, so your Character name is %s, Great!" % str(charName)
choice = ikgenmodules.printRaceList(config.raceDict)
raceChoiceStats = ikgenmodules.GetRaceStats(experienceLevel, choice)
print raceChoiceStats