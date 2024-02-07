from kivy.lang import Builder
from kivymd.app import MDApp
import datetime

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition


MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDBoxLayout:

                        MDNavigationRail:
                            id: navigation_rail
                            md_bg_color: "#9C7E43"
                            selected_color_background: "#e7e4c0"
                            ripple_color_item: "#e7e4c0"
                            on_item_release: app.switch_screen(*args)
                            type: "selected"
                            width : 100
                            anchor: "center"

                            MDNavigationRailItem:
                                text: "Communication"
                                icon: "phone"

                            MDNavigationRailItem:
                                text: "Méteo"
                                icon: "sun-snowflake"

                            MDNavigationRailItem:
                                text: "Réseau"
                                icon: "network"

                            MDNavigationRailItem:
                                text: "Surveillance"
                                icon: "table-check"

                        ScreenManager:
                            id: screen_manager
                            transition:
                                FadeTransition(duration=.5)

'''


class Example(MDApp):
    def build(self):
        self.icon = "Logo.png"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def update_date(self, dt):
        # Mettre à jour l'étiquette avec la date d'aujourd'hui
        today = datetime.today()
        self.label.text = f'Date d\'aujourd\'hui: {today.strftime("%Y-%m-%d")}'

    def switch_screen(
            self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        Called when tapping on rail menu items. Switches application screens.
        '''

        self.root.ids.screen_manager.current = (
            instance_navigation_rail_item.text
        )

    def on_start(self):

        navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            name_screen = widget.text
            self.root.ids.screen_manager.add_widget(Builder.load_file("./" + name_screen + "/main.kv"))


Example().run()
