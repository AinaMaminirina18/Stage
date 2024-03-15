from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

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
                            md_bg_color: "#fffcf4"
                            selected_color_background: "#e7e4c0"
                            ripple_color_item: "#e7e4c0"
                            on_item_release: app.switch_screen(*args)

                            MDNavigationRailMenuButton:
                                icon:'chevron-left'

                            MDNavigationRailItem:
                                text: "Python"
                                icon: "language-python"

                            MDNavigationRailItem:
                                text: "JavaScript"
                                icon: "language-javascript"

                            MDNavigationRailItem:
                                text: "CPP"
                                icon: "language-cpp"

                            MDNavigationRailItem:
                                text: "Swift"
                                icon: "language-swift"

                        ScreenManager:
                            id: screen_manager
                            transition:
                                FadeTransition(duration=.2, clearcolor=app.theme_cls.bg_dark)
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        Called when tapping on rail menu items. Switches application screens.
        '''

        self.root.ids.screen_manager.current = (
            instance_navigation_rail_item.icon.split("-")[1].lower()
        )

    def on_start(self):
        '''Creates application screens.'''

        navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            name_screen = widget.icon.split("-")[1].lower()
            screen = MDScreen(
                name=name_screen,
                md_bg_color="#edd769",
                radius=[18, 0, 0, 0],
            )
            box = MDBoxLayout(padding="12dp")
            label = MDLabel(
                text=name_screen.capitalize(),
                font_style="H1",
                halign="right",
                adaptive_height=True,
                shorten=True,
            )
            box.add_widget(label)
            screen.add_widget(box)
            self.root.ids.screen_manager.add_widget(screen)


Example().run()