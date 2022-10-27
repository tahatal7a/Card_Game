


                                                                #### Card Game. ####
                                                                #### Jeu de cartes. ####



# L'ordinateur est le donneur des cartes.
# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') 
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

    
def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]

     for i in range(len(p)):
         if i%2==0:
            donneur.append(p[i])
         else:
            autre.append(p[i])
     
     return (donneur, autre)


def elimine_paires(l):
   

    resultat=[]
    l.sort()

    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']  
    liste = []                                          

    for i in l:                                        
        for j in i:                                     
            
            if j == '\u2660' or j == '\u2661' or j == '\u2662' or j == '\u2663' or j == "0" :  
                break
            else:                                       
                if len(i)== 3:   
                    liste.append("10")
                elif len(i) == 2 : 
                    liste.append(j)
            
    liste1 = []
    for i in liste:
        if i  in liste1: 
            liste1.remove(i)
        else : 
            liste1.append(i)
    
    liste2= []
    for x in liste1:
        for y in couleurs: 
            if (x+y) in l: 
                liste2.append(x+y)
                break
    l = liste2.copy()  
    resultat = l.copy() 
        

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    for i in p: 
        print(i, end =" ") 
 

def entrez_position_valide(n):

     resultat = False 
     valeur = int(input("SVP entrez un entier de 1 à "+str(n)+" : "))
     while resultat == False: 
         if valeur  in range(1,n+1): 
             resultat=True
         else : 
             valeur = int(input("SVP entrez un entier de 1 à "+str(n)+" : "))
     return valeur




def fct1(humain,robot):#le tour de l'humain
    print("votre tour.")
    print("Votre main est : ")
    affiche_cartes(humain)
     
    print("J'ai",len(robot)," carte . Si 1 est la position de ma première carte et ",len(robot)," la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
    n = entrez_position_valide(len(robot))
    print("Vous avez demande ma",n,"eme carte")
    carte = robot[n-1]
    print("La voila . C'est un :",carte)
    humain.append(carte)
    robot.remove(carte)
    if robot == []:
        return (robot,humain)
    else :
        print("avec",carte,"ajoute a votre main. Votre main est :")
        affiche_cartes(humain)
        humain=elimine_paires(humain)
        print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
        affiche_cartes(humain)
        return (robot,humain)

def fct2(humain,robot):#le tour du robot
    print("Mon tour")
    n = random.randint(1,len(humain)) 
    carte = humain[n-1]
    print("J'ai pris votre  :",n,"eme carte")
    robot.append(carte)
    humain.remove(carte)
    robot=elimine_paires(robot)
    return (robot,humain)

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

    
     termine = False 
     player = 1 
     if len(humain) == 0:
            termine = True 
     while not termine:
         if player == 1:
             print("***********************************************************")
             print("Votre tour.")
             print("Votre main est:",end = "\n")
             affiche_cartes(humain)
             print("J'ai",len(donneur),"cartes. Si 1 est la position de ma première carte et",len(donneur),"est la position de ma dernière carte, laquelle de mes cartes vous voulez?")
             choixHumain = entrez_position_valide(len(donneur))
             
             if choixHumain == 1:
                 print("Vous avez demande ma 1ère carte.")
             else :
                 print("Vous avez demande ma",str(choixHumain)+"ème carte.")
             print("La voila. C'est un",donneur[choixHumain-1])
             print("Avec",donneur[choixHumain-1],"ajouté, votre main est:")
             humain.append(donneur[choixHumain-1])
             affiche_cartes(humain)
             print("Après défaussé toutes les paires et mélanger les cartes, votre main est:")
             humain = elimine_paires(humain)
             affiche_cartes(humain)
             donneur.remove(donneur[choixHumain-1]) 
             
             if len(donneur) == 0 or len(humain) == 0:
                 termine = True #devient true si l'un des joueurs n'a plus de cartes
             player = 2 
             attend_le_joueur()
         else :
             print("***********************************************************")
             print("Mon tour.")
             choixRobot = random.randint(1,len(humain)) 
             
             if choixRobot == 1:
                 print("J'ai pris votre 1ère carte.")
             else :
                 print("J'ai pris votre",str(choixRobot)+"ème carte.")
             donneur.append(humain[choixRobot-1])
             #ajoute la carte choisi au cartes du robot
             donneur = elimine_paires(donneur)
             #elimine les paires des cartes du robot
             humain.remove(humain[choixRobot-1])
             #elimine la carte choisie des cates de l'humain
             
             if len(donneur) == 0 or len(humain) == 0:
                 termine = True
                 #devient true si l'un des joueurs n'a plus de cartes
             player = 1 
             attend_le_joueur()
     
     print("***********************************************************")
     if len(donneur) == 0 : 
        print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
     else : 
        print("Vous avez terminé toutes les cartes.\nFelicitations! Vous, Humain, vous avez gagné.")
        
         
         
         

joue()
