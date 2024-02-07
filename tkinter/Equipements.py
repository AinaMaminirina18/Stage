import tkinter as tk
import customtkinter as ctk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Communication")

        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.frame1 = tk.Frame(self.container)
        self.frame2 = tk.Frame(self.container)
        self.frame3 = tk.Frame(self.container)
        self.frame4 = tk.Frame(self.container)

        self.create_widgets_frame1()
        self.create_widgets_frame2()
        self.create_widgets_frame3()
        self.create_widgets_frame4()

        self.current_frame = None
        self.show_frame(self.frame1)  # Afficher la première page par défaut

    def create_widgets_frame1(self):
        """ label = tk.Label(self.frame1, text="Communication", padx=400, pady=10)
        label.pack()"""
        ecran1 = tk.Frame(self.frame1, padx=300, pady=100)
        ecran1.pack(side=tk.LEFT)
        SMA = tk.Button(ecran1,
                                  text="SMA",
                                  padx=500,
                                  pady=13,
                                  relief=tk.RAISED,
                                  bg='#9C7E43',
                                  fg="white",
                                  font=("Arial", 13))
        SMA.pack(padx=10, pady=10, anchor='center')
        SFA = tk.Button(ecran1,
                                  text="SFA",
                                  padx=51,
                                  pady=10,
                                  relief=tk.RAISED,
                                  bg='#9C7E43',
                                  fg="white",
                                  font=("Arial", 12))
        SFA.pack(padx=10, pady=10)
        CMM = tk.Button(ecran1,
                                  text="COMMUN",
                                  padx=51,
                                  pady=10,
                                  relief=tk.RAISED,
                                  bg='#9C7E43',
                                  fg="white",
                                  font=("Arial", 12))
        CMM.pack(padx=10, pady=10)

    def create_widgets_frame2(self):
        label = tk.Label(self.frame2, text="Méteo", padx=400, pady=10)
        label.pack()

    def create_widgets_frame3(self):
        label = tk.Label(self.frame3, text="Reseautique", padx=400, pady=10)
        label.pack()

    def create_widgets_frame4(self):
        label = tk.Label(self.frame4, text="Surveillance", padx=400, pady=10)
        label.pack()

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()  # Cacher le cadre actuel

        frame.pack(fill="both", expand=True)  # Afficher le cadre spécifié
        self.current_frame = frame


def set_button_color(buttons, current_button):
    current_button.config(bg="#9C7E43", fg="white")
    for button in buttons:
        if button != current_button:
            button.config(bg="SystemButtonFace", fg="black")


def quitter():
    msgbox = tk.messagebox.askquestion("Quiter l'application", "Vous voulez vraiment quitter?", icon="error")
    if msgbox == "yes":
        root.destroy()
def title_page( str):
    root.title(str)



if __name__ == "__main__":
    root = tk.Tk()

    """root.attributes('-fullscreen', True)"""
    root.bind('<Escape>', lambda e: quitter())
    root.geometry("1000x600+150+50")
    root.resizable(False, False)

    frame = tk.Frame(root, bg='#9C7E43')
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame.grid_propagate(False)

    # Bouton sur le côté

    button_frame1 = tk.Button(frame,
                              text="Communication",
                              command=lambda: [set_button_color([button_frame2, button_frame3, button_frame4], button_frame1),
                                               app.show_frame(app.frame1), title_page("Communication")],
                              padx=51,
                              pady=10,
                              relief=tk.RAISED,
                              bg='#9C7E43',
                              fg="white",
                              font=("Arial", 12))
    button_frame1.pack(padx=10, pady=10)

    button_frame2 = tk.Button(frame,
                              text="Méteo",
                              command=lambda: [set_button_color([button_frame1, button_frame3, button_frame4], button_frame2),
                                               app.show_frame(app.frame2), title_page("Méteo")],
                              padx=82,
                              pady=10,
                              relief=tk.RAISED,
                              font=("Arial", 12))
    button_frame2.pack(padx=10, pady=10, anchor='s')

    button_frame3 = tk.Button(frame,
                              text="Reseautique",
                              command=lambda: [set_button_color([button_frame1, button_frame2, button_frame4], button_frame3),
                                               app.show_frame(app.frame3), title_page("Reseautique")],
                              padx=60,
                              pady=10,
                              relief=tk.RAISED,
                              font=("Arial", 12))
    button_frame3.pack(padx=10, pady=10)

    button_frame4 = tk.Button(frame,
                              text="Surveillance",
                              command=lambda: [set_button_color([button_frame1, button_frame2, button_frame3], button_frame4),
                                               app.show_frame(app.frame4), title_page("Surveillance")],
                              padx=62,
                              pady=10,
                              relief=tk.RAISED,
                              font=("Arial", 12))
    button_frame4.pack(padx=10, pady=10)

    Quit = ctk.CTkButton(frame, text="Quitter", font=("Arial", 15), fg_color='#393535', hover_color='#BE0707', command=quitter)
    Quit.pack(padx=10, pady=10, side=tk.BOTTOM)

    app = MyApp(root)

    root.mainloop()