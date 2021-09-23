from tkinter import *
import webbrowser
import datetime
import qrcode
import os

class App(Tk):

    def __init__(self):
        super().__init__()
        self.anglais = " -Anglais : 1 Cahier 24x32 + le TD ( facultatif )\n"
        self.arts_plastiques = " -Arts Plastique : 1 Cahier de travaux pratiques + 1 pochette a rabat\n"
        self.histoire_geo_e_m_c = " -Histoire-Géographie-E.M.C : 1 Cahier 24x32\n"
        self.fr = " -Francais : 1 Pochette a rabat + le TD ( facultatif )\n"
        self.maths = " -Mathématiques : 1 Cahier 24x32 + le TD\n"
        self.latin = " -Latin : 1 Cahier 24x32 \n"
        self.physique_chimie = " -Physique-Chimie : 1 Classeur souple + Manuel\n"
        self.espagnol = " -Espagnol : 1 Cahier 24x32 + Manuel\n"
        self.eps = " -Sport : Affaires de sports + gourde\n"
        self.technologie = " -Technologie : 1 Classeur souple\n"
        self.svt = " -Science et Vie de la Terre : 1 Cahier 24x32 + 1 Répertoire\n"
        self.musique = " -Musique : 1 Cahier 24x32\n"
        self.vie_de_classe = " -Vie de classe : Les papiers ( si nécessaire )\n"
        self.allemand = " -Allemand : 1 Cahier 24x32 + Manuel\n"
        self.italien = " -Italien : 1 Cahier 24x32 + Manuel + TD\n"
        self.pastorale = " -Pastorale : Affaires de pastorale\n"
        self.title("EMPLOIE DU TEMPS")
        self.rien = ""
        self.color = "aqua"
        self.geometry("1200x800")
        self.config(bg=self.color)
        self.font = "Times New Roman", 30
        self.resizable(False, False)
        self.copyright()
        self.code()
        self.img_jp()
        self.lv_deux()
    
    def code(self):
        self.button_code = Button(self, font=self.font, text="Lien vers le code", command=self.lien_code, bg=self.color)
        self.button_code.place(x=0, y=600)
    
    def lien_code(self):
        webbrowser.open_new("https://github.com/QuentinOnFire/Emploie-du-temps/")
    
    def copyright(self):
        self.label_copyright = Label(self, font=self.font, bg=self.color, text="Quentin\n BORRAS ©")
        self.label_copyright.place(x=-10, y=500)
    
    def img_qr(self):
        if self.week_impaire():
            qr_impaire = qrcode.QRCode()
            qr_impaire.add_data("https://ibb.co/pfsg8VC")
            qr_impaire = qr_impaire.make_image(back_color="aqua")
            try:
                os.remove("qr_impaire.png")
            except:
                qr_impaire.save("qr_impaire.png")
            emplacement_img = "qr_impaire.png"
        elif self.week_paire():
            qr_paire = qrcode.QRCode()
            qr_paire.add_data("https://ibb.co/2dYgTF6")
            qr_paire = qr_paire.make_image(back_color="aqua")
            try:
                os.remove("qr_paire.png")
            except:
                qr_paire.save("qr_paire.png")
            emplacement_img = "qr_paire.png"
        self.width = 300
        self.height = 300
        self.image = PhotoImage(file=emplacement_img).zoom(48).subsample(64)
        self.canvas = Canvas(self, width=self.width, height=self.height, bd=0, highlightthickness=0, bg=self.color)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)
        self.canvas.place(x=930, y=530)
        os.remove(emplacement_img)
        self.label_qr = Label(self, font=self.font, text="Lien vers l'emploie du temps :", bg=self.color)
        self.label_qr_deux = Label(self, font=self.font, text="SCAN LE QRCODE !", bg=self.color)
        self.label_qr.place(x=470, y=550)
        self.label_qr_deux.place(x=470, y=600)
    
    def img_jp(self):
        self.wi = 257
        self.he = 245
        self.img_jp = PhotoImage(file="img/jp2.png").zoom(48).subsample(64)
        self.canvas_jp = Canvas(self, width=self.wi, height=self.he, bd=0, highlightthickness=0, bg=self.color)
        self.canvas_jp.create_image(self.wi / 2, self.he / 2, image=self.img_jp)
        self.canvas_jp.place(x=-30, y=-35)
        self.label_class = Label(self, font=self.font, bg=self.color, text="Classe : 4°2")
        self.label_class.place(x=0, y=180)
    
    def latin_y_n(self):
        if self.latin_yes_no:
            return self.latin
        else:
            return self.rien
    
    def lv_deux(self):
        self.label_question_lv_deux = Label(self, font=self.font, text="Quelle est votre langue LV2 ? ", bg=self.color)
        self.label_question_lv_deux.place(x=400, y=200)
        self.button_allemand = Button(self, font=self.font, text="ALLEMAND", command=self.lv_deux_allemand, bg=self.color)
        self.button_espagnol = Button(self, font=self.font, text="ESPAGNOL", command=self.lv_deux_espagnol, bg=self.color)
        self.button_italien = Button(self, font=self.font, text="ITALIEN", command=self.lv_deux_italien, bg=self.color)
        self.button_allemand.place(x=290, y=300)
        self.button_espagnol.place(x=545, y=300)
        self.button_italien.place(x=784, y=300)
    
    def lv_deux_italien(self):
        self.lv = self.italien
        self.suppr_lv_deux()

    def lv_deux_espagnol(self):
        self.lv = self.espagnol
        self.suppr_lv_deux()

    def lv_deux_allemand(self):
        self.lv = self.allemand
        self.suppr_lv_deux()
    
    def suppr_lv_deux(self):
        self.label_question_lv_deux.destroy()
        self.button_allemand.destroy()
        self.button_espagnol.destroy()
        self.button_italien.destroy()
        self.question_latin()
    
    def question_latin(self):
        self.label_latin = Label(self, text="Faites-vous latin ?", font=self.font, bg=self.color)
        self.button_yes = Button(self, font=self.font, text="Oui", command=self.latin_yes, bg=self.color)
        self.button_no = Button(self, font=self.font, text="Non", command=self.latin_no, bg=self.color)
        self.label_latin.place(x=450, y=200)
        self.button_yes.place(x=487, y=300)
        self.button_no.place(x=580, y=300)

    def suppr_latin(self):
        self.label_latin.destroy()
        self.button_no.destroy()
        self.button_yes.destroy()
        self.apres()

    def latin_yes(self):
        self.latin_yes_no = True
        self.suppr_latin()
    
    def latin_no(self):
        self.latin_yes_no = False
        self.suppr_latin()

    def apres(self):
        self.nb_jour = self.b()
        self.nom_jour = self.a()
        self.mois = self.c()
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
        self.lundi = self.maths + self.eps + self.impaire_paire(self.lv, self.physique_chimie) + self.fr + self.histoire_geo_e_m_c + self.latin_y_n()
        self.mardi = self.impaire_paire(self.svt, self.technologie) + self.musique + self.fr + self.anglais + self.lv + self.maths + self.vie_de_classe
        self.mercredi = self.impaire_paire(self.maths, self.rien) + self.histoire_geo_e_m_c + self.svt + self.anglais
        self.jeudi = self.physique_chimie + self.technologie + self.lv + self.fr + self.pastorale + self.impaire_paire(self.rien, self.fr) + self.latin_y_n()
        self.vendredi = self.anglais + self.arts_plastiques + self.histoire_geo_e_m_c + self.fr + self.maths + self.latin_y_n()
        self.label_affaires = Label(self, font=self.font, text=self.l_m_m_j_v(), bg=self.color)
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
        if day == 6 or day == 7 or day == 5:
            nbr_week += 1
        nbr_week = nbr_week / 2
        if ".5" in str(nbr_week):
            return impaire
        else:
            return paire

    
    def bouton_reset(self):
        self.bouton_reset_ = Button(self, font=self.font, text="Réinitialiser", width=11, command=self.reset, bg=self.color)
        self.bouton_reset_.place(x=955, y=480)

    def bouton(self):
        self.label_day = Label(self, font=self.font, text=f" -Lundi : 1     \n -Mardi : 2     \n -Mercredi : 3\n -Jeudi : 4      \n -Vendredi : 5", bg=self.color)
        self.label_day.pack()
        self.entry_nb_day = Entry(self, font=self.font, width=11, bg=self.color)
        self.entry_nb_day.pack()
        self.bouton_valide_nb_day = Button(self, font=self.font, text="Valider", width=10, command=self.valider, bg=self.color)
        self.bouton_valide_nb_day.pack()

    



    def c(self):
        moi = int(str(datetime.date.today()).split('-')[1])
        list_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre' ,'Décembre']
        return list_mois[moi - 1]
    
    def week_impaire(self):
        week = datetime.datetime.now().isocalendar()[1]
        jour = datetime.datetime.now().isocalendar()[2]
        if jour == 6 or jour == 7:
            week += 1
        week /= 2
        if ".5" in str(week):
            return True
    
    def week_paire(self):
        week = datetime.datetime.now().isocalendar()[1]
        jour = datetime.datetime.now().isocalendar()[2]
        if jour == 6 or jour == 7:
            week += 1
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
        return list[b - 1]

    def semaine(self):
        self.label_week = Label(self, text=f"Nous sommes le {self.nom_jour} {self.nb_jour} {self.mois}"
                                        f"       Semaine : {datetime.datetime.now().isocalendar()[1]}", font=self.font, bg=self.color)
        self.label_week.place(x=20, y=740)

App().mainloop()
