import sys

sys.path.insert(0, './biblio_ext')
import sys

sys.path.insert(0, './biblio_ext')
from gopigo import *
import time, math
import requests
from grovepi import *
import os  # pour PushBullet


def DeroulerFeuille(coef):
	from modules.Incnbfeuille import incrementerNombreFeuille
	incrementerNombreFeuille()
	tmpRotation = (coef*1.5)/360
	print("---->")
	print(tmpRotation)
	fwd()
	time.sleep(tmpRotation)
	stop()
	time.sleep(4)
	main()

def calculerRestantSopalin():
    ultrasonic_ranger = 7
    valeurCapteur = 1
    try:
        valeurCapteur = float(ultrasonicRead(ultrasonic_ranger))  # mettre notre fonction capteur
    except TypeError:
        print "Error"
    distanceCapteurRouleau = 12  # valeur constante a calculer
    from modules.ChangerCouleur import ChangerCouleur
    ChangerCouleur(valeurCapteur)
    print("----------")
    print(valeurCapteur)
    if (valeurCapteur < distanceCapteurRouleau):
        print("peut derouler")
        from modules.CalculerCoef import CalculerCoef
        coef = CalculerCoef(valeurCapteur, distanceCapteurRouleau)
        print("*************")
	print(coef)
	DeroulerFeuille(coef);
	
    else:
        print("peut pas derouler")
	from modules.EteindreProgramme import Eteindre_prog
	Eteindre_prog()
	main()
	

def main():

    #try:
       # ChangerCouleur(ultrasonicRead(7))
    #except:
    #    print("le systeme ne peut fonctionner")
    capteur_main = 8
    main = False
    valeur = 11
    while (main == False):
       
        try:
            valeur = ultrasonicRead(capteur_main)
        except:
            print("error")
	from modules.EstAllumer import est_allumer
        if (valeur < 5 and est_allumer()):
            print("main trouve")
            main = True
            calculerRestantSopalin()
	

main()
