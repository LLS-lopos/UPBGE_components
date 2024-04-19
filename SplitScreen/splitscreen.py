# UPBGE 0.36.1
# Python Component for Splitscreen
# script by Ludérïck Le Saouter @LLS
# CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
# update V3: 19/04/2024

import bge
from collections import OrderedDict

class Splitscreen(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Activate", False),
        ("Camera", ""),
        ("Left", 0.0),
        ("Bottom", 0.0),
        ("Right", 1.0),
        ("Top", 1.0),
        ("PropertyActif", "")
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.ecran_H = bge.render.getWindowHeight()
        self.ecran_L = bge.render.getWindowWidth()
        self.actif = args["Activate"]
        self.gauche = args["Left"]
        self.bas = args["Bottom"]
        self.droite = args["Right"]
        self.haut = args["Top"]
        self.camera = self.scene.objects[args["Camera"]]
        self.actionneur = args["PropertyActif"]
        self.objet = self.scene.objects

    def activation(self):
        liste_actionneur = self.actionneur.split(", ")
        prop_list = [obj for obj in self.objet if any(prop in obj for prop in liste_actionneur)]
        for element in prop_list:
            if any(element[prop] for prop in liste_actionneur if prop in element and element[prop]):
                self.actif = True
                break
            else:
                self.actif = False

    def tailleEcran(self):
        Gauche = int(self.ecran_L*self.gauche); Bas = int(self.ecran_H*self.bas); Droite = int(self.ecran_L*self.droite); Haut = int(self.ecran_H*self.haut)
        self.camera.setViewport(Gauche, Bas, Droite, Haut)
        self.camera.useViewport = True

    def update(self):
        self.activation()
        if self.actionneur is not None:
            if self.actif is True:
                self.tailleEcran()
            else:
                self.camera.useViewport = False
        else:
            self.tailleEcran()
