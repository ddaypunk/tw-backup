"""
ik_Resource module definitions
function definitions
"""
import config

#checkStat checks for special stat situations of 0 and -1
def checkStat(stat):
    if stat > 0:
        return str(stat)
    elif stat < 0:
        return "-"
    else:
        return "*"

#printRaceList prints out all the above data in a table format for each race
def printRaceList(racedict,statslist):
    #for each race, print the race name in the header
    for race, statlist in sorted(racedict.iteritems()):
        print "\n" + config.horizPipe
        if len(race) < 6:
            print "|\t\t\t          %s\t\t\t\t\t|" % race.upper()
        else:
            print "|\t\t\t          %s\t\t\t\t|" % race.upper()
        print config.horizPipe
        # for each race print the table headers
        print "|\*|*|*/|    Starting\t|     Hero\t|    Veteran\t|     Epic\t|"
        print "|/*|*|*\|    Value\t|     Limit\t|    Limit\t|     Limit\t|"
        print config.horizLine
        #loop throught and print out the stat values with row headers for each race
        i = 0
        for stat in statslist:
            print "|  %s\t" % stat,
            #make sure to check the stats for special situations
            print "|       %s\t" % checkStat(statlist["Start"][i]),
            print "|       %s\t" % checkStat(statlist["Hero"][i]),
            print "|       %s\t" % checkStat(statlist["Veteran"][i]),
            print "|       %s\t|" % checkStat(statlist["Epic"][i])
            
            i += 1
        #close the table and print sub-text
        print config.horizLine
        print " '*' = Only characters with the Gifted archetype have the Arcane stat."
        print " '-' = Race does not have the ability to take the Gifted Archetype."