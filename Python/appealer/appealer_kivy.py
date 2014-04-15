'''
Python Imports
'''
from subprocess import call, check_output
from appeal_defs import *
from functools import partial

'''
Kivy Imports
'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView


class AppealerApp(App):

    def build(self):
    	#create the parent object
        parentLayout = BoxLayout(padding=10,orientation='vertical')
        
        #create children layouts and add to parent
        layout1 =  BoxLayout(padding=10)
        layout2 = BoxLayout(padding=10)
        layout3 = BoxLayout(padding=10)
        parentLayout.add_widget(layout1)
        parentLayout.add_widget(layout2)
        parentLayout.add_widget(layout3)

        #create layout1 children and add to layout1
        ip_label = Label(text='[b]IP Address[/b]',markup=True)
        ip_textbox = TextInput(hint_text='Enter your IP address here.',hint_text_color=(1,.5,.5,1.),multiline=False)
        runButton = Button(text='Run')
        resetButton = Button(text='Reset')
        layout1.add_widget(ip_label)
        layout1.add_widget(ip_textbox)
        layout1.add_widget(runButton)
        layout1.add_widget(resetButton)

        #create layout2 childrean and add to layout2
        options_label = Label(text='[b]Options[/b]',markup=True)
        layout2.add_widget(options_label)

        #create layout3 childrean and add to layout3
        results_container = BoxLayout(size_hint_y=None)
        results_textbox = TextInput()
        results_container.add_widget(results_textbox)
        results_scrollbox = ScrollView(size_hint=(None, None))
        results_scrollbox.add_widget(results_container)
        layout3.add_widget(results_scrollbox)

        def run_command(box,instance,*args):
            console_command = ['traceroute', ip_textbox.text]
            console_code =  call(console_command)
            if console_code == 0:
                box.text = check_output(console_command)

        runButton.bind(on_release=partial(run_command,results_textbox))

        def clear_app(obj):
            ip_textbox.select_all()
            ip_textbox.delete_selection()
            results_textbox.select_all()
            results_textbox.delete_selection()

        resetButton.bind(on_release=clear_app)


        return parentLayout

if __name__ == '__main__':
    AppealerApp().run()