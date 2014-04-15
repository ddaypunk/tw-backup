"""
config.py is the configuration file for the ikResources application

It contains all data elements used by the application
"""

__author__ = "Andrew Delso"

"""
Variable and data declarations
"""

horizPipe = "*=======================================================================*"
horizLine = "*-----------------------------------------------------------------------*"

raceDict = {"Human" : {"Start" : [5,6,4,3,4,4,3,0,3],
                       "Hero" : [7,7,6,5,5,5,5,4,5],
                       "Veteran" : [8,7,7,6,6,6,6,6,6],
                       "Epic" : [8,7,8,7,7,7,7,8,7]},

            "Dwarf" : {"Start" : [6,4,5,3,4,3,4,0,3],
                       "Hero" : [7,5,6,5,5,4,5,4,4],
                       "Veteran" : [7,6,7,6,6,5,6,6,6],
                       "Epic" : [8,6,8,7,7,6,7,7,7]},

            "Gobber" : {"Start" : [4,6,3,4,4,3,3,-1,3],
                       "Hero" : [6,7,4,5,5,5,4,-1,4],
                       "Veteran" : [7,7,5,6,6,6,5,-1,4],
                       "Epic" : [7,7,6,7,7,7,6,-1,5]},

            "Iosian" : {"Start" : [5,6,4,3,4,4,4,0,3],
                       "Hero" : [7,7,5,5,5,5,6,4,5],
                       "Veteran" : [7,7,6,6,6,6,6,6,6],
                       "Epic" : [7,7,7,7,7,7,7,8,7]},

            "Nyss": {"Start" : [5,6,4,4,4,4,3,0,3],
                       "Hero" : [7,7,6,5,5,5,5,4,5],
                       "Veteran" : [7,7,7,6,6,6,6,6,6],
                       "Epic" : [8,7,8,7,7,7,6,7,6]},

            "Ogrun" : {"Start" : [6,5,6,3,4,3,3,-1,2],
                       "Hero" : [7,6,8,5,5,4,5,-1,4],
                       "Veteran" : [8,6,9,5,6,5,5,-1,5],
                       "Epic" : [9,6,10,6,7,6,6,-1,6]},

            "Trollkin" : {"Start" : [6,5,5,3,4,2,3,0,3],
                       "Hero" : [8,6,7,5,5,4,4,4,4],
                       "Veteran" : [9,6,8,6,6,5,5,6,5],
                       "Epic" : [10,6,9,7,7,6,6,7,6]}}

statsList = ["PHY","SPD","STR","AGL","PRW","POI","INT","ARC","PER"]