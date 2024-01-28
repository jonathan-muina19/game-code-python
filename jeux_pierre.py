import random

options = ("piere","papier","cisceau")
playing = True

while playing:
    
    user = None
    IA = random.choice(options)
    
    while user not in options:
        user = input("Entrer votre choix(Pierre, papier , cisceau): ")

    print(f"Moi:{user}")
    print(f"I.A:{IA}")

    if user == IA:
        print("Egalité !")
    elif user == "piere" and IA == "cisceau":
        print("C'est gagner !")
    elif user == "papier" and IA == "piere":
        print("C'est gagner !")
    elif user == "cisceau" and IA == "papier":
        print("C'est gagner !")
    else:
        print("C'est perdu!")
    
    if not input("Voulez-vous continuer de jouer?:(o/n)").lower() == "o":
        playing = False
        
print("Fin du jeu!")
