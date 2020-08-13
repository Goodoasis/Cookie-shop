# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:31:07 2020
@author: GoodOasis
Exercice proposé par Graven www.youtube.com/channel/UCIHVyohXw6j2T-83-uLngEg
J'ai été un peu plus loin avec une POO
"""

from tkinter import *
from variable import *
from text import *


class CookieShop:

    """
    Frame principal en haut qui tient le label principal
    Frame central avec une image de cookie
    Frame à droite contient "la cuisine"
    Frame à gauche contient la "boutique"
    Le but est de cliquer pour confectionner des cookies
    Puis le revendre afin de se faire de l'argent
    Des point de skills sont apres un certain avec bcp fabriquer et vendu
    """

    def __init__(self):
        # Initialisation de la fenetre principale
        self.window = Tk()
        self.window.title("Cookie Shop")
        self.window.geometry("850x357")
        self.window.minsize(600, 320)
        self.window.iconbitmap("cookie.ico")
        self.window.config(background=marron)
        # Initialisation des variable de class
        self.cookie_count = 0
        self.pastry_skill = 1
        self.cookie_starting_price = 1
        self.seller_skill = 1
        self.cashier = 0
        self.image_cookie = None
        # Initialisation des elements
        self.frame = Frame(self.window, bg=marron)
        self.frame_central = Frame(self.frame, bg=marron)
        # Sub_frame dans frame central
        self.frame_kitchen = Frame(self.frame_central, bg=marron)
        self.frame_shop = Frame(self.frame_central, bg=marron)
        # Creation des widgets
        self.create_widgets()
        # Empactage
        self.frame.pack(expand=YES)
        self.frame_central.grid(row=1, column=0, sticky=S)
        self.frame_kitchen.grid(row=0, column=2, sticky=E)
        self.frame_shop.grid(row=0, column=0, sticky=W)

    def create_widgets(self):
        """"Initialise les fonction de creation de widgets"""
        # Frame central et canvas central
        self.create_title()
        self.create_canvas()
        # Frame kitchen
        self.create_title_kitchen()
        self.create_cookie_counter()
        self.create_button_counter()
        # Frame Shop
        self.create_title_shop()
        self.create_cashier()
        self.create_button_seller()

    # Frame Central
    def create_title(self):
        """Ajout du message général de bienvenue"""
        label_title = Label(self.frame, text=welcome,
                            font=("Courrier", 25, 'bold'),
                            bg=marron, fg=brun_claire)
        label_title.grid(row=0, column=0, sticky=N)

    def create_canvas(self):
        """Ajout d'un canvas pour y contenir
        l'image de cookie central."""
        self.image_cookie = PhotoImage(file="cookie.png"
                                       ).zoom(3).subsample(5)
        canvas = Canvas(self.frame_central, width=width, height=height,
                        bg=marron, highlightthickness=0)
        canvas.create_image(width/2, height/2, image=self.image_cookie)
        canvas.grid(row=0, column=1, sticky=N)

    # Frame Kitchen
    def create_title_kitchen(self):
        """Ajout du message en haut de la frame kitchen
        qui invite l'utilisateur à cliquer pour creer des cookies."""
        title_kitchen = Label(self.frame_kitchen, text=label_kitchen,
                              font=("Courrier", 20), bg=marron, fg=brun_claire)
        title_kitchen.pack(side=TOP)

    def create_cookie_counter(self):
        """"Ajout d'un compteur de cookie pour compter les cliques
        de l'utilisateurs."""
        self.label_cookie_counter = Label(self.frame_kitchen,
                                          text=self.cookie_count,
                                          font=("Courrier", 80, 'bold'),
                                          bg=marron, fg=brun_claire)
        self.label_cookie_counter.pack(expand=YES)

    def create_button_counter(self):
        """Ajout d'un bouton en bas de la frame kitchen
        pour creer des cookies."""
        button_counter = Button(self.frame_kitchen,
                                text=bake_cookie, bg=marron,
                                fg=brun_claire, activebackground=marron_fonce,
                                command=self.make_cookie)
        button_counter.pack(pady=2, padx=2, side=BOTTOM, fill=X)

    def refresh_cookie_counter(self):
        """Fonction qui actualise le compteur de cookie."""
        return self.label_cookie_counter.config(text=self.cookie_count)

    # Frame Shop
    def create_title_shop(self):
        """Ajout du message en haut de la frame Shop
        qui invite l'utilisateur a cliquer pour vendre qes cookies."""
        title_shop = Label(self.frame_shop, text=label_shop,
                           font=("Courrier", 20), bg=marron, fg=brun_claire)
        title_shop.pack(side=TOP)

    def create_cashier(self):
        """"Ajout d'un label au centre de la frame Shop,
        qui affiche l'argent généré par la vente des cookies."""
        self.label_cashier = Label(self.frame_shop, text=(self.cashier, "€"),
                                   font=("Courrier", 80, 'bold'),
                                   bg=marron, fg=brun_claire)
        self.label_cashier.pack(expand=YES)

    def create_button_seller(self):
        """Ajout d'un bouton en bas de la frame Shop
        pour vendre les cookies."""
        button_seller = Button(self.frame_shop, text=sell_cookie,
                               bg=marron, fg=brun_claire,
                               activebackground=marron_fonce,
                               command=self.sell_cookie)
        button_seller.pack(pady=2, padx=2, expand=YES, fill=X)

    def refresh_cashier(self):
        """""Actualise le montant de la caisse."""
        return self.label_cashier.config(text=(self.cashier, "€"))

    # Fonctions de commande du boutons coté Kitchen
    def make_cookie(self):
        """Fonction qui incrémente le nombre de cookie.
        Puis fait appel a refresh_cookie_counter."""
        add = 1 * self.pastry_skill
        self.cookie_count += add
        self.refresh_cookie_counter()

    # Fonctions de commande du boutons coté Shop
    def sell_cookie(self):
        """Fonction qui vend transforme les cookies en argent.
        Elle fait appel a la fonction "define_cookie_price".
        Ensuite elle compte le montant du panier total.
        Elle ajoute ce montant a la caisse.
        Puis fait appel a la fonction empty_cookie_count."""
        cookie_price = self.define_cookie_price()
        total_amount = cookie_price * self.cookie_count
        self.cashier += total_amount
        self.empty_cookie_count()
        self.refresh_cashier()

    def define_cookie_price(self):
        """"Fonction pour définir le prix du cookie.
        Prix de base, multipliyé par, le niveau du vendeur."""
        price = self.cookie_starting_price * self.seller_skill
        return price

    def empty_cookie_count(self):
        """Fonction qui vide le panier a cookie
        et qui actualise le compteur."""
        self.cookie_count = 0
        self.refresh_cookie_counter()


# lance le jeu
APP = CookieShop()
APP.window.mainloop()
