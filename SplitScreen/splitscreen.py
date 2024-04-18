# UPBGE 0.36.1
# Python Component for Splitscreen
# script by Ludérïck Le Saouter @LLS
# CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
# update V2: 18/04/2024

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
        self.actif = args["Activate"]
        self.gauche = args["Left"]
        self.bas = args["Bottom"]
        self.droite = args["Right"]
        self.haut = args["Top"]
        self.camera = args["Camera"]
        self.actionneur = args["PropertyActif"]
        
        self.scene = bge.logic.getCurrentScene()
        self.objet = self.scene.objects
        self.cam = self.scene.objects[self.camera]
    
    def activation(self):
        prop = str(self.actionneur)
        prop_verifier = [obj for obj in self.objet if prop in obj]
        for element in prop_verifier:
            if element[prop] == True:
                self.actif = True
                break
            else:
                self.actif = False
        
    def tailleEcran(self):
        self.ecran_H = bge.render.getWindowHeight()
        self.ecran_L = bge.render.getWindowWidth()
        self.scene = bge.logic.getCurrentScene()
        
        Gauche = self.ecran_L*self.gauche; Bas = self.ecran_H*self.bas; Droite = self.ecran_L*self.droite; Haut = self.ecran_H*self.haut
        
        Gauche = int(Gauche)
        Bas = int(Bas)
        Droite = int(Droite)
        Haut = int(Haut)
        
        self.cam.setViewport(Gauche, Bas, Droite, Haut)
        self.cam.useViewport = True
    
    def update(self):
        self.activation()
        if self.actionneur is not None:
            if self.actif is True:
                self.tailleEcran()
            else:
                self.cam.useViewport = False
        else:
            self.tailleEcran()