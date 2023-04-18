# -*- coding: utf-8 -*-
"""Projet rpg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_dywmHhq6pP2yVLTrpZxQPbblqoZ5EO
"""

def show_menu():
  print("RPG Game Menu")
  print("1. Start game")
  print("2. Ask name")
  print("3. Load game")
  print("4. Credits")
  print("5. Exit")

def main():
  show_menu()
  choice = input("Entrer votre choix: ")
  if choice == "1":
    start_game()
  elif choice == "2":
    ask_name()
  elif choice == "3":
    load_game()
  elif choice == "4":
    show_credits()
  elif choice == "5":
    exit_game()
  else:
    print("Choix invalid")

def start_game():
  print("Starting game...")
  # code pour démarrer le jeu

def ask_name():
  name = input("Entrer votre nom: ")
  print(f"Bienvenue a toi, {name}")
  # a remplacer par le code ask name

def load_game():
  print("Loading game...")
  # code pour charger le jeu

def show_credits():
  print("Created by Yassine Abdou Raouf Cheik Ali, Ismael Dubuc, Saad Abi, Octave Angotti")

def exit_game():
  print("Exiting game...")
  # code pour sortir du jeu

show_menu()

main()

import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) # Get them to fight

import random
# Définition des objets
class Objet:
  def __init__(self, nom, description, valeur):
    self.nom = nom
    self.description = description
    self.valeur = valeur
    
  def __str__(self):
    return f"{self.nom}: {self.description} (valeur={self.valeur})"
# Création d'un objet
lean = Objet("Potion", "elle rend:", 50)
flaki = Objet("Potion", "elle rend:", 70)
#Création d'une liste d'objet
l=[]
l1=[""]
#Calcul de la force du joueur
def force_calcul(a, b):
  return random.randint(a, b)
#Variable Variées
fin = ""
stage = 0
w = 30
z = 80
we = 10
ze = 80
doudoune = 50
katana = 20
attmoment = "poing"
attmoment_e = "hors"
liste_arme = ["poing", "katana", ""]
liste_arme_e = ["hors", "shooters", ""]
arme = 1
# Définition des personnages
class Personnage:
  def __init__(self, nom, sante, force, defense):
    self.nom = nom
    self.sante = sante
    self.force = force
    self.defense = defense
      
  def attaquerj(self, cible):
    # Calcul les dégâts causés
    degats = self.force - cible.defense
    # Si les dégâts sont positifs, on inflige des dégâts à la cible
    if degats > 0:
      cible.sante -= degats
      if attmoment == "poing":
        print(f"{self.nom} met une droite et enlève {degats} points de dégâts à {cible.nom}.")
      elif attmoment == "katana":
        print(f"{self.nom} plante son katana directement dans sa cible et enlève {degats} points de dégâts à {cible.nom}.")
    else:
      print(f"{self.nom} n'a pas mis un coup assez puissant pour blesser {cible.nom}.")

  def attaquere(self, cible):
    # Calcul les dégâts causés
    degats = self.force - cible.defense
    # Si les dégâts sont positifs, on inflige des dégâts à la cible
    if degats > 0:
      cible.sante -= degats
      print(f"{ennemi.nom} vous a mis",degats,"!")
    else:
      print(f"{self.nom} n'a pas mis un coup assez puissant pour blesser {cible.nom}.")
      
  def __str__(self):
    return f"{self.nom}: pv={self.sante}"

# Création des personnages
joueur = Personnage("Freeze corleone", 100, force_calcul(w, z), 0)
ennemi = Personnage("Gazo", 100, force_calcul(we, ze), 0)
ennemi2 = Personnage("1Pliké140", 100, force_calcul(we, ze), 0)
ennemi3 = Personnage("Bolloré", 170, force_calcul(we, ze), 0)
listennemi = [ennemi, ennemi2, ennemi3, "fin"]
# Définition des variables
pv_max = ennemi.sante
pvj_max = joueur.sante
#move
def move():
  direction = input("\n4 choix se présente a vous, vous pouvez aller à droite, gauche ou en face")
  if direction == "droite":
    return "droite"
  elif direction == "gauche":
    return "gauche"
  elif direction == "en face":
    return "front"
  else:
    print("Invalid direction")
    return move()
# Combat
def sys_combat(joueur, ennemi, w, z, we, ze):
  print("\nVous rentrez dans une salle et vous tombez face à face avec "f"{ennemi.nom}")
  i_j = 0
  i_e = 0
  while joueur.sante > 0 and ennemi.sante > 0:
    # Affichage des informations sur les personnages
    print(joueur)
    print(ennemi)
    print()
    
    # Tour du joueur
    choix = input("Que voulez-vous faire? (attaquer/defendre/heal)")
    if choix == "attaquer":
      joueur.attaquerj(ennemi)
      joueur.force = force_calcul(w, z)
    elif choix == "defendre":
      i_j += 1
      if i_j <= 3:
        joueur.defense += 10
        print(f"{joueur.nom} se muscle et gagne 10 points de défense.")
      else:
        print("Vous êtes déjà trop musclé")
    elif choix == "heal":
      print("Choissisez votre objet parmis la liste suivante (taper le numéro de l'emplacement de l'objet)")
      print(l1)
      num=int(input(""))
      num = num-1
      joueur.sante += l[num].valeur
      print(f"{joueur.nom} se heal avec",l1[num],"qui rapporte",l[num].valeur,"points de vie.")
      if joueur.sante > pvj_max:
          joueur.sante = pvj_max
          print("Vos pv ne peuvent pas dépasser",pvj_max,"cependant vous êtes heal au maximum")
      
      del l[num]
      del l1[num]
    else:
      print("Choix inconnu.")
    
    # Tour de l'ennemi (si il est en vie)
    hasard = random.randint(1,10)
    if ennemi.sante > 0:
      if hasard <= 6:
        ennemi.attaquere(joueur)
        ennemi.force = force_calcul(we, ze)
      elif hasard > 6 and hasard <= 8:
        i_e += 1
        if i_e <= 3:
          ennemi.defense += 10
          print(f"{ennemi.nom} se muscle et gagne 10 points de défense.")
        else:
          print(f"{ennemi.nom} est déja trop musclé.")
      else:
        ennemi.sante += 70
        if ennemi.sante > pv_max:
          ennemi.sante = pv_max
        print(f"{ennemi.nom} se heal.")
    # Affichage du résultat
    if joueur.sante <= 0:
      print(f"{ennemi.nom} a gagné !")
    elif ennemi.sante <= 0:
      print(f"{joueur.nom} a gagné !")
#Lancement du combat
#ennemi_i = 0
#if listennemi != []:
#  while listennemi != []:
#    sys_combat(joueur, listennemi[ennemi_i], w, z, we, ze, iloot)
#    attmoment = liste_arme[arme]
#    attmoment_e = liste_arme_e[arme]
#    arme = arme+1
#    ennemi_i += 1
#    iloot += 1
#else:
#  print("Félicitations vous avez battu le racisme en France")
#Lancement du combat avec map
ennemi_i = 0
print("Bienvenue dans TrashTalk, vous êtes Freeze corleone et après un son controversé vous êtes poursuivi par les raciste.\nVotre mission aujourd'hui est de quitter la France en esquivant les racistes sur votre route.\nVous commencez votre périple à Saint Denis, nous nous retrouverons à l'aéroport. Enfin si vous arrivez jusque la...")
while fin != "end":
  print("Stage ", stage)
  choixDirection = move()
  print("choix : ", choixDirection)
  #print("La direction choisie est ", choixDirection)
  if stage == 0:
    if choixDirection == "droite":
      #print("On va à droite")
      stage = 1
    elif choixDirection == "gauche":
      #print("On va à gauche")
      stage = 2
    elif choixDirection == "front":
      #print("On va en face")
      stage = 3

  if stage == 1:
    #print("On entre dans le stage 1")
    print("\nVous tombez nez à nez avec zuukoue mayzie, il vous donne une lean (permet de récuperer des hp en combat)")
    l.append(lean)
    l1.append("lean")
    print("Derrière lui il n'y a plus de chemin, vous revenez sur vos pas")
    stage = 0
  if stage == 2:
    #print("On entre dans le stage 2")
    print("Vous tombez nez à nez avec Gazo, vous êtes dans sa ville et il n'est visiblement pas content de vous voir...")
    sys_combat(joueur, ennemi, w, z, 40, 80)
    print("Gazo pars en courant et fais tomber sa Doudoune Gucci, vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
    print("Vous montez au niveau 2, vos stats s'améliorent...")
    w += 20
    z += 20
    pv_max += 30
    joueur.defense = 20
    stage = 0
  if stage == 3:
    joueur.sante = pv_max
    print("\nVous sortez de Saint Denis, êtes vous sur de vous ?\n(il est conseillé d'avoir fait toutes les directions avant de sortir de Saint Denis)")
    sortie = input("\noui ou non")
    if sortie == "oui":
      stage = 4
    else: 
      stage = 0
  if stage == 4:
    print("\nVous êtes bien arrivé à Paris, la capitale de l'amour, du tourisme et du ça vient d'ou ?")
    choixDirection = move()
    if choixDirection == "droite":
      #print("On va à droite")
      stage = 7
    elif choixDirection == "gauche":
      #print("On va à gauche")
      stage = 5
    elif choixDirection == "front":
      #print("On va en face")
      stage = 9
  if stage == 5:
    print("Oeeee mon gas ! Ca vient d'ou la ? He vide ta sacoche et donne moi ton tel")
    sys_combat(joueur, ennemi, w, z, 50, 90)
    print("1plike140 est dans le coma, vous en profitez pour récupérer son opinel 13, vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
    w += 10
    z += 10
    stage = 4
  if stage == 9:
    print("Vous voyez un groupe d'albanais partir au loin, ils ont laissé leur moto et il reste un casque arai dessus")
    print("Vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
    stage = 4
  if stage == 7:
    print("Vous récuperez les pdf interdit coffré par Osirus Jack")
    stage = 4

import random
import sys
# Définition des objets
class Objet:
  def __init__(self, nom, description, valeur):
    self.nom = nom
    self.description = description
    self.valeur = valeur
    
  def __str__(self):
    return f"{self.nom}: {self.description} (valeur={self.valeur})"
# Création d'un objet
potion = Objet("Potion", "elle rend:", 20)
lean = Objet("Potion", "elle rend:", 50)
flaki = Objet("Potion", "elle rend:", 70)
#Création d'une liste d'objet
l=[potion]
l1=["potion"]
#Calcul de la force du joueur
def force_calcul(a, b):
  return random.randint(a, b)
#Variable Variées
fin = ""
stage = 0
w = 30
z = 80
we = 20
ze = 40
doudoune = 50
katana = 20
attmoment = "poing"
attmoment_e = "hors"
liste_arme = ["poing", "katana", ""]
liste_arme_e = ["hors", "shooters", ""]
arme = 1
# Définition des personnages
class Personnage:
  def __init__(self, nom, sante, force, defense):
    self.nom = nom
    self.sante = sante
    self.force = force
    self.defense = defense
      
  def attaquerj(self, cible):
    # Calcul les dégâts causés
    degats = self.force - cible.defense
    # Si les dégâts sont positifs, on inflige des dégâts à la cible
    if degats > 0:
      cible.sante -= degats
      if attmoment == "poing":
        print(f"{self.nom} met une droite et enlève {degats} points de dégâts à {cible.nom}.")
      elif attmoment == "katana":
        print(f"{self.nom} plante son katana directement dans sa cible et enlève {degats} points de dégâts à {cible.nom}.")
    else:
      print(f"{self.nom} n'a pas mis un coup assez puissant pour blesser {cible.nom}.")

  def attaquere(self, cible):
    # Calcul les dégâts causés
    degats = self.force - cible.defense
    # Si les dégâts sont positifs, on inflige des dégâts à la cible
    if degats > 0:
      cible.sante -= degats
      print(f"{self.nom} vous a mis",degats,"!")
    else:
      print(f"{self.nom} n'a pas mis un coup assez puissant pour blesser {cible.nom}.")
      
  def __str__(self):
    return f"{self.nom}: pv={self.sante}"

# Création des personnages
joueur = Personnage("Freeze corleone", 130, force_calcul(w, z), 0)
ennemi = Personnage("Gazo", 100, force_calcul(we, ze), 0)
ennemi2 = Personnage("Darmanin", 130, force_calcul(we, ze), 0)
ennemi3 = Personnage("1Pliké140", 100, force_calcul(we, ze), 0)
ennemi4 = Personnage("Ateyaba", 150, force_calcul(we, ze), 0)
ennemi5 = Personnage("Bolloré", 150, force_calcul(we, ze), 0)
ennemi6 = Personnage("Zemmour", 50, force_calcul(we, ze), 0)
ennemi7 = Personnage("Menace Santana", 180, force_calcul(we, ze), 0)
ennemi8 = Personnage("Jean-Marie Le Pen", 230, force_calcul(we, ze), 0)
listennemi = [ennemi, ennemi2, ennemi3, ennemi4, ennemi5, ennemi6, ennemi7, ennemi8, "fin"]
# Définition des variables
pv_max = ennemi.sante
pvj_max = joueur.sante
#move
def move():
  direction = input("\n3 choix se présente a vous, vous pouvez aller à droite, gauche ou en face")
  if direction == "droite":
    return "droite"
  elif direction == "gauche":
    return "gauche"
  elif direction == "en face":
    return "front"
  else:
    print("Direction non connu")
    return move()
# Combat
def sys_combat(joueur, ennemi, w, z, we, ze):
  print("\nVous rentrez dans une salle et vous tombez face à face avec "f"{ennemi.nom}")
  i_j = 0
  i_e = 0
  while joueur.sante > 0 and ennemi.sante > 0:
    # Affichage des informations sur les personnages
    print(joueur)
    print(ennemi)
    print()
    
    # Tour du joueur
    choix = input("Que voulez-vous faire? (attaquer/defendre/heal)")
    if choix == "attaquer":
      joueur.attaquerj(ennemi)
      joueur.force = force_calcul(w, z)
    elif choix == "defendre":
      i_j += 1
      if i_j <= 3:
        joueur.defense += 10
        print(f"{joueur.nom} se muscle et gagne 10 points de défense.")
      else:
        print("Vous êtes déjà trop musclé")
    elif choix == "heal":
      print("Choissisez votre objet parmis la liste suivante (taper le numéro de l'emplacement de l'objet)")
      print(l1)
      num=int(input(""))
      num = num-1
      joueur.sante += l[num].valeur
      print(f"{joueur.nom} se heal avec",l1[num],"qui rapporte",l[num].valeur,"points de vie.")
      if joueur.sante > pvj_max:
          joueur.sante = pvj_max
          print("Vos pv ne peuvent pas dépasser",pvj_max,"cependant vous êtes heal au maximum")
      
      del l[num]
      del l1[num]
    else:
      print("Choix inconnu.")
    
    # Tour de l'ennemi (si il est en vie)
    hasard = random.randint(1,10)
    if ennemi.sante > 0:
      if hasard <= 6:
        ennemi.attaquere(joueur)
        ennemi.force = force_calcul(we, ze)
      elif hasard > 6 and hasard <= 8:
        i_e += 1
        if i_e <= 3:
          ennemi.defense += 10
          print(f"{ennemi.nom} se muscle et gagne 10 points de défense.")
        else:
          print(f"{ennemi.nom} est déja trop musclé.")
      else:
        ennemi.sante += 50
        if ennemi.sante > pv_max:
          ennemi.sante = pv_max
        print(f"{ennemi.nom} se heal.")
    # Affichage du résultat
    if joueur.sante <= 0:
      print(f"{ennemi.nom} a gagné !")
      print("Game Over")
      sys.exit()

    elif ennemi.sante <= 0:
      print(f"{joueur.nom} a gagné !")
#Lancement du combat
#ennemi_i = 0
#if listennemi != []:
#  while listennemi != []:
#    sys_combat(joueur, listennemi[ennemi_i], w, z, we, ze, iloot)
#    attmoment = liste_arme[arme]
#    attmoment_e = liste_arme_e[arme]
#    arme = arme+1
#    ennemi_i += 1
#    iloot += 1
#else:
#  print("Félicitations vous avez battu le racisme en France")
#Lancement du combat avec map
print("Bienvenue dans TrashTalk, vous êtes Freeze corleone et après un son controversé vous êtes poursuivi par les raciste.\nVotre mission aujourd'hui est de quitter la France en esquivant les racistes sur votre route.\nVous commencez votre périple à Saint Denis, nous nous retrouverons à l'aéroport. Enfin si vous arrivez jusque la...")
xp = 0
xp1 = 0
xp2 = 0
xp3 = 0
xp4 = 0
xp5 = 0
itemloot = 0
def xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5):
  if xp1 == 0:
    if xp >= 100:
      print("Vous passez niveau 1 EKIP")
      w += 10
      z += 10
      xp1 += 1
  if xp2 == 0:
    if xp >= 250:
      print("Vous passez niveau 2 MMS")
      w += 15
      z += 15
      xp2 += 1
  if xp3 == 0:
    if xp >= 300:
      print("Vous passez niveau 3 LDO")
      w += 20
      z += 20
      xp3 += 1
  if xp4 == 0:
    if xp >= 350:
      print("Vous passez niveau 4 NRM")
      w += 30
      z += 30
      xp4 += 1
  if xp5 == 0:
    if xp >= 400:
      print("Vous passez niveau 5 667")
      w += 40
      z += 40
      xp5 += 1
def stage0():
  choixDirection = move()
  if choixDirection == "droite":
    print("on va à droite")
    stage1()
    stage0()
  elif choixDirection == "gauche":
    print("On va à gauche")
    stage2(w, z, xp, xp1, xp2, xp3, xp4, xp5, joueur.defense)
    stage0()
  elif choixDirection == "front":
    print("On va en face")
    stage3(w, z, xp, joueur.sante, xp1, xp2, xp3, xp4, xp5, itemloot)

def stage1():
  print("\nVous tombez nez à nez avec zuukoue mayzie, il vous donne une lean (permet de récuperer des hp en combat)")
  l.append(lean)
  l1.append("lean")
  print("Derrière lui il n'y a plus de chemin, vous revenez sur vos pas")

def stage2(w, z, xp, xp1, xp2, xp3, xp4, xp5, f):
  print("Vous tombez nez à nez avec Gazo, vous êtes dans sa ville et il n'est visiblement pas content de vous voir...")
  sys_combat(joueur, ennemi, w, z, 30, 50)
  print("Gazo pars en courant et fais tomber sa Doudoune Gucci, vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
  print("Vous montez d'un niveau, vos stats s'améliorent...")
  print("Derrière lui il n'y a plus de chemin, vous revenez sur vos pas")
  f += 30
  xp += 100
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)

def stage3(w, z, xp, f, xp1, xp2, xp3, xp4, xp5, itemloot):
  print("vous etes proche de la sortie de la ville est croiser Darmanin qui vous menace d'appeler des crs si vous parter d'ici")
  sys_combat(joueur, ennemi2, w, z, 30, 50)
  print("Darmanin vous supplie d'arreter de le frapper et vous donne un passport ainsi qu'une giga kichta")
  itemloot += 1
  print("vous montez au niveau 3, vos stats s'améliorent...")
  xp += 150
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)
  f += 100
  print("\nVous sortez de Saint Denis, êtes vous sur de vous ?\n(il est conseillé d'avoir fait toutes les directions avant de sortir de Saint Denis)")
  sortie = input("\noui ou non")
  if sortie == "oui":
    print("\nVous êtes bien arrivé à Paris, la capitale de l'amour, du tourisme et du ça vient d'ou ?")
    stage4()
  else: 
    stage0()

def stage4():
  choixDirection = move()
  if choixDirection == "droite":
    print("vous parter a droite")
    stage7(itemloot)
    stage8(w, z, xp, joueur.sante, xp1, xp2, xp3, xp4, xp5, itemloot)
  elif choixDirection == "gauche":
    print("vous partez a gauche")
    stage5(w, z, xp, xp1, xp2, xp3, xp4, xp5)
    stage6(itemloot)
    stage4()
  elif choixDirection == "front":
    print("vous partez en face")
    stage9(joueur.defense, itemloot)
    stage10(w, z, xp, xp1, xp2, xp3, xp4, xp5, itemloot)
    stage4()

def stage7(itemloot):
  print("Vous récuperez les pdf interdit coffré par Osirus Jack")
  itemloot += 1

def stage9(f, itemloot):
  print("Vous voyez un groupe d'albanais partir au loin, ils ont laissé leur moto et il reste un casque arai dessus")
  itemloot += 1
  print("Vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
  f += 10

def stage5(w, z, xp, xp1, xp2, xp3, xp4, xp5):
  print("Oeeee mon gas ! Ca vient d'ou la ? He vide ta sacoche et donne moi ton tel")
  sys_combat(joueur, ennemi3, w, z, 50, 70)
  print("1plike140 est dans le coma, vous en profitez pour récupérer son opinel 13, vous l'équipez (équiper le stuff de vos ennemis augmente vos stats...)")
  w += 20
  z += 20
  xp += 150
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)

def stage6(itemloot):
  print("Vous croiser Femtogo, il vous donne 2 sac de guala et du flaki")
  itemloot += 1
  l.append(flaki)
  l1.append("flaki")
  print("il n'y a rien derriere lui, vous revenez sur vos pas")

def stage10(w, z, xp, xp1, xp2, xp3, xp4, xp5, itemloot):
  print("Oui bitch tu ma pas s/o dans un de tes sons alors que t'es un de mes fils !!!")
  print("vous tomber nez a nez avec Ateyaba et il n'a pas l'air de vous apprecier...")
  sys_combat(joueur, ennemi4, w, z, 50, 70)
  print("Ateyaba prend la fuite comme d'hab mais il fait tomber son disque dur et un exemplaire unique de son projet Ultraviolet")
  itemloot += 1
  xp += 50
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)

def stage8(w, z, xp, f, xp1, xp2, xp3, xp4, xp5, itemloot):
  print("Vous avez le malheur de croiser Vincent Bolloré et il n'a pas l'air d'avoir apprécier vos propos dans vos musique...")
  sys_combat(joueur, ennemi5, w, z, 60, 70)
  print("vous avais effrayer Bolloré il vous donne les clés de sont jet privé et de son M2 compet pour vous dirigé vers l'aeroport")
  itemloot += 2
  xp += 150
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)
  f += 100
  print("\nVous sortez de Paris, êtes vous sur de vous ?\n(il est conseillé d'avoir fait toutes les directions avant de sortir de Paris)")
  sortie = input("\noui ou non")
  if sortie == "oui":
    print("\nVous rouler a 240km/h jusqu'a l'aeroport, vous etes enfin arriver a votre derniere destination avant de fuir ce pays de de raciste")
    stage11()
  else: 
    stage4()

def stage11():
  choixDirection = move()
  if choixDirection == "droite":
    print("on va a droite")
    stage13(w, z, xp, xp1, xp2, xp3, xp4, xp5)
    stage11()
  elif choixDirection == "gauche":
    print("on va a gauche")
    stage12(w, z, xp, joueur.sante, pv_max, xp1, xp2, xp3, xp4, xp5)


  elif choixDirection == "front":
    print("on va en face")
    stage14(w, z)
    stage11()
    
def stage12(w, z, xp, f, h, xp1, xp2, xp3, xp4, xp5):
  print("l'avion pret a décoller vous courer vers celui-ci et vous entender un cris derriere vous ?")
  print("Reviens ici sale immigrer !!,vous tomber nez a nez avec Jean-Marie Le Pen qui ne veut pas vous lacher vous aller devoir vous occuper de lui avant de pouvoir partir")
  sys_combat(joueur, ennemi8, w, z, 50, 90)
  print("Vous avez remis les idées en place a Jean-Marie Le Pen, il decide de quitter la France pour vivre comme un moine sur une montagne au Yemen")
  xp += 50
  xpstats(xp, w, z, xp1, xp2, xp3, xp4, xp5)
  print("Vous parvenez a prendre l'avion et quitter enfin la France apres l'avoir pillez une derniere fois")
  print("Vous avez fini le jeu avec un score de",itemloot,"(votre score équivaut au nombre d'objet que vous avez ramassée pendant le combat)")

def stage13(w, z, xp, xp1, xp2, xp3, xp4, xp5):
  print("BuubuuBinks tu va avalez ma lame comme si c'etait du Schweppes")
  print("pas de chance vous allez devoir combattre Menace Santana")
  sys_combat(joueur, ennemi7, w, z, 60, 70)
  print("Menace Santana disparait lanssant derriere lui un Samourai+ (équiper le stuff de vos ennemis augmente vos stats...)")
  w += 20
  z += 20
  xp += 50
  xpstats(xp, w, z)
  print("vous vous rendez compte que ce n'est pas le bon chemin vous revenez donc sur vos pas")

def stage14(w, z):
  print("toi fait moi voir t'es valises !")
  print("éric Zemmour veut vous controler vous devait lui faire face")
  sys_combat(joueur, ennemi6, w, z, 10, 30)
  print("éric Zemmour a retenu la leçon et décide de changer de partit politique pour rejoindre celui de gauche")
  print("vous vous rendez compte que ce n'est pas le bon chemin vous revenez donc sur vos pas")
stage0()