from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.pickers import MDTimePicker, MDDatePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
import mysql.connector
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from datetime import datetime

Window.size = (1100, 650)
Window.left = 120
Window.top = 60

Window.minimum_height = 650  # Définit la taille minimale de la hauteur
Window.minimum_width = 1100

connection = mysql.connector.connect(
    user='root',
    password='Asecna2024',
    host='localhost',
    database='panne')

mycursor = connection.cursor()
cat = ''


class MainApp(MDApp):
    """def on_start(self):
        mycursor.execute("SELECT COUNT(identifiant) FROM login")
        result = mycursor.fetchone()
        if result[0] == 0:
            self.root.current = "creation"
        else:
            self.root.current = "login" """

    def build(self):
        self.icon = "Logo.png"
        self.title = "Rapport de maintenance"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Lime"
        screen = ScreenManager()
        screen.transition.duration = .5
        screen.add_widget(Builder.load_file("Fin.kv"))
        screen.add_widget(Builder.load_file("equip.kv"))
        screen.add_widget(Builder.load_file('login.kv'))
        screen.add_widget(Builder.load_file('Creation.kv'))
        screen.add_widget(Builder.load_file("Choice.kv"))
        return screen

    def log_in(self, user_input, password_input):
        if not user_input or not password_input:
            self.show_dialog("Attention!!", "Les deux champs sont vides")
            return
        query = """
            SELECT prenom, sexe
            FROM login 
            WHERE identifiant = %s AND motdepasse = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query, (user_input, password_input))
            user_data = cursor.fetchone()
            if user_data:
                prenom, sexe = user_data
                ts = 'Mr' if sexe.upper() == 'H' else 'Mme'
                self.root.current = 'centre'
                self.root.transition.direction = 'left'
                self.root.get_screen('login').ids.user.text = ''
                self.root.get_screen('login').ids.password.text = ''
                self.show_dialog("Connexion réussie", f"Bienvenue {ts} {prenom}")
            else:
                self.show_dialog("Erreur", "Veuillez vérifier vos identifiants et mot de passe.")

    def new_account(self, nom, prenom, sexe, identifiant, mdp, rmdp):
        if not nom or not prenom or not sexe or not identifiant or not mdp:
            self.show_dialog("Attention", "Veuillez compléter tous les champs.")
            return
        if mdp != rmdp:
            self.show_dialog("Attention", "Les mots de passe ne correspondent pas. Veuillez les vérifier.")
            return
        if len(sexe) > 1:
            self.show_dialog('Attention', 'Veuillez verifier les champs')
            return

        inscription_query = """
            INSERT INTO login(nom, prenom, sexe, identifiant, motdepasse) 
            VALUES (%(nom)s, %(prenom)s, %(sexe)s, %(identifiant)s, %(mdp)s)
        """
        with connection.cursor() as cursor:
            try:
                cursor.execute(inscription_query,
                               {'nom': nom,
                                'prenom': prenom,
                                'sexe': sexe.upper(),
                                'identifiant': identifiant,
                                'mdp': mdp})
                connection.commit()
                self.show_dialog("Félicitations", "Votre compte a bien été créé.")
                self.root.current = 'centre'
                self.root.transition.direction = 'left'
                self.clear_creation_fields('creation')
            except Exception as e:
                self.show_dialog("Erreur", f"Une erreur est survenue : {str(e)}")

    def clear_creation_fields(self, choix):
        creation_screen = self.root.get_screen('creation')
        ajout_screen = self.root.get_screen('rapport')
        creation = ['nom', 'prenom', 'sx', 'ident', 'mdp', 'rmdp']
        ajout = ['date', 'cat', 'nom_equip', 'se', 'debut', 'fin']
        if choix == 'creation':
            for field_id in creation:
                creation_screen.ids[field_id].text = ''
        if choix == 'ajout':
            for field_id in ajout:
                ajout_screen.ids[field_id].text = ''

    def show_time_picker(self, textfield_instance, value):
        # Open time picker dialog.
        from datetime import datetime
        if value and textfield_instance.focus:
            # print(f"ID de l'objet dans show_time_picker : {textfield_instance.hint_text}")
            time_picker = MDTimePicker()
            time_picker.bind(on_save=lambda instance, time: self.on_time_picker_dismiss(textfield_instance.hint_text, time))
            time_picker.set_time(datetime.today().time())
            time_picker.open()

    def on_time_picker_dismiss(self, input_id, time):
        rapport_screen = self.root.get_screen("rapport")
        rapport_screen.ids[input_id].text = str(time)

    def choix(self, instance):
        if instance in self.root.get_screen('rapport').ids.values():
            global cat
            current_id = list(self.root.get_screen('rapport').ids.keys())[list(self.root.get_screen('rapport').ids.values()).index(instance)]
            # print(current_id)
            for i in range(4):
                self.root.get_screen('rapport').ids.lab_cat.text = 'Catégorie: ' if not current_id == 'nav_icon4' else 'Station:'
                self.root.get_screen('rapport').ids.cat.disabled = False if current_id in {'nav_icon1', 'nav_icon4'} else True
                self.root.get_screen('rapport').ids.cat.line_color_normal = 'white' if current_id in {'nav_icon1', 'nav_icon4'} else '#377BFF'
                self.root.get_screen('rapport').ids.cat.fill_color_normal = 'white' if current_id in {'nav_icon1', 'nav_icon4'} else '#377BFF'
                self.root.get_screen('rapport').ids.lab_cat.text_color = 'white' if current_id in {'nav_icon1', 'nav_icon4'} else '#377BFF'
                if f"nav_icon{i+1}" == current_id:
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].md_bg_color = '#19F498'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].text_color = 'black'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].icon_color = 'black'
                    self.root.get_screen('rapport').ids.cat.text = ''
                    cat = self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].text
                else:
                    self.root.get_screen('rapport').ids[f"nav_icon{i + 1}"].md_bg_color = 'white'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].text_color = 'black'
                    self.root.get_screen('rapport').ids[f"nav_icon{i+1}"].icon_color = 'black'

    def reset(self):
        for i in range(1, 4):
            self.root.get_screen('rapport').ids[f"nav_icon{i}"].md_bg_color = 'white'
            global cat
            cat = ''

    def show_dialog(self, titre, affiche):
        buttons = [MDFlatButton(
                    text='OK' if titre != 'Deconnexion' else 'Oui',
                    on_release=self.dismiss_dialog)]

        if titre == 'Deconnexion':
            buttons.append(MDFlatButton(
                    text='Non',
                    on_release=self.fermer))
        self.dialog = MDDialog(
            title=titre,
            text=affiche,
            buttons=buttons
        )
        self.dialog.open()

    def dismiss_dialog(self, *args):
        if self.dialog.title != "Deconnexion":
            self.dialog.dismiss()
        else:
            self.root.current = "login"
            self.dialog.dismiss()

    def fermer(self, *args):
        self.dialog.dismiss()

    def show_date_picker(self):
        date_dialog = MDDatePicker(primary_color='#F5EC0E')
        date_dialog.open()
        date_dialog.bind(on_save=self.on_save_date)

    def on_save_date(self, instance, value, date_range):
        # print(instance, value,date_ra
        # nge)
        self.root.get_screen("rapport").ids.date.text = str(value.strftime("%Y/%m/%d"))

    def enregistrer(self, date, categ, nom, sou_eq, hd, hf):
        if not date or not nom or not hd or not hf:
            self.show_dialog("Attention", "Veuillez compléter tous les champs.")
            return

        if not cat:
            self.show_dialog("Attention", "Choisissez un département")
            return
        
        hdebut = datetime.strptime(hd, "%H:%M:%S")
        hfin = datetime.strptime(hf, "%H:%M:%S")

        diff = hfin - hdebut
        diff_heures = diff.seconds // 3600
        diff_minutes = (diff.seconds % 3600) // 60
        hd = diff_heures + (diff_minutes / 60)
        heure_def = "{:.2f}".format(hd)
        hm = 24 - hd
        heure_norm = "{:.2f}".format(hm)
        print(cat, date, categ, nom, sou_eq)
        print(f'{diff_heures } heure et {diff_minutes} minutes et donc {heure_def}')
        # self.clear_creation_fields('ajout')
        print(cat)

        query_ajout = f'INSERT INTO {cat}(date_panne,categ,equip,se,h_normal,h_def) VALUES (%s,%s ,%s ,%s, %s , %s)'
        ajout_query = f'INSERT INTO {cat}(date_panne,equip,se,h_normal,h_def) VALUES (%s,%s ,%s ,%s, %s)'
        with connection.cursor() as cursor:
            try:
                if cat in {"Communication", "Surveillance"}:
                    cursor.execute(query_ajout,
                                   (date, categ, nom, sou_eq, heure_norm, heure_def))
                    connection.commit()
                if cat in {"Méteo", "Réseau"}:
                    cursor.execute(ajout_query,
                                   (date, nom, sou_eq, heure_norm, heure_def))
                    connection.commit()
                self.show_dialog("Alert !!", "Ca a bien été enregistrer.")
                self.reset()
            except Exception as e:
                self.show_dialog("Erreur", f"Une erreur est survenue : {str(e)}")
                print(str(e))

    def on_start(self):
        navigation_rail_items = self.root.get_screen('Export').ids.navigation_rail.get_items()[:]
        navigation_rail_items.reverse()

        for widget in navigation_rail_items:
            name_screen = widget.icon.split("-")[1].lower()
            screen = MDScreen(
                name=name_screen,
            )
            box = MDBoxLayout(
                pos_hint={"center_x": 0.5, 'center_y': 0.5},
                padding="24dp",
            )
            data_tables = MDDataTable(
                pos_hint={"center_y": 0.5, "center_x": 0.5},
                size_hint=(0.9, 0.7),
                use_pagination=False,
                column_data=[
                    ("Date", dp(25)),
                    ("Catégories", dp(25)),
                    ("Nom équipements", dp(40)),
                    ("Sous-ensemble", dp(40)),
                    ("Heure normal", dp(25)),
                    ("Heure normal", dp(25))
                ],
                row_data=[("31 Septembre", "SFA", "VHF", "EQTS E/R ens.1", "24", "0")],
            )
            # Adding a table and buttons to the toot layout.
            box.add_widget(data_tables)
            screen.add_widget(box)
            self.root.get_screen('Export').ids.screen_manager.add_widget(screen)

    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        Called when tapping on rail menu items. Switches application screens.
        '''

        self.root.get_screen('Export').ids.screen_manager.current = (
            instance_navigation_rail_item.icon.split("-")[1].lower()
        )


if __name__ == "__main__":
    LabelBase.register(name='poppins',
                       fn_regular='./fonts/Poppins/Poppins-SemiBold.ttf')
    MainApp().run()
