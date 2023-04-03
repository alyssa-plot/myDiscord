import tkinter as tk
from database import Database
from client import Client
import threading

class Discord:
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.title("My Discord")
        self.gui.geometry("420x490")
        self.gui.configure(bg="#36393f")

        #Création de boutons pour se connecter à notre compte déjà crée.
        self.mail1 = tk.Label(self.gui, text="adresse mail:", bg= "#36393f", fg="white", font=('Arial', 12))
        self.mail1.grid(column=0, row=0, padx=10, pady=10)
        self.entry_mail1 = tk.Entry(self.gui, width=25)
        self.entry_mail1.grid(column=1, row=0, padx=10, pady=10)

        self.password1 = tk.Label(self.gui, text="mot de passe:", bg="#36393f", fg="white", font=('Arial', 12))
        self.password1.grid(column=0, row=1, padx=10, pady=10)
        self.entry_password1 = tk.Entry(self.gui, width=25, show="*")
        self.entry_password1.grid(column=1, row=1, padx=10, pady=10)

        self.button1 = tk.Button(self.gui, text="Connexion", bg="#7289da", fg="white", font=('Arial', 12), command=self.login)
        self.button1.grid(columnspan=2, row=2, padx=10, pady=10)

        #Création de boutons, cette fois-ci pour se créer un compte
        self.first_name = tk.Label(self.gui, text="prénom:", bg="#36393f", fg="white", font=('Arial', 12))
        self.first_name.grid(column=0, row=3, padx=10, pady=10)
        self.entry_first_name = tk.Entry(self.gui, width=25)
        self.entry_first_name.grid(column=1, row=3, padx=10, pady=10)

        self.last_name = tk.Label(self.gui, text="nom:", bg="#36393f", fg="white", font=('Arial', 12))
        self.last_name.grid(column=0, row=4, padx=10, pady=10)
        self.entry_last_name = tk.Entry(self.gui, width=25)
        self.entry_last_name.grid(column=1, row=4, padx=10, pady=10)

        self.mail2 = tk.Label(self.gui, text="adresse mail:", bg="#36393f", fg="white", font=('Arial', 12))
        self.mail2.grid(column=0, row=5, padx=10, pady=10)
        self.entry_mail2 = tk.Entry(self.gui, width=25)
        self.entry_mail2.grid(column=1, row=5, padx=10, pady=10)

        self.password2 = tk.Label(self.gui, text="mot de passe:", bg="#36393f", fg="white", font=('Arial', 12))
        self.password2.grid(column=0, row=6, padx=10, pady=10)
        self.entry_password2 = tk.Entry(self.gui, width=25, show="*")
        self.entry_password2.grid(column=1, row=6, padx=10, pady=10)

        self.button2 = tk.Button(self.gui, text="Inscription", bg="#7289da", fg="white", font=('Arial', 12), command=self.add)
        self.button2.grid(columnspan=2,row=7)

        self.gui.mainloop()

    def add(self):
        self.prenom = self.entry_first_name.get()
        self.nom = self.entry_last_name.get()
        self.email = self.entry_mail2.get()
        self.mot_de_passe = self.entry_password2.get()

        if not self.prenom or not self.nom or not self.email or not self.mot_de_passe:
            fail_label = tk.Label(self.gui, text="L'utilisateur n'a pas été créé car une des conditions n'est pas respectée.", fg="red",bg="#313338")
            fail_label.grid(row=9, column=0, columnspan=2)
            return

        db = Database()
        db.cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",(self.prenom, self.nom, self.email, self.mot_de_passe))
        db.mydb.commit()
        if db.cursor.rowcount == db.cursor.rowcount==+1:
            success_label = tk.Label(self.gui, text="L'utilisateur a été créé avec succès.", fg="green",bg="#313338")
            success_label.grid(row=9, column=0, columnspan=2)

    def login(self):
        self.email = self.entry_mail1.get()
        self.mot_de_passe = self.entry_password1.get()
        db = Database()
        #HOST = 'localhost'
        #PORT = 1234
        db.cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.email, self.mot_de_passe))
        user = db.cursor.fetchone()
        if user:
            success_label = tk.Label(self.gui, text="Vous vous êtes connecté(e) avec succès.", fg="green", bg="#313338")
            success_label.grid(row=3, column=0, columnspan=2)
            #client = Client(HOST, PORT)
            #if client.pseudo:
                #client.receive_thread = threading.Thread(target=client.receive)
                #client.receive_thread.start()
                #client.gui_done = True
                #client.interface()
        else:
            fail_label = tk.Label(self.gui, text="Utilisateur ou mot de passe invalide.", fg="red", bg="#313338")
            fail_label.grid(row=3, column=0, columnspan=2)

Discord()