from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.garden import mapview

Window.size = (300,500)

__version__ = "1.0.0"

screen_helper = """
#:import MapView kivy.garden.mapview.MapView
Screen:
	MDNavigationLayout:
		ScreenManager:
			Screen:
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Navigation'
						left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
						elevation: 10
					MapView:
						id: mapview
						lat: 51.44465290828848
						lon: 7.261104080810651
						zoom: 19
						on_lat:
							print(self.lat)
						on_lon:
							print(self.lon)
						MapMarker:
							id: ziel
							source: "flag.png"
							lat: 51.44465290828848
							lon: 7.261104080810651
						MapMarker:
							id: start
							source: "directions_walk.png"
							lat: 51.44477160176767
							lon:7.259752247467162

		MDNavigationDrawer:
			id: nav_drawer
			type: "standard"
			close_on_click: True
			BoxLayout:
				orientation: 'vertical'
				Image:
					source: 'RUB-Logo.png'
					size_hint_y: None
				MDBoxLayout:
					adaptive_height: True
					MDIconButton:
						icon: 'magnify'
					MDTextField:
						id: search_field
						hint_text: 'Find Room'
						on_text: Main().printText(self.text)
				ScrollView:
					MDList:
						id: list
						OneLineListItem:
							text: 'H1'
							on_press: print("H1")
						OneLineListItem:
							text: 'H2'
							on_press: print("H2")
						OneLineListItem:
							text: 'H3'
							on_press: print("H3")
						OneLineListItem:
							text: 'H4'
							on_press: print("H4")
						OneLineListItem:
							text: 'H5'
							on_press: print("H5")
						OneLineListItem:
							text: 'H6'
							on_press: print("H6")
						OneLineListItem:
							text: 'H7'
							on_press: print("H7")
						OneLineListItem:
							text: 'H8'
							on_press: print("H8")
"""

class Main(MDApp):

	def build(self):
		self.theme_cls.primary_palette = "Indigo"
		screen = Builder.load_string(screen_helper)
		return screen

if __name__ == "__main__":
	Main().run() 
