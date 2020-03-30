#encondings: latin-1
# -*- coding: utf-8 -*-
__author__ = 'Mabel'

#__version__ = '0.0.12'
'''GOROROBA App
   escrito por: Mabel Calim Costa
   data: OUT/2019
   DRAFT01
'''
import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import time
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
import platform
import sys
from kivy.uix.popup import Popup
from functools import partial
from kivy.uix.label import Label
from kivy.factory import Factory as F
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window

# Editor
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os

class ImageButton(ButtonBehavior, Image):
    pass
class LabelButton(ButtonBehavior, Label):
    pass
class Rodape(Screen):
    pass
class Abertura(Screen):
    pass

class Salgados(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    path_s = str(os.path.abspath(os.path.dirname(__file__))) + "/salgados"
    path_f = str(os.path.abspath(os.path.dirname(__file__))) + "/favoritas_S2"


    def show_load(self):
        self.ids['doces_msg'].text = ""
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        self.ids['doces_msg'].text = ""
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.ids['doces_msg'].text = ""
        path_s = str(os.path.abspath(os.path.dirname(__file__))) + "/salgados"

        with open(os.path.join(path_s, filename[0])) as stream:
            self.text_input.text = stream.read()

        #self.dismiss_popup()

    def save(self, path, filename):
        if self.ids['text_input2'].text == '':
            self.ids['doces_msg'].text = " Atenção, dê um nome para receita modificada aqui embaixo. Ex: nova_receita.txt"
        else:
            with open(os.path.join(path, filename), 'w') as stream:
                stream.write(self.text_input.text)
            self.ids['doces_msg'].text = "Sua receita foi salva com sucesso!"

        #self.dismiss_popup()

class Doces(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    path_d = str(os.path.abspath(os.path.dirname(__file__))) + "/doces"
    path_f = str(os.path.abspath(os.path.dirname(__file__))) + "/favoritas_S2"


    def show_load(self):
        self.ids['doces_msg'].text = ""
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        self.ids['doces_msg'].text = ""
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.ids['doces_msg'].text = ""
        #path = str(os.path.abspath(os.path.dirname(__file__)))
        #path = path + '/doces/'
        path_d = str(os.path.abspath(os.path.dirname(__file__))) + "/doces"
        print (path_d)
        with open(os.path.join(path_d, filename[0])) as stream:
            self.text_input.text = stream.read()


        #self.dismiss_popup()

    def save(self, path, filename):
        if self.ids['text_input2'].text == '':
            self.ids['doces_msg'].text = " Atenção, dê um nome para receita modificada aqui embaixo. Ex: nova_receita.txt"
        else:
            with open(os.path.join(path, filename), 'w') as stream:
                stream.write(self.text_input.text)
            self.ids['doces_msg'].text = "Sua receita foi salva com sucesso!"

        #self.dismiss_popup()

class Favoritas(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    path_f = str(os.path.abspath(os.path.dirname(__file__))) + "/favoritas_S2"
    print (path_f)


    def show_load(self):
        self.ids['doces_msg'].text = ""
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        self.ids['doces_msg'].text = ""
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.ids['doces_msg'].text = ""
        path_f = str(os.path.abspath(os.path.dirname(__file__))) + "/favoritas_S2"
        print (path_f)
        with open(os.path.join(path_f, filename[0])) as stream:
            self.text_input.text = stream.read()

    def save(self, path, filename):
        if self.ids['text_input2'].text == '':
            self.ids['doces_msg'].text = " Atenção, dê um nome para receita modificada aqui embaixo. Ex: nova_receita.txt"
        else:
            with open(os.path.join(path, filename), 'w') as stream:
                stream.write(self.text_input.text)
            self.ids['doces_msg'].text = "Sua receita foi salva com sucesso!"

        #self.dismiss_popup()



GUI = Builder.load_file("main.kv")  # Make sure this is after all class definitions!
class GororobaApp(App):
    #url = 'https://legec-app.firebaseio.com'
    #rm no dir data
    def build(self):
        self.icon = 'figs/kpi_logo.png'
        self.title = 'GOROROBA-APP'
        return GUI
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


F.register('Doces', cls=Doces)
F.register('Salgados', cls=Doces)
F.register('Favoritas', cls=Favoritas)


GororobaApp().run()
