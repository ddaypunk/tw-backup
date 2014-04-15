"""
Filename: ikrpg_gen.py
Function: Lays out the kivy framework for the app
__author__ = 'adelso'
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel

#load external kivy ui files
Builder.load_file('ikrpg_gen.kv')
Builder.load_file('titlebar.kv')
Builder.load_file('tabarea.kv')


#define classes

class IkRpg_Gen(TabbedPanel):
    pass

class IkRpg_GenApp(App):
    def build(self):
        return IkRpg_Gen()

if __name__ == '__main__':
    IkRpg_GenApp().run()