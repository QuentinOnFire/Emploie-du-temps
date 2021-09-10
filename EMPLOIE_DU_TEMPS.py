from tkinter import *
import datetime
import qrcode
import os

class App(Tk):

    def __init__(self):
        super().__init__()
        self.anglais = " -Anglais : 1 Cahier 24x32 Vert + le TD ( facultatif )\n"
        self.arts_plastiques = " -Arts Plastique : 1 cahier de travaux pratiques + 1 pochette a rabat\n"
        self.histoire_geo_e_m_c = " -Histoire-Géographie-E.M.C Blanc : 1 Cahier 24x32\n"
        self.fr = " -Francais : 1 pochette a rabat / 1 Classeur + le TD ( facultatif )\n"
        self.maths = " -Mathématiques : 1 Cahier 24x32 rouge + le TD\n"
        self.latin = " -Latin : 1 Cahier 24x32 jaune\n"
        self.physique_chimie = " -Physique-Chimie : 1 Classeur souple jaune\n"
        self.espagnol = " -Espagnol : 1 Cahier 24x32 violet + Manuel\n"
        self.eps = " -Sport : Affaires de sports + gourde\n"
        self.technologie = " -Technologie : 1 Classeur souple noir\n"
        self.svt = " -Science et Vie de la Terre : 1 Cahier 24x32 bleu + 1 Répertoire\n"
        self.musique = " -Musique : 1 Cahier 24x32 blanc\n"
        self.vie_de_classe = " -Vie de classe : Les papiers ( si nécessaire )\n"
        self.pastorale = " -Pastorale : Affaires de pastorale\n"
        self.title("EMPLOIE DU TEMPS")
        self.rien = ""
        self.geometry("1200x800")
        self.font = "Times New Roman", 30
        self.nb_jour = self.b()
        self.nom_jour = self.a()
        self.mois = self.c()
        self.resizable(False, False)
        self.img_qr()
        self.semaine()
        self.bouton()
        self.bouton_reset()
        self.a = False

    def reset(self):
        if self.a:
            self.bouton_valide_nb_day.destroy()
            self.entry_nb_day.destroy()
            self.label_day.destroy()
            self.label_affaires.destroy()
            self.a = False
            self.bouton()
    
    def valider(self):
        self.value_entry = self.entry_nb_day.get()
        if self.value_entry == "1" or self.value_entry == "2" or self.value_entry == "3" or self.value_entry == "4" or self.value_entry == "5":
            self.a = True
            self.value_entry = int(self.value_entry)
            self.bouton_valide_nb_day.destroy()
            self.entry_nb_day.destroy()
            self.label_day.destroy()
            self.affaire()
    
    def affaire(self):
        self.lundi = self.maths + self.eps + self.impaire_paire(self.espagnol, self.physique_chimie) + self.fr + self.histoire_geo_e_m_c + self.latin
        self.mardi = self.impaire_paire(self.svt, self.technologie) + self.musique + self.fr + self.anglais + self.espagnol + self.maths + self.vie_de_classe
        self.mercredi = self.impaire_paire(self.maths, self.rien) + self.histoire_geo_e_m_c + self.svt + self.anglais
        self.jeudi = self.physique_chimie + self.technologie + self.espagnol + self.fr + self.pastorale + self.impaire_paire(self.rien, self.fr) + self.latin
        self.vendredi = self.anglais + self.arts_plastiques + self.histoire_geo_e_m_c + self.fr + self.maths + self.latin

        self.label_affaires = Label(self, font=self.font, text=self.l_m_m_j_v())
        self.label_affaires.pack()
    
    def l_m_m_j_v(self):
        if self.value_entry == 1:
            return self.lundi
        elif self.value_entry == 2:
            return self.mardi
        elif self.value_entry == 3:
            return self.mercredi
        elif self.value_entry == 4:
            return self.jeudi
        elif self.value_entry == 5:
            return self.vendredi
    
    def impaire_paire(self, impaire, paire):
        nbr_week = datetime.datetime.now().isocalendar()[1]
        day = datetime.datetime.now().isocalendar()[2]
        if day == 6 or day == 7:
            nbr_week += 1
        nbr_week = nbr_week / 2
        if ".5" in str(nbr_week):
            return impaire
        else:
            return paire

    
    def bouton_reset(self):
        self.bouton_reset_ = Button(self, font=self.font, text="Réinitialiser", width=11, command=self.reset)
        self.bouton_reset_.place(x=955, y=480)

    def bouton(self):
        self.label_day = Label(self, font=self.font, text=f" -Lundi : 1     \n -Mardi : 2     \n -Mercredi : 3\n -Jeudi : 4      \n -Vendredi : 5")
        self.label_day.pack()
        self.entry_nb_day = Entry(self, font=self.font, width=11)
        self.entry_nb_day.pack()
        self.bouton_valide_nb_day = Button(self, font=self.font, text="Valider", width=10, command=self.valider)
        self.bouton_valide_nb_day.pack()

    def img_qr(self):
        if self.week_impaire():
            qr_impaire = qrcode.make("https://ibb.co/pfsg8VC")
            try:
                os.remove("qr_impaire.png")
            except:
                qr_impaire.save("qr_impaire.png")
            emplacement_img = "qr_impaire.png"
        elif self.week_paire():
            qr_paire = qrcode.make("https://ibb.co/2dYgTF6")
            try:
                os.remove("qr_paire.png")
            except:
                qr_paire.save("qr_paire.png")
            emplacement_img = "qr_paire.png"
        self.width = 300
        self.height = 300
        self.image = PhotoImage(file=emplacement_img).zoom(48).subsample(64)
        self.canvas = Canvas(self, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)
        self.canvas.place(x=930, y=530)
        os.remove(emplacement_img)
        

    def c(self):
        moi = int(str(datetime.date.today()).split('-')[1])
        list_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre' ,'Décembre']
        return list_mois[moi - 1]
    
    def week_impaire(self):
        week = datetime.datetime.now().isocalendar()[1]
        week /= 2
        if ".5" in str(week):
            return True
    
    def week_paire(self):
        week = datetime.datetime.now().isocalendar()[1]
        week /= 2
        if not ".5" in str(week):
            return True

    def b(self):
        today = str(datetime.date.today()).split('-')[2]
        t = int(today)
        if t < 10:
            today = today.replace("0", "")
        return today

    def a(self):
        b = datetime.datetime.now().isocalendar()[2]
        list = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        return list[b]

    def semaine(self):
        self.label_week = Label(self, text=f"Nous sommes le {self.nom_jour} {self.nb_jour} {self.mois}"
                                        f"         Semaine : {datetime.datetime.now().isocalendar()[1]}", font=self.font)
        self.label_week.place(x=20, y=740)

App().mainloop()