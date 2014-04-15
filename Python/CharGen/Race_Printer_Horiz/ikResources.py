"""
Just an example of printing the stats too the screen in a nice format

Uses horizontally oriented grids

Bug: Dictionaries do not print in order.  Might need to 
"""

raceList = {"Human" : {"1: Start" : [5,6,4,3,4,4,3,0,3],
                       "2: Hero" : [7,7,6,5,5,5,5,4,5],
                       "3: Veteran" : [8,7,7,6,6,6,6,6,6],
                       "4: Epic" : [8,7,8,7,7,7,7,8,7]},

            "Dwarf" : {"1: Start" : [6,4,5,3,4,3,4,0,3],
                       "2: Hero" : [7,5,6,5,5,4,5,4,4],
                       "3: Veteran" : [7,6,7,6,6,5,6,6,6],
                       "4: Epic" : [8,6,8,7,7,6,7,7,7]},

            "Gobber" : {"1: Start" : [4,6,3,4,4,3,3,0,3],
                       "2: Hero" : [6,7,4,5,5,5,4,0,4],
                       "3: Veteran" : [7,7,5,6,6,6,5,0,4],
                       "4: Epic" : [7,7,6,7,7,7,6,0,5]},

            "Iosian" : {"1: Start" : [5,6,4,3,4,4,4,0,3],
                       "2: Hero" : [7,7,5,5,5,5,6,4,5],
                       "3: Veteran" : [7,7,6,6,6,6,6,6,6],
                       "4: Epic" : [7,7,7,7,7,7,7,8,7]},

            "Nyss": {"1: Start" : [5,6,4,4,4,4,3,0,3],
                       "2: Hero" : [7,7,6,5,5,5,5,4,5],
                       "3: Veteran" : [7,7,7,6,6,6,6,6,6],
                       "4: Epic" : [8,7,8,7,7,7,6,7,6]},

            "Ogrun" : {"1: Start" : [6,5,6,3,4,3,3,0,2],
                       "2: Hero" : [7,6,8,5,5,4,5,0,4],
                       "3: Veteran" : [8,6,9,5,6,5,5,0,5],
                       "4: Epic" : [9,6,10,6,7,6,6,0,6]},

            "Trollkin" : {"1: Start" : [6,5,5,3,4,2,3,0,3],
                       "2: Hero" : [8,6,7,5,5,4,4,4,4],
                       "3: Veteran" : [9,6,8,6,6,5,5,6,5],
                       "4: Epic" : [10,6,9,7,7,6,6,7,6]}}

statsList = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]

def printHeader(race,statlist):
    print "| \t\t\t\t  Race Stat Table: %s  \t\t\t\t|" % race
    print "|   Stat Type  ",
    for stat in statlist:
        print "|  %s \t" % stat,
    print "|",

def printStatLine(raceStatDict):
    for key, value in sorted(raceStatDict.iteritems()):
        print "|   %s \t" % key,
        for stat in value:
            if stat == 0:
                print "|   * \t", 
            else: 
                print "|   %s \t" % stat,
        print "|"



def printRaceStats(racelist, statlist):
    for key, value in sorted(racelist.iteritems()):
        printHeader(key,statlist)
        print ""
        printStatLine(value)
        print ""

printRaceStats(raceList,statsList)

class race:
    name = ""
    statList = {}

    #constructor
    #destructor
    #etc

"""
A different way to print vertically using multiple lists in a for:

for a, b, c, d, e, f, g in zip (stat1, stat2, stat3...):
    print a, b, c, d, e, f, g
"""