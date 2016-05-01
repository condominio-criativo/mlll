#! /usr/bin/env python3
# mlll.py - A Máquina de Libertar Livros Livres

from kivy.garden.router import AppRouter, Router, route
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

#
# Load the templates
#

Builder.load_file('mlll.kv')

#
# instantiate the views
#

class WelcomeScreen(Screen):
    pass

class MetaScreen(Screen):
    pass

class ConsentScreen(Screen):
    pass

class CropScreen(Screen):
    pass

class ScanScreen(Screen):
    pass

class ThankScreen(Screen):
    pass

#
# Setup routing
#

class MainRouter(Router):
    @route("/")
    def index(self):
        return WelcomeScreen()

    @route("/meta")
    def meta(self):
        return MetaScreen()

    @route("/consent")
    def consent(self):
        return ConsentScreen()

    @route("/crop")
    def crop(self):
        return CropScreen()

    @route("/scan")
    def scan(self):
        return ScanScreen()

    @route("/thanks")
    def thanks(self):
        return ThankScreen()

#
# Run app
#

class BookScanApp(AppRouter):
    def build(self):
        self.root = MainRouter()
        self.route = "/"

        
BookScanApp().run()
