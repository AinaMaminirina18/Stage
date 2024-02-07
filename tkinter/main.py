import tkinter
import customtkinter as ctk
import subprocess
from tkinter import messagebox



def quitter():
    messagebox.askyesno('Attention', "Voulez-vous quitter?")
    login.destroy()


def Verification(id, mdp):
    if id == '' and mdp == '':
        messagebox.showwarning('Erreur', 'Veuillez completer les champs')
    else:
        if id.lower() == 'admin':
            if mdp.capitalize() == 'Asecna':
                login.destroy()
                subprocess.call(["python", "Equipements.py"])

            else:
                messagebox.showwarning('Erreur', 'Verifier votre Mot de passe')
        else:
            messagebox.showwarning('Erreur', 'Verifier votre identifiant')


ctk.set_appearance_mode("light")


login = ctk.CTk()
"""login.attributes('-alpha', True)
login.bind('<Enter>', lambda e: Verification(Id.get().lower(), Mdp.get().lower()))"""
login.geometry("600x350+150+50")
login.title("Authentification")
login.resizable(False, False)

frame = ctk.CTkFrame(login)
frame.pack(pady=40,
           padx=60,
           fill="both",
           expand=True)

label = ctk.CTkLabel(frame,
                     text="Valider votre identiter",
                     font=("Arial", 25))
label.pack(pady=15,
           padx=10)

Id = ctk.CTkEntry(frame,
                  placeholder_text="Identifiant",
                  width=250,
                  height=40,
                  font=("Arial", 15),
                  corner_radius=20)
Id.pack(pady=12)

Mdp = ctk.CTkEntry(frame,
                   placeholder_text="Mot de passe",
                   show="*",
                   width=250,
                   height=40,
                   font=("Arial", 15),
                   corner_radius=20)
Mdp.pack(pady=12, anchor='center')

button = ctk.CTkButton(frame,
                       text="Entrer",
                       command=lambda: Verification(Id.get(), Mdp.get()),
                       width=400,
                       font=('Arial', 18),
                       fg_color='#503604',
                       hover_color='#9C7E43',
                       corner_radius=20)
button.pack(pady=30)

login.mainloop()
