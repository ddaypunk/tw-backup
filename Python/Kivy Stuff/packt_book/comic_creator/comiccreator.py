# File Name: comiccreator.py
# pthon backend code for the comiccreator app in Kivy

#load all needed resources from Kivy classes
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

#load Kivy layout files
Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')

#create the main layout in python
class ComicCreator(AnchorLayout):
    pass

# run the app
class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()

if __name__ == "__main__":
    ComicCreatorApp().run()