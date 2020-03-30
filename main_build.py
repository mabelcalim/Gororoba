Rodape#encondings: utf-8
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


#from firebase import firebase
import requests
import json
from kivy.garden.mapview import MapView,MapMarker
from kivy.properties import NumericProperty
import pickle
from kivy.utils import platform

Builder.load_string('''

<Gerenciador>:
    Rodape:
        name: 'rodape'
<Rodape>:
    GridLayout:
        cols: 1
        FloatLayout:
            GridLayout:
                canvas:
                    Color:
                        #rgba: 0.9961,0.5508,0,1
                        rgba: 0.5, 0.7773,0.8047,1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                rows: 1
                pos_hint: {"top": 1, "left": 1}
                size_hint: 1, .1
                #Image:
                #    source: "figs/logo.png"
                #    id: avatar_image
                #    #size_hint: 0.5, 0.7
                #    pos_hint: {"top": 1, "right": 0.75}
                Image:
                    source: "figs/mauro_logo.png"
                    size_hint: 0.25,0.55
                    pos_hint: {"top": 1, "right": 0.45}
                Image:
                    source: "figs/mabel_logo.png"
                    size_hint: 0.25, 0.55
                    pos_hint: {"top": 1, "right": 0.8}
                Image:
                    size_hint: 0.25,0.55
                    source: "figs/kpi_logo.png"

            ScreenManager:
                size_hint: 1, 0.899
                pos_hint: {"top": .899, "left": 1}
                id: screen_manager
                Abertura:
                    name: "abertura"
                    id: abertura
<Abertura>:

    FloatLayout:
        canvas:
            Color:
                #rgba:  0.6211,0.8906,0.9141,1
                #rgba: 0.5, 0.7773,0.8047,1
                rgba: 0.4922, 0.7969,0.8281,.9
            Rectangle:
                size: self.size
                pos: self.pos

        Image:
            source: "figs/logo.png"
            id: avatar_image
            size_hint: 0.8, 1.1
            pos_hint: {"top": 1.5, "right": 0.9}

        ImageButton:
            source: "figs/salgados.png"
            size_hint: 0.25,0.55
            pos_hint: {"top": 1, "right" :.75}
        ImageButton:
            source: "figs/doces.png"
            size_hint: 0.25,0.55
            pos_hint: {"top": 1, "right" :.4}
        ImageButton:
            source: "figs/ingredientes.png"
            size_hint: 0.25,0.55
            pos_hint: {"top": .6, "right" :.6}
        GridLayout:
            #  Menu buttons here
            rows: 1
            pos_hint: {"top": .15, "left": 1}
            size_hint: 1, .15
            #ImageButton:
            #    source: "figs/meu_mapa.png"
            #    on_release: root.draw_MapNow()  #root.MeuMapa()
            #Button:
            #    source: "figs/nova_coleta.png"
            #    on_release:root.change_screen() #app.root.current='local'

            #ImageButton:
            #    source: "figs/settings.png"
''')


class Gerenciador(ScreenManager):
        #def new_craca(self,ind):
        #    self.app.root.ids['%s'%ind].ids['%s_craca'%ind].color = 1.,1.,1., 1
        #    self.app.root.ids['%s'%ind].ids['%s_ostra'%ind].color = 1.,1.,1., 0.5
        #    self.app.root.ids['%s'%ind].ids['%s_alga'%ind].color = 1.,1.,1., 0.5
        #    self.app.root.ids['%s'%ind].ids['%s_anemona'%ind].color = 1.,1.,1., 0.5
        #    self.app.root.ids['%s'%ind].ids['%s_mexilhao'%ind].color = 1.,1.,1., 0.5
        #    self.app.root.ids['%s'%ind].ids['%s_caramujo'%ind].color = 1.,1.,1., 0.5
        #    self.app.root.ids['%s'%ind].ids['%s_outro'%ind].color = 1.,1.,1., 0.5
        pass


class ImageButton(ButtonBehavior, Image):
    pass
class FirstPage(Screen):
    pass
class Abertura(Screen):
    pass
class GororobaApp(App):
    #url = 'https://legec-app.firebaseio.com'
    #rm no dir data
    def build(self):
        self.icon = 'figs/kpi_logo.png'
        #self.title = 'LEGEC-APP'

        return Gerenciador()
    #def build(self):
    #    root = ScreenManager()
    #    screen0 = Abertura(name='login')
    #    root.add_widget(screen0)
    #    screen1 = LocalColeta(name='local')
    #    root.add_widget(screen1)



GororobaApp().run()
