import time
import sys
from PIL import Image
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QMovie
import webbrowser


class Window(QWidget): #Création d'un gif
    def __init__(self, filename, dim):
        super().__init__()
        x, y, w, h = dim
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("gif")
        label = QLabel(self)
        movie = QMovie(filename)
        label.setMovie(movie)
        movie.start()


def render_gif(filename, dimensions):
    app = QApplication([])
    window = Window(filename, dimensions)
    window.show()
    app.exec()



def check(question, group): #détermine si une réponse est valide ou non
    while True:
        ans = input(question).lower()
        if ans == "q":
            impr("Merci d'avoir utilisé ce logiciel.")
            sys.exit() #quitter
        time.sleep(0.5)
        if ans == "":
            print("Entrez votre réponse.")
            continue
        if ans in group:
            return ans #la réponse est valide
        else:
            print("Votre entrée n'est pas valide, essayez encore.")

def impr(text): #Permet le texte d'aller de gauche à droite
    for i in list(text):
        print(i, end="")
        if i == "." or i == "?":
            time.sleep(.1)
        if i == "," or i == ";":
            time.sleep(0.07)
        else:
            time.sleep(0.04)
        
    print("")
    
def fin():
    for i in range(3):
        print(". ", end="")
        time.sleep(1)
    print("\n")



def run():

    impr("\nBonjour et bienvenu à la présentation de Noah à propos du transformateur.")
    impr("(entrez q pour quitter et le bouton 'enter' pour continuer)")
    input("")

    c1 = False #AC
    c2 = False #Watt
    c3 = False #bobine
    c4 = False #Induction
    c5 = False #FEM
    c6 = False #fonctionnement
    c7 = False # utilite (general)
    c8 = False #histoire
    c9 = False #ingenieur mecanique
    c10 = False # extras
    c11 = False #explanation courte
    c12 = False #explanation longue
    c13 = False #utilite
    c14 = False #voltage = moins de pertes
    c15 = False #tension de claquage
    

        
    while True:
        impr("Choisissez une de ces options:")
        impr(" 1: Le fonctionnement d'un transformateur {}".format(("(déjà fait)" if c6 else '')))
        impr(" 2: L'utilité du transformateur {}".format(("(déjà fait)" if c7 else '')))
        impr(" 3: L'histoire du transformateur {}".format(("(déjà fait)" if c8 else '')))
        impr(" 4: L'ingénieur mécanique {}".format(("(déjà fait)" if c9 else '')))
        impr(" 5: Extras {}".format(("(déjà fait)" if c10 else ''))) #inclure bibliographie
        impr(" 6: Quitter")
        
        ans = check("", ["1",  "2", "3", "4", "5", "6"])
        
        if ans == "6":
            impr("Merci d'avoir utilisé ce logiciel.")
            sys.exit() #quitter

        time.sleep(.3)


        if ans == "1": #Le fonctionnement d'un transformateur
            c6 = True

            impr("\nLe transformateur électrique est un système qui permet de changer")
            impr("l'intensité de courant et la différence de potentiel d'un courant alternatif.")
            impr("Elle est similaire à l'engrenage en mecanique.")
            input("")
            
            impr("Le transformateur est, à sa base, composé de deux circuits électriques avec")
            impr("des tours dans le câble adjacents.")
            input("")
            
            impr("Voici une représentation d'un transformateur:")
            
            #création d'une image
            im = Image.open(r"C:\Users\noahl\Downloads\transformateur_simpifie.gif")
            im.show()
            input("")
            time.sleep(.2)

            impr("Voici ce qu'un transformateur a l'air réelement:")
            
            #création d'une image
            im = Image.open(r"C:\Users\noahl\Downloads\transformateur_reel.jpg")
            im.show()

            input("")
            time.sleep(0.2)
            

            while True: #Definitions partie 1
                impr("Choissisez une de ces options:")
                impr(" 1: Définition de courant alternatif {}".format(("(déjà fait)" if c1 else '')))
                impr(" 2: Définition du Watt {}".format(("(déjà fait)" if c2 else '')))
                impr(" 3: Continuer")
                ans = check("", ["1", "2", "3"])
                time.sleep(1)
                

                if ans == "1": #AC
                    c1 = True
                    impr("\nUn courant alternatif (AC) est un courant dont la direction du mouvement des électrons,") 
                    impr("du voltage et du courant alternent d'une direction à l'autre.")
                    impr("\nVoir un graphique? (y/n):")

                    ans = check("", ["y", "n"])
                    if ans == "y": 
                        render_gif(r"Alternate-Current-AC.gif", [100, 100, 800, 700])        
                        input("")

                    impr("Notez aussi que le voltage dans un courant alternatif en relation avec le temps")
                    impr("prend une forme sinusoïdale, et puis le transformateur ne change pas sa fréquence.")
                    
                    input("")
                    fin()
                    continue
                
                if ans == "2": #watt
                    c2 = True
                    impr("\nLe watt est une unité de mesure équivalente à une Joule par seconde. Elle")
                    impr("peut être determinée en utilisant ces formules:")
                    impr(" - P = I*ΔV  (P étant la puissance exprimée en watts)")
                    impr(" - P = I²R  (la puissance utilisée par une résistance)")
                    input("")
                    fin()
                    continue
                if ans == "3":
                    break

            while True:
                
                impr("\nAvant d'apprendre comment le transformateur fonctionne, il y a quelques")
                impr("autres concepts à apprendre:")
                time.sleep(.5)
                
                impr("\nChoissisez une de ces options:")
                impr(" 1: La bobine électrique {}".format(("(déjà fait)" if c3 else '')))
                impr(" 2: L'induction électromagnétique {}".format(("(déjà fait)" if c4 else '')))
                impr(" 3: La force électromotrice {}".format(("(déjà fait)" if c5 else '')))
                impr(" 4: Continuer")
                ans = check("", ["1", "2", "3", "4"])
                time.sleep(.5)

                if ans == "1": #bobine
                    c3 = True
                    impr("Une bobine électrique est une partie d'un circuit où le câble se met")
                    impr("en plusieurs boucles; elle crée un champ magnétique autour d'elle quand")
                    impr("un courant lui traverse.")

                    input("")
                    impr("Voici une bobine:")
                    im = Image.open("bobine.jpg")
                    im.show()
                    input("")
                    fin()
                    continue



                elif ans == "2": #Induction
                    c4 = True
                    impr("\nL'induction électromagnétique est une proprieté des conducteurs où,")
                    impr("quand un champ magnétique bouge ou change d'intensité près d'elle, les électrons dans le")
                    impr("conducteur commencent à bouger. Ceci induit un voltage et de l'intensité dans")
                    impr("le courant.") 
                    input("")

                    impr("Voici un exemple de ce phénomène:")
                    render_gif(r"electromagnetic-induction.gif", [400, 250, 750, 400])
                    input("")
                    
                    impr("L'inverse de ce phénomène est aussi vraie: si des électrons dans")
                    impr("un conducteur bougent, ils créent un champ magnétique autour d'elle.")
                    input("")
                    fin()
                    continue
                
                elif ans == "3": #FEM
                    c5 = True
                    impr("La force électromotrice (FEM) est la tension (en volts) produite dans")
                    impr("un courant électrique par l'induction électromagnétique.")
                    input("")

                    impr("Notez que quand il y a plus de tours dans une bobine, il")
                    impr("y a plus de FEM induite par le champ magnétique. Ceci est") 
                    impr("car une il y a plus de câble près de la source magnétique.")
                    input("")
                    fin()
                    continue
                
                else:
                    break
            
            while True:
                impr("Maintenant que vous savez ces cinque termes ci-dessus, c'est le temps")
                impr("d'apprendre comment un transformateur fonctionne:")
                time.sleep(.3)
                
                impr("\nComme vous savez déjà, le transformateur est formée de deux bobines")
                impr("adjacents. Appelons ces bobines bobine 1 et bobine 2.")
                impr("Bobine 1 est connecté à une source d'électricité AC et la bobine 2 est")
                impr("connectée à une lumière. Ce circuit aurait l'air un peu comme ceci:")
                time.sleep(.2)
                im = Image.open(r"diagramme-1.png")
                im.show()
                input("")

                impr("Quand le voltage augmente et diminue dans la bobine 1, son champ magnétique")
                impr("devient plus fort et puis moins fort. Ceci induit du courant et du voltage")
                impr("dans la bobine 2, ce qui fait que la lumière s'allume!")
                input("")

                impr("Voici un diagramme complet de ceci:")
                render_gif(r"how-transformers work.gif", [300, 300, 460, 270])
                input("")
                
                impr("Mais comment est-ce que le transformateur change le voltage et le courant")
                impr("de l'électricité?")
                time.sleep(.1)
                impr("1: Explanation courte".format(("(déjà fait)" if c11 else '')))
                impr("2: Explanation longue".format(("(déjà fait)" if c12 else '')))
                impr("3: Continuer")
                ans = check("", ["1", "2"])
                
                if ans == "1":
                    c11 = True
                    impr("La formule pour déterminer le changement de voltage et d'intensité est celle-ci:")
                    impr("(notez que N = nombre de tours, V = Voltage et I = intensité)")
                    im = Image.open(r"tours-a-voltage.png")
                    im.show()
                    input("")
                    impr("Ceci veut dire que si il y a deux fois le nombre de boucles dans la deuxième")
                    impr("bobine que la première, le voltage dans la deuxième bobine doublera.")
                    impr("Cependant, l'intensité serait réduit de demie.\n")
                    impr("L'opposé est aussi vrai: si la bobine 1 a 10 tours et la bobine 2 en a 5,")
                    impr("et puis l'intensité et le voltage du premier boucle était de 2,5 A et 20V,")
                    impr("on fait:")
                    impr("N₁/N₂ = 10/5 = 2;")
                    impr("N₁/N₂= V₁/V₂; 2 = 20/V₂; V₂ = 10V")
                    impr("N₁/N₂ = I₂/I₁; 2 = I₂/2,5; I₂ = 5A")
                    input("")
                    fin()
                
                if ans == "2":
                    c12 = True
                    impr("La facon dont un transformateur fonctionne est qu'un champ magnétique")
                    impr("induit un courant dans une bobine. Pour comprendre comment les voltages")
                    impr("changent, il faut regarder à une formule.\n")

                    impr("Cette formule est celle qui determine le FEM qui est induit dans un câble:")
                    impr("E = 4,44fNФ")
                    impr(" - E: la moyenne quadratique du voltage induit (equivalent à ce que le voltage serait si elle était DC)")
                    impr(" - f: la fréquence de la vague sinusoïdale du courant en Hertz")
                    impr(" - N: nombre de tours")
                    impr(" - Ф: flux magnétique en V*s (maximale)")
                    
                    impr("\nCe que cette formule signifie est que 4,44fФ est le FEM induit dans une boucle,")
                    impr("et puis on le multiplie par le nombre de boucles.")
                    
                    input("")
                    impr("Cette formule, toutefois, peut aussi fonctionner de renvers pour")
                    impr("trouver le flux magnétique:")
                    impr("Ф = E/(4,44fN)")
                    impr("Si on sait la fréquence, le nombre de tours et le voltage du courant, on peut")
                    impr("determiner le flux magnétique, et puis avec ce flux magnétique on peut determiner")
                    impr("le FEM induit dans la deuxième bobine.")
                    input("")
                    impr("Voici un exemple:")
                    impr("Le voltage d'un courant AC est de 20V, elle a une fréquence de 70 Hz et")
                    impr("elle a 5 tours dans une bobine. La deuxième bobine a 10 tours dans le câble.")
                    impr("C'est quoi le voltage qu'on trouverait dans la deuxième bobine?")
                    input("")
                    impr("Le flux magnétique serait: 20/(4,44*70*5) = 0,0129 V*s\n")
                    impr("Comme on sait que la fréquence reste le même sur les deux cotes, que")
                    impr("le flux magnétique qui l'influence est de 0,0129 V*s et que le nombre de")
                    impr("boucles dans la bobine est de 10, on peut utiliser ces valeurs pour trouver le FEM:\n")
                    impr("E = 4,44*70*10*0,0129 = 40V")
                    input("")

                    impr("Alors, avec ces deux formules, on peut les simplifier beaucoup:")
                    impr("E₂ = 4,44fN₂(E₁/(4,44fN₁))")
                    impr("E₂*4,44fN₁ = E₁*4,44fN₂")
                    impr("E₂*N₁ = E₁*N₂")
                    impr("E₁/E₂ = N₁/N₂")
                    input("")

                    impr("Alors, tout ceci est à dire que le taux du nombre de boucles est la même que le")
                    impr("taux du voltage sur les deux cotes: si la bobine 2 a deux fois le nombre de tours du premier,")
                    impr("elle aura aussi deux fois le voltage.")
                    input("")

                    impr("Toutefois, si on double le nombre de volts sans diminuer le nombre d'amperes,")
                    impr("le nombre de watts doublerait aussi (P = IV). Ceci serait un violement de la loi de")
                    impr("la conservation de l'énergie, ce qui n'est pas possible. Alors, quand le voltage")
                    impr("double, l'intensité est coupe de demie, et vice-versa.\n")
                    
                    impr("La formule qui represente ceci est N₁/N₂ = I₂/I₁.\n")
                    
                    impr("Notez que toutes ces formules s'appliquent pour un transformateur sans")
                    impr("pertes, ce qui n'existe pas. Dans une transformateur reel, le voltage et")
                    impr("l'intensité dans la deuxieme boucle seraient inférieures à leur valeurs")
                    impr("théoriques.")
                    input("")
                    fin()

                else:
                    break
            
        
            impr("Voulez vous apprendre à propos des autres parties du transformateur? (y/n):")
            ans = check("", ["y", "n"])
            if ans == "y":
                impr("Les autres parties du transformateur vont en trois categories: le")
                impr("noyau, l'isolation et le refoidissement.\n")
                impr(" - Le noyau, qui est faite generallement du fer, se trouve au centre")
                impr("   des deux bobines, comme ceci:")
                im = Image.open(r"core.png")
                im.show()
                input("")
                impr(" - Le noyau permet de réduire les pertes magnétiques entre les deux bobines car")
                impr("   il y a moins de distance entre la bobine et le noyau qu'entre les deux bobines.\n")
                impr(" - Il faut isoler toutes les parties du transformateur des unes les autres, incluant")
                impr("   les tours d'une bobine et ses voisins, pour qu'elle fonctionne. Alors, il faut")
                impr("   mettre du verni ou du resin polymere autour des bobines.\n")
                impr(" - Pour augmenter la longueur de vie de l'insulation, il faut refroidir les bobines.")
                impr("   Ceci peut être faite avec la convection naturelle d'eau, ou bien avec de l'huile ou")
                impr("   de l'air.")
                input("")
            
            impr("Vous savez maintenant comment un transformateur fonctionne.👏Wahoo👏.")
            fin("")
            continue

        if ans == 2:
            c7 = True
            impr("Comment important est-ce que le transformateur est? Très, très important.")
            impr("Tout l'électricité qui s'est rendu à votre maison et à cette ecole est")
            impr("passé par au moins deux transformateurs, et generallement plus; la petite")
            impr("boite noire qui est connecte à cet ordinateur est un transformateur. On")
            impr("n'aurait probablement pas les ordinateurs et les machines qu'on à aujourdhui, et si")
            impr("on les avait, ça prenderait beaucoup plus d'énergie et elle serait beaucoup moins")
            impr("versatile. Ça serait comme un monde où les voitures et les bicyclettes avaient qu'un")
            impr("seul engrenage.")
            impr("Mais pourquoi est-ce que le transformateur est-il tellement important?")
            input()
            while True:
                impr("Choissisez une de ces options:")
                impr(" 1: Utilité".format(("(déjà fait)" if c13 else '')))
                impr(" 2: Impact".format(("(déjà fait)" if c1 else '')))
                ans = check("", ["1", "2"])
                if ans == "1":
                    c13 = True

                    impr("Le plus le voltage d’un courant électrique, le moins de pertes d'énergie il")
                    impr("y a. Ceci fait qu'un voltage très haut est utile pour apporter de")
                    impr("l'énergie d’une source d'énergie, comme une centrale nucleaire, autre part.")
                    input("")
                    impr("Cependant, un voltage trop haut ne peut pas être utilisé dans des")
                    impr("circuits, car le voltage serait au dessus de la tension de claquage") 
                    impr("des isolants autour des circuits, ce qui ferait que le circuit ne")
                    impr("fonctionnerait plus.")
                    impr("Comme le transformateur réduire et augmenter le voltage, elle est très")
                    impr("utile dans l’industrie de l’énergie et de l'électronique.")
                    input("")
                    impr("Choisissez une de ces options:")
                    impr(" 1: Pourquoi un voltage plus haut a moins de pertes".format(("(déjà fait)" if c14 else '')))
                    impr(" 2: Tension de claquage".format(("(déjà fait)" if c15 else '')))
                    impr(" 3: Terminer")
                    
                    ans = check("", ["1", "2"])

                    if ans == "1":
                        c14 = True
                        impr("Pour determiner le montant d'énergie perdue dans un câble, on utilise")
                        impr("la formule pour la puissance:")
                        impr("P = I²R (P etant les pertes en Watts et R etant la resistance du câble)") 
                        time.sleep(.2)
                        impr("Alors, sachant que quand on augmente le voltage dans un câble avec un")
                        impr("transformateur, l'intensité du courant est réduit. Ceci fait que des courants")
                        impr("qui ont etes transformes d'un voltage plus bas (pour les centrales d'énergie le")
                        impr("nombre de volts est generallement environ 14 kV) a un voltage beaucoup plus haut")
                        impr("(environ 40 kV a 750 kV) dans des câbles réduit de facon immense les pertes")
                        impr("d'énergie. En fait, si on convertie un courant de 14 kV a un courant de 750 kv,")
                        impr("il y a presque 3000 fois moins de pertes par Ohm de resistance.")
                        input("")
                        impr("Voir la mathematique que Noah a du faire pour avoir ce nombre? (y/n)")
                        ans = check("", ["y", "n"])
                        if ans == "y":
                            impr("Si P₁ = la puissance perdue si le courant ne passe pas par un transformateur et")
                            impr("P₂ = la puissance perdue si le courant est convertie de 14kV a 750 kV:\n")
                            impr("V₂/V1 = I₁/I₂   →  750 000V/14 000V = I₁/I₂  →  I₁/53,6 = I₂")
                            impr("P₁ = I₁²R")
                            impr("P₂ = I₂²R = (I₁/53,6)²*R = I₁²/2900*R")
                            impr("Alors: P1 = 2900*P₂")
                            input("")
                        fin()

                    if ans == "2":
                        c15 = True
                        impr("\nLa tension de claquage est le voltage où un isolant, ou toute autre chose,")
                        impr("devient conductif. Un exemple de ceci est la foudre: si la différence de")
                        impr("potentiel entre les nuages et la terre est assez haute, l'air conduit")
                        impr("l'électricité, et on le voit comme une lumière forte. La tension de claquage")
                        impr("est exprimée en V/cm².")
                        input("")
                        impr("La raison pour que les électroniques ne fonctionnent pas si le voltage est")
                        impr("de 750 kV comme on pourrait voir dans des câbles a haute voltage est que les")
                        impr("petits circuits ont très peu de cm² d'insulation, alors la tension de claquage de")
                        impr("ces insulants seraient facilement éxcedée. Si ceci arrive, ça serait le pandémonium:")
                        impr("le circuit court-circuiterait, l'insulation ne nous protégerait plus, les condensateurs")
                        impr("(capacitors) ne fonctionneraient plus; les petits circuits seraient impossibles a")
                        impr("utiliser.")
                        input("")
                        fin()

                    else:
                        break
        
        if ans == "3":
            c8 = True
            impr("Le site web edisontechcenter.org est la source pour les informations")
            impr("suivantes:\n")
            impr("Qui a inventé le transformateur?")
            impr("\"Ottó Bláthy, Miksa Déri, Károly Zipernowsky de l'Empire austro-hongrois")
            impr("ont d'abord conçu et utilisé le transformateur dans des systèmes")
            impr("expérimentaux et commerciaux. Plus tard, Lucien Gaulard, Sebstian")
            impr("Ferranti et William Stanley en ont perfectionné la conception.\"\n")
            impr("Quand est-ce que le transformateur a t'elle été inventée?")
            impr("La propriété de l'induction a été découverte dans les années 1830, mais")
            impr("ce n'est qu'en 1886 que William Stanley, travaillant pour Westinghouse,")
            impr("a construit le premier transformateur commercial fiable. Son travail s'est")
            impr("appuyé sur des conceptions rudimentaires de la société Ganz en Hongrie")
            impr("(transformateur ZBD 1878), et de Lucien Gaulard et John Dixon Gibbs en Angleterre.")
            impr("Nikola Tesla n'a pas inventé le transformateur comme certaines sources douteuses") 
            impr("l'ont prétendu. Les Européens mentionnés ci-dessus ont effectué les premiers") 
            impr("travaux dans ce domaine. George Westinghouse, Albert Schmid, Oliver Shallenberger") 
            impr("et Stanley ont rendu le transformateur bon marché à produire, et facile") 
            impr("à ajuster pour l'utilisation finale.")
            input("")
            fin()
        if ans == "4":
            c9 = True
            impr("Les ingénieurs mécaniques conceptualisent et planifient la construction de ")
            impr("plusieurs produits électriques dans plusieurs secteurs:")
            impr(" - L'énergie (générateurs, transformateurs, turbines)")
            impr(" - Appareils électroménagers")
            impr(" - Machines pour des bâtiments ou pour des compagnies manufactières (ascenseurs, convoyeurs)\n")
            impr("Ils se soucient plus du côté “hardware” que du côté “software”, et moins sur les")
            impr("parties électriques et plus sur les parties non-électriques.\n")
            impr("Par exemple, Un ingénieur mécanique pourrait travailler avec des ingénieurs électriques pour")
            impr("créer des transformateurs pour le gouvernement ou pour l’industrie. L'ingénieur")
            impr("électrique s’occuperait des parties électriques du transformateur, et puis")
            impr("l'ingénieur mécanique travaillerait sur les parties non électriques du")
            impr("transformateur. L'insolation et la réfrigération seraient des choses dont l'ingénieur")
            impr("mécanique s’occuperait.")
            input("")

            impr("Exigences: diplôme universitaire (baccalauréat ou plus) en génie.\n")
            impr("Habiletés: créativité, communication, résolution de problèmes, aptitudes en calcul.\n")
            impr("Milieu de travail: ils travaillent dans des compagnies manufacturières ou"
            impr("architectes, et puis ils travaillent avec d’autres ingénieurs et des techniciens.\n")
            impr("Taches quoditiennes:")
            impr(" - Evaluer la faisabilité, la conception, les activités ou la performance de")
            impr("   l'équipement, des composantes ou des systèmes")
            impr(" - Travailler avec d’autres ingénieurs pour résoudre des problèmes d’un système et")
            impr("   fournir des informations techniques\n")
            impr("Salaire: 50k-80k-125k; perspective équitable")
            input("")
            fin()

        if ans == "5": #extras
            impr("Choissisez une de ces reponses:")
            impr(" 1: Simulation de transformateur")
            impr(" 2: Bibliographie")
            impr(" 3: Retourner")
            ans = check("", ["1", "2"])
            if ans == "1":
                webbrowser.open("https://www.falstad.com/circuit/e-transformerup.html")
            if ans == "2":
                print("https://edisontechcenter.org/Transformers.html\nhttps://en.wikipedia.org/wiki/Faraday%27s_law_of_induction\nhttps://www.electronics-tutorials.ws/transformer/transformer-basics.html\nhttps://www.nationalgeographic.com/environment/article/lightning")
                print("https://www.quora.com/Why-does-the-current-increase-when-voltage-drops\nhttps://www.electricalsafetyfirst.org.uk/amps-to-watts-calculator/ \nhttps://www.alloprof.qc.ca/fr/eleves/bv/sciences/l-induction-electromagnetique-s1175 ")
                print("https://powertemp.com/what-is-the-purpose-of-a-transformer/\nhttps://www.techno-science.net/definition/3207.html \nhttps://www.explainthatstuff.com/powerplants.html")
                print("https://www.quora.com/What-can-a-mechanical-engineer-do-in-designing-power-transformers\nhttps://en.wikipedia.org/wiki/Breakdown_voltage\nttps://fr.wikipedia.org/wiki/Transformateur_%C3%A9lectrique")
            if ans == "3":
                continue
                

run()
