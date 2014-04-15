"""
***************************************************************************************
Just an example of printing the stats too the screen in a nice format

Uses vertically oriented grids

All data is contained in a config file

to improve:
* Modulize into different printing sections
* Braeak up the compund check at the end of the printing into a module to check since
its repetitive
***************************************************************************************
"""
#import external configuration data
import config
#impot ikResources modules
import ikRv_mods

"""
MAIN
"""

#run the function and output to console
ikRv_mods.printRaceList(config.raceDict,config.statsList)